from email import message
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# importing requests and json
import requests, json


# Note
# '''Direct Url for city'''
# URL=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=4ddad70e730b5067d87b478bfc5d7fc0'

def index(request):
    if request.POST.get('city'):
        CITY = request.POST.get('city')
        API_KEY = "4ddad70e730b5067d87b478bfc5d7fc0"
        # upadting the URL
        URL=f"http://api.openweathermap.org/geo/1.0/direct?q={CITY}&appid={API_KEY}"
        response = requests.get(URL)
        # print(response)
    
        # if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # print(data)
        if data:
    # getting the main dict block
        
            main = data[0]
            # print('----------StaRT---------------')
            # print(main)
            # print('-------------enD------------')
        # getting latitude and longitude
            lat = main['lat']
            lon = main['lon']
            # print(lat,lon)
            URL1 = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
            response1 = requests.get(URL1)
            # print(response1)
            if response1.status_code == 200:
            # getting data in the json format
                data1 = response1.json()


                City=(data1['name'])
                Lon=(data1['coord']['lon'])
                lat=(data1['coord']['lat'])
                weather=(data1['weather'][0]['main'])
                temprature=(data1['main']['temp'])
                pressure=(data1['main']['pressure'])
                humidity=(data1['main']['humidity'])

                data={'City':City,'Longitude':Lon,'Latitude':lat,'Weather':weather,'Temperature':temprature,'Pressure':pressure,'Humidity':humidity}

            return render(request, 'whether/index.html',{'data':data})
        else:
            messages.error(request,"Please Enter Correct City Name")
            return render(request,'whether/index.html')


    return render(request,'whether/index.html')
    