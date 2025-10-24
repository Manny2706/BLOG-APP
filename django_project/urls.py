"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_project import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('about-us/', views.about_us, name='about_us'),
    path ('course/', views.course, name='course'),
    path ('course/<int:course_id>/', views.course_detail, name='course_detail'),# int:course_id captures an integer parameter from the URL
"int :course_id should be replaced with an actual course id for the course_detail view to work."
"slug :course_slug can also be used to capture string parameters from the URL.e.g. path('course/<slug:course_slug>/', views.course_detail, name='course_detail'),"
" without int or slug, the parameter will be treated as a string by default and any value can be passed."

]
