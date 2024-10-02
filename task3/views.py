from django.shortcuts import render
from django.views.generic import TemplateView

def main_page(request):
    return render(request, 'main_page.html')


def shop_page(request):
    mix = 'Саморезы'
    fai = 'Гвозди'
    whir = 'Шурупы'
    htr = 'Скобы'
    context = {
        'mix': mix,
        'fai': fai,
        'whir': whir,
        'htr': htr
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
