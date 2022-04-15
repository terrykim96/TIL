from django.http import HttpResponse
from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from .models import Vote, Comment
from .forms import VoteForm, CommentForm
import random


# Create your views here.
def index(request):
    votes = Vote.objects.order_by('title')
    context = {
        'votes': votes,
    }
    return render(request, 'polls/index.html', context)

def new(request):
    
    if request.method == 'POST':
        form = VoteForm(request.POST, request.FILES) # bound form
        if form.is_valid():                          # 유효성 검사
            form.save()                              # DB 저장
            messages.add_message(request, messages.INFO, '글이 성공적으로 작성되었습니다.')
            return redirect('polls:index')
    else:
        form = VoteForm() # unbound form
    
    context = {
        'form': form,
    }
    return render(request, 'polls/new.html', context)

def detail(request, pk):
    vote = get_object_or_404(Vote, pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.vote = vote
            comment.save()

            return redirect('polls:detail', vote.pk)
    else:
        comment_form = CommentForm()

    comments = Comment.objects.filter(vote=pk).order_by('-id')
    
    total = comments.count()
    blue = comments.filter(pick='blue').count()

    if not total:
        blue = 50
        red = 50
    else:
        blue = round((blue / total) * 100, 2)
        red = 100 - blue



    context = {
        'vote': vote,
        'comment_form': comment_form,
        'comments': comments,
        'blue' : blue,
        'red': red,
    }
    return render(request, 'polls/detail.html', context)

def random_pick(request):
    pk_lst = Vote.objects.values('id')
    ran_pk = random.choice(pk_lst)['id']

    return redirect('polls:detail', ran_pk)