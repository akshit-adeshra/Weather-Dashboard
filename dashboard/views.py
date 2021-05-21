from django.shortcuts import render
from dashboard.forms import CityForm
from dashboard.models import City
from dashboard.helper import get_weather_data

# Create your views here.
def home(request):
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        name = form.cleaned_data.get('name')
        weather_data = get_weather_data(name)

    elif request.method == 'GET':
        try:
            name = City.objects.latest('date_added').name
            weather_data = get_weather_data(name)
        except Exception as e:
            weather_data = None
        
    context={'form': form, 'weather_data': weather_data}
    return render(request, 'home.html', context)


def history(request):
    cities = City.objects.all().order_by('-date_added')[:5]

    weather_data_list = []
    for city in cities:
        weather_data_list.append(get_weather_data(city.name))

    return render(request, 'history.html', context={'weather_data_list': weather_data_list})
