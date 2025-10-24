from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.   

def home(request):
    data={
        'title':'Home Page',
        'welcome_message':'Welcome to the Home Page!'
    }
    return render(request, 'index.html', data)

def about_us(request):
    return HttpResponse("This is the About Us page.")# can pass any string here
def course(request):
    return HttpResponse("This is the Course page.")# can pass any string here
def course_detail(request, course_id):
    return HttpResponse(f"This is the detail page for course {course_id}.")
