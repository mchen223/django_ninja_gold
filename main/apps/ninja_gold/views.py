# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    try:
        request.session['bank'] += 0
    except KeyError:
        request.session['bank'] = 0
        request.session['activities'] = []
    if request.session['bank']<0:
        request.session['message'] = "Game over, man! Game over!"
    return render(request, 'ninja_gold/index.html')

def reward(request):
    activity = request.session['activities']
    time = datetime.now().strftime('%m-%d-%Y %I:%m %p')
    name = request.POST['action']
    if name == 'farm':
        reward = random.randint(10,20)
    elif name == 'cave':
        reward = random.randint(5,10)
    elif name == 'house':
        reward = random.randint(2,5)
    elif name == 'casino':
        reward = random.randint(-50,50)
    request.session['bank'] += reward
    activity.append('Earned '+ str(reward) + ' golds from the ' + str(name) + '! ' + '(' + time + ')' + '.')
    request.session['activities'] = activity
    print request.session['activities']


def process(request):
    if request.session['bank'] >= 0:
        reward(request)
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")
