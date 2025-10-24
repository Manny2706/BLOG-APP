from django.http import HttpResponse
def about_us(request):
    return HttpResponse("This is the About Us page.")# can pass any string here
def course(request):
    return HttpResponse("This is the Course page.")# can pass any string here
def course_detail(request, course_id):
    return HttpResponse(f"This is the detail page for course {course_id}.")