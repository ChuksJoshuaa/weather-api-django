from django.shortcuts import render
import json
import urllib.request


def weather_view(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        result = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=08ea2a56a504bfa613e99307bae687df').read()
        main = json.loads(result)

        data = {
            "description": main['weather'][0]['description'],
            "temperature": main['main']['temp'],
            "pressure": main['main']['pressure'],
            "humidity": main['main']['humidity'],
            "weather_icon": main['weather'][0]['icon'],
        }

    else:
        data = {
            "description": None,
            "temperature": None,
            "pressure": None,
            "humidity":None,
            "weather_icon": None,
        }

    context = {
        "data": data
    }
    return render(request, 'home.html', context)
