from django.shortcuts import render

def home(request):
	import json
	import requests

	api_request = requests.get("http://api.weatherapi.com/v1/current.json?key=d1e01c1dba2a4199b46200853210304&q=Pasewalk&aqi=no")

	try:
		api = json.loads(api_request.content)
		api_t = json.loads(api_request.content)
		loc = api_t['location']['localtime']
		time = loc[10:]

	except Exception as e:
		api = "Error..."
	#
	return render(request, 'home.html',{'api': api, 'time': time})


def about(request):
	return render(request, 'about.html', {})
