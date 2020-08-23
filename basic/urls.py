from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('', Simulation.as_view(), name='simulation_url'),
    path('recent/', Recent.as_view(), name='recent_url'),
    path('save/', SavePlot.as_view(), name='save_plot_url'),
    path('<str:id>/upvote/', Upvote.as_view(), name='upvote_url'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
