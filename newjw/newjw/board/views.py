from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'board/index.html',context)