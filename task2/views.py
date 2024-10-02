from django.shortcuts import render
from django.views.generic import TemplateView


class all_class(TemplateView):
    template_name = 'class_template.html'


def all_func(request):
    return render(request, 'func_template.html')

def all_main(request):
    return render(request, 'main_template.html')
