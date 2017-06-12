# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User, Paper
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    username = request.POST.get('username')  # username = request.POST['username']
    password = request.POST.get('password')
    if username == '' or username is None or password == '' or password is None:
        return render(request, 'login.html')
    else:
        try:
            user = User.objects.get(username=username, password=password)
        except:
            return HttpResponse("用户名或密码错误！")
        request.session['session_username'] = user.username
        return HttpResponseRedirect('displaypaper')


def signout(request):
    try:
        del request.session['session_username']
        return HttpResponse("退出登陆！")
    except KeyError:
        pass


def signup(request):
    number = request.POST.get('number')
    username = request.POST.get('username')
    sex = request.POST.get('sex')
    age = request.POST.get('age')
    department = request.POST.get('department')
    jobTitle = request.POST.get('jobTitle')
    password = request.POST.get('password')
    checkPassword = request.POST.get('checkPassword')
    if username == '' or password == '' or username is None or password is None:
        return render(request, 'signup.html')

    if User.objects.filter(number=number).exists():
        return HttpResponse("该工号已被注册")

    if password != checkPassword:
        return HttpResponse("两次密码不一致，请重新输入")

    if username != None and password != None and password == checkPassword:
        User.objects.create(number=number, username=username, password=password, sex=sex, age=age,
                            department=department, jobTitle=jobTitle)
        return HttpResponse("注册成功！")
    else:
        return HttpResponse("请重新输入")


def modifypassword(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    newPassword = request.POST.get('newPassword')
    if username == '' or password == '' or username is None or password is None:
        return render(request, 'modifypassword.html')

    if password == newPassword:
        return HttpResponse("新密码与旧密码一致！")

    try:
        user = User.objects.get(username=username, password=password)
    except:
        return HttpResponse("用户名或密码错误！")

    if User.objects.filter(username=username, password=password).exists():
        user = User.objects.get(username=username, password=password)
        user.password = newPassword
        user.save()
        return HttpResponse("修改成功")
    else:
        return HttpResponse("用户名或密码错误！")


def uploadpaper(request):
    try:
        user = User.objects.get(username=request.session['session_username'])
    except:
        return HttpResponse('未登录 ')
    if user.username == request.session['session_username']:
        paperTitle = request.GET.get('paperTitle')
        journalName = request.GET.get('journalName')
        papaerDate = request.GET.get('papaerDate')
        papaerAuthor = request.GET.get('papaerAuthor')
        if paperTitle == '' or paperTitle is None or papaerDate == '' or papaerDate is None:
            return render(request, 'uploadpaper.html')
        else:
            if Paper.objects.filter(paperTitle=paperTitle).exists():
                return HttpResponse("文章已存在")
            Paper.objects.create(paperTitle=paperTitle, journalName=journalName, papaerDate=papaerDate,
                                 papaerAuthor=papaerAuthor, uploadedBy=request.session['session_username'])
            return HttpResponseRedirect('displaypaper')
    else:
        return HttpResponse('未登录 ')


def displaypaper(request):
    try:
        user = User.objects.get(username=request.session['session_username'])
    except:
        return HttpResponse("未登录")
    if user.username == request.session['session_username']:
        paper = Paper.objects.filter(uploadedBy=request.session['session_username'])
        if len(paper) == 0:
            return HttpResponseRedirect('uploadpaper')
        else:
            return render(request, 'displaypaper.html',
                          {'username': request.session['session_username'], 'paperList': paper})
