from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from .scrape import get_today_data
from .news import news_title_urls
from .camera import MaskDetect
from datetime import datetime

data = get_today_data()
if data[0]['date'] != datetime.today().strftime('%Y-%m-%d'):
	data = get_today_data()

def home(request):
	context = {
		'posts': data,
		'titles_urls': news_title_urls,
	}
	return render(request, 'blog/home.html', context)

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def mask_feed(request):
	return StreamingHttpResponse(gen(MaskDetect()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def about(request):
	return HttpResponse('<h1>Blog-About</h1>')

def resources(request):
	return render(request, 'blog/resources.html') 

def vaccine(request):
	return render(request, 'blog/vaccine.html') 
