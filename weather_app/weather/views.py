from django.shortcuts import render
import json
import urllib.request
# Create your views here.

def index(request):
    if request.method == "POST":
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=48a90ac42caa09f90dcaeee4096b9e53').read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
  
        # data for variable list_of_data 
        data = { 
            "icon" : str(list_of_data['weather'][0]['icon']),
            "Location":city[0].upper()+city[1:],
            "country_code": str(list_of_data['sys']['country']),  
            "temp": str(list_of_data['main']['temp']) + 'k or '+str(int(list_of_data['main']['temp']-273))+' deg C', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
            "description": str(list_of_data['weather'][0]['description']),
        } 
        print(data) 
    else: 
        data ={} 
    return render(request, "weather/index.html", data)


