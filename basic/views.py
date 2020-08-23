import base64
import io
from datetime import datetime
from PIL import Image

from django.shortcuts import render
from django.views.generic import View
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from .forms import CurveParamaterForm
from .generate import generate_lissajou_curve
from .models import LissajousCurve

class Simulation(View):
    def get(self, request):
        form = CurveParamaterForm()
        top_upvotes = LissajousCurve.objects.all().order_by('-upvotes')[:6]
        return render(request, 'simulation.html', {'form': form, 'top': top_upvotes})

    def post(self, request):
        form = CurveParamaterForm(request.POST)
        if form.is_valid():
            data = {
                'x_frequency': form.cleaned_data['x_frequency'],
                'y_frequency': form.cleaned_data['y_frequency'],
                'phase': form.cleaned_data['phase'],
                'simulation_time': form.cleaned_data['simulation_time'],
            }

            return JsonResponse(data, status=200)
        else:
            return render(request, 'simulation.html', {'form': form})


class Recent(View):
    def get(self, request):
        # plots = LissajousCurve.objects.all().order_by('-date')[:12]
        plots = LissajousCurve.objects.all().order_by('-date')
        return render(request, 'recent.html', {'plots': plots})


class SavePlot(View):
    def post(self, request):
        form = CurveParamaterForm(request.POST)

        if form.is_valid():
            new_plot = LissajousCurve()
            new_plot.x_frequency = form.cleaned_data['x_frequency']
            new_plot.y_frequency = form.cleaned_data['y_frequency']
            new_plot.phase = form.cleaned_data['phase']
            new_plot.simulation_time = form.cleaned_data['simulation_time']
            image_url = form.cleaned_data['image']
            decoded_image = base64.b64decode(image_url.split(',')[1])
            # saving image
            time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            file = open(f'media/generated_plots/plot_{time}.png', 'w+b')
            file.write(decoded_image)
            file.close()
            # resizing image
            image_resize = Image.open(f'media/generated_plots/plot_{time}.png')
            image_resize = image_resize.resize((400,400))
            image_resize.save(f'media/generated_plots/plot_{time}.png', quality=100)
            # saving image url to database
            new_plot.image = f'/generated_plots/plot_{time}.png'
            new_plot.save()
    
            return JsonResponse({'result': 'New plot added successfully'}, status=200)
        else:
            return JsonResponse({'result': 'New plot added unsuccessfully'}, status=400)


class Upvote(View):
    def post(self, request, id):
        plot = LissajousCurve.objects.get(id=id)
        # something is upvoted
        if request.COOKIES.get('upvoted'):
            objects_id = request.COOKIES['upvoted']
            list_of_id = objects_id.split()
            # plot already upvoted (delete upvote)
            if id in list_of_id:
                plot.upvotes -= 1
                list_of_id.remove(id)
            # plot not upvoted yet (add upvote)
            else:
                plot.upvotes += 1
                new_cookie = list_of_id.append(id)
            new_cookie = ' '.join(list_of_id)
        # nothing is upvoted
        else:
            plot.upvotes += 1
            new_cookie = str(plot.id)
        plot.save()
        response = HttpResponse()
        response.set_cookie('upvoted', new_cookie, max_age=604800)
        return response
    