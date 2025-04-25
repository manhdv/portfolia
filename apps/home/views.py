# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render , redirect


from .models import UserProfile

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
