from django.shortcuts import render
import requests
import datetime

def home(request):

    if request.method == "POST":
        city = request.POST.get("city")
    else:
        city = "New Delhi"

    url = f"http://api.weatherapi.com/v1/current.json?key=194f617a16284a068b570539260903 &q={city}"

    try:
        response = requests.get(url)
        data = response.json()

        city_name = data['location']['name']
        temp = data['current']['temp_c']
        description = data['current']['condition']['text']
        icon = data['current']['condition']['icon']

    except:
        city_name = "City not found"
        temp = "N/A"
        description = "Weather not found"
        icon = ""

    day = datetime.date.today()

    return render(request,'web/index.html',{
        'city': city_name,
        'temp': temp,
        'description': description,
        'icon': icon,
        'day': day,
        
    })