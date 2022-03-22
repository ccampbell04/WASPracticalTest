from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from course.models import Course


def course(request):
    course_list = Course.objects.all()
    context_dict = {'courses': course_list}

    return render(request, 'course/course.html', context=context_dict)


def about(request):
    return render(request, 'course/about.html')
