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

import requests
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from .models import Stock, UserProfile
from decimal import Decimal, InvalidOperation

from datetime import datetime


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
    stocks = Stock.objects.filter(user=user).order_by('code')
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
        code = request.POST.get("code")
        exchange = request.POST.get("exchange")
        print("DEBUG: exchange =" + exchange)
        name = request.POST.get("name")
        type = request.POST.get("type")
        country = request.POST.get("country") 
        description = request.POST.get("description", "")
        currency = request.POST.get("currency")
        isin = request.POST.get("isin")
        close_str = request.POST.get("close", "")
        try:
            close = Decimal(close_str)
        except (InvalidOperation, TypeError):
            close = 0  # default

        date_str = request.POST.get("date", "")
        print("DEBUG: date_str =" + date_str)

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()  # Đảm bảo đúng định dạng ngày
        except ValueError:
            date = datetime.today()  # Nếu không thể chuyển đổi thì gán None, có thể set giá trị mặc định ở DB
        
        try:
            Stock.objects.create(
                user=request.user,
                code=code,
                exchange=exchange,
                name=name,
                type=type,
                description=description,
                country=country,
                currency=currency,
                isin=isin,
                close=close,
                date=date
                )
        except Exception as e:
            print("CREATE ERROR:", e)
            return redirect("securities")
    return redirect("securities")  # hoặc tên url của trang list

@login_required(login_url="/login/")
def edit_stock(request):
    if request.method == "POST":
        stock_id = request.POST.get("stock_id")
        stock = get_object_or_404(Stock, id=stock_id, user=request.user)

        stock.code = request.POST.get("code")
        stock.name = request.POST.get("name")
        stock.description = request.POST.get("description", "")
        stock.save()

    return redirect("securities")

@login_required(login_url="/login/")
def user_profile_view(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        profile.address = request.POST.get('address', '')
        profile.city = request.POST.get('city', '')
        profile.country = request.POST.get('country', '')
        profile.postal_code = request.POST.get('postal_code', '')
        profile.about_me = request.POST.get('about_me', '')
        profile.finhub_api_key = request.POST.get('finhub_api_key', '')
        profile.alpha_vantage_api_key = request.POST.get('alpha_vantage_api_key', '')
        profile.eodhd_api_key = request.POST.get('eodhd_api_key', '')
        profile.yahoo_finance_api_key = request.POST.get('yahoo_finance_api_key', '')
        profile.google_map_api_key = request.POST.get('google_map_api_key', '')
        profile.save()

        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()

        return redirect('user')  # hoặc bất kỳ route nào bạn đặt tên


    context = {
        "user": user,
        "profile": profile
    }
    print("DEBUG: user_profile_view called")
    return render(request, "home/user.html", context)

@require_GET
def search_stock_api(request):
    query = request.GET.get("q", "")
    if not query:
        return JsonResponse([], safe=False)

    url = f"https://eodhd.com/api/search/{query}?api_token=67c9ca27830eb1.54218837&fmt=json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        return JsonResponse([], safe=False)

    # Lọc dữ liệu cần thiết
    results = []
    for item in data:
        results.append({
            "code": item.get("Code"),
            "exchange": item.get("Exchange"),
            "name": item.get("Name"),
            "type": item.get("Type"),
            "country": item.get("Country"),
            "currency": item.get("Currency"),
            "isin": item.get("ISIN"),
            "close": item.get("previousClose"),
            "date": item.get("previousCloseDate"),
        })

    return JsonResponse(results, safe=False)