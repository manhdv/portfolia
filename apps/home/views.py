# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render , redirect, get_object_or_404


from .models import Stock


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
@login_required(login_url="/login/")
def securities_view(request):
    user = request.user
    stocks = Stock.objects.filter(user=user).order_by('ticker')
    paginator = Paginator(stocks, 10)  # 10 stocks mỗi page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print("DEBUG: securities_view called")
    return render(request, 'home/securities.html', {
        'page_obj': page_obj
    })

@login_required(login_url="/login/")
def add_stock(request):
    if request.method == "POST":
        ticker = request.POST.get("ticker")
        name = request.POST.get("name")
        description = request.POST.get("description", "")
        Stock.objects.create(user=request.user,ticker=ticker, name=name, description=description)
    return redirect("securities")  # hoặc tên url của trang list

@login_required(login_url="/login/")
def edit_stock(request):
    if request.method == "POST":
        stock_id = request.POST.get("stock_id")
        stock = get_object_or_404(Stock, id=stock_id, user=request.user)

        stock.ticker = request.POST.get("ticker")
        stock.name = request.POST.get("name")
        stock.description = request.POST.get("description", "")
        stock.save()

    return redirect("securities")