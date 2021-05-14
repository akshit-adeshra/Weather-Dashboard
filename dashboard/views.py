from django.shortcuts import render
from .forms import *
import requests

# Create your views here.
def home(request):
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        name = form.cleaned_data.get('name')

        # OpenWeatherMap API handling
        url = f'https://api.openweathermap.org/data/2.5/weather?appid=7e105e5260d0b87cd090d3791f442584&q={name}&units=metric'
        response = requests.get(url)
        json_response = response.json()

        # filtering the required data from the api response
        weather_data = {
            'temp': json_response['main']['temp'],
            'temp_min': json_response['main']['temp_min'],
            'temp_max': json_response['main']['temp_max'],
            'name': json_response['name'],
            'country': json_response['sys']['country'],
            'lat': json_response['coord']['lat'],
            'lon': json_response['coord']['lon'],
            'weather': json_response['weather'][0]['main'],
            'weather_desc': json_response['weather'][0]['description'],
            'pressure': json_response['main']['pressure'],
            'humidity': json_response['main']['humidity'],
            'wind_speed': json_response['wind']['speed'],
        }

    elif request.method == 'GET':
        weather_data = None
        
    context={'form': form, 'weather_data': weather_data}
    return render(request, 'home.html', context)
