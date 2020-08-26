function generateCurve(xFrequency, yFrequency, phase, simulationTime) {
    time = [];
    values = [];
    phaseRad = phase * (Math.PI / 180);
    var k = 0;
    for (i = 0; i < simulationTime; i+=0.0001) { 
        time[k] = i;
        values[k] = {x: Math.sin(xFrequency*time[k] + phaseRad), y:Math.sin(yFrequency*time[k])};
        k++;
    }
    return values;
}

function simulate() {
    // var serializedData = $("#simulateForm").serialize();

    x_frequency = $("#id_x_frequency").val()
    y_frequency = $("#id_y_frequency").val()
    phase = $("#id_phase").val()
    simulation_time = $("#id_simulation_time").val()
    chart.data.datasets[0].data = generateCurve(x_frequency, y_frequency, phase, simulation_time);
    color = $(".jscolor").val();

    chart.data.datasets[0].borderColor = color;
    chart.update();
}

var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'scatter',


    data: {
        datasets: [{
            showLine: true,
            borderColor: '#10E3FF',
            radius: 0,
            fill: false,
            data: generateCurve(100,100,90,1),
        }]
    },
    options: {
        events: [],
        tooltips: {enabled: false},
        animation: {duration: 0},
        hover: {mode: null},
        aspectRatio: 1,
        legend: {display: false},
    }
});

$(function() {

    $("#simulateButton").click(function () {
        simulate();
    });

    $("#saveButton").click(function() {
        simulate();
        var canvas = document.getElementById('myChart');
        document.getElementById("id_image").value = canvas.toDataURL();
        var serializedData = $("#simulateForm").serialize();
        
        $.ajax({
            type: 'POST',
            url: '/save/',
            data: serializedData,
            success: function (response) {
                alert(response.result);
            }
        })
    });


    //base value for inputs
    $("#id_x_frequency").val('100')
    $("#id_y_frequency").val('100')
    $("#id_phase").val('90')
    $("#id_simulation_time").val('1')

    //Sliders handling functions

    $("#slider1").slider({
        value: 100,
        min: 1,
        max: 2000,
        step: 1,
        slide: function(event, ui) {
            $("#id_x_frequency").val(ui.value);
            simulate();
        }
    });

    $("#id_x_frequency").change(function () {
        var value = this.value;
        simulate();
        $("#slider1").slider("value", parseInt(value));
    });

    $("#slider2").slider({
        value: 100,
        min: 1,
        max: 2000,
        step: 1,
        slide: function(event,ui) {
            $("#id_y_frequency").val(ui.value);
            simulate();
        }
    });

    $("#id_y_frequency").change(function () {
        var value = this.value;
        simulate();
        $("#slider2").slider("value", parseInt(value));
    });

    $("#slider3").slider({
        value: 90,
        min: 0,
        max: 360,
        step: 1,
        slide: function(event,ui) {
            $("#id_phase").val(ui.value);
            simulate();
        }
    });

    $("#id_phase").change(function () {
        var value = this.value;
        simulate();
        $("#slider3").slider("value", parseInt(value));
    });
    
    $("#slider4").slider({
        value: 1,
        min: 0.1,
        max: 6.3,
        step: 0.1,
        slide: function(event,ui) {
            $("#id_simulation_time").val(ui.value);
            simulate();
        }
    });

    $("#id_simulation_time").change(function () {
        var value = this.value;
        simulate();
        $("#slider4").slider("value", parseInt(value));
    });
    
});