from django.shortcuts import render
from django.views.generic import TemplateView

class all_class(TemplateView):
    template_name = 'class_template.html'


def menu_page(request):
    return render(request, 'menu.html')


def shop_page(request):
    fasteners = ['Саморезы', 'Гвозди', 'Шурупы', 'Скобы']
    context = {
        'fasteners': fasteners
    }
    return render(request, 'shop_page.html', context)


def bin_page(request):
    cont = 'Продолжить покупки'
    done = 'Оформить заказ'
    context = {
        'cont': cont,
        'done': done,

    }
    return render(request, 'bin_page.html', context)
