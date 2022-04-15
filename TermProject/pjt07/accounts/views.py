from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth import get_user_model
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm, CustomUserCreationForm



# Create your views here.

def index(request):
    accounts = get_user_model().objects.all()
    context = {
        'accounts': accounts,
    }
    return render(request, 'accounts/index.html', context)


def signup(request):
    """
    - GET: 회원가입 폼이 담긴 페이지 응답
    - POST: 사용자 회원정보 받아서 회원가입
    """
    if request.user.is_authenticated:
        return redirect('movies:index')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.add_message(request, messages.INFO, '가입이 완료되었습니다')
            return redirect('movies:index')

    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


def login(request):
    """
    - GET: 로그인 폼이 담긴 페이지 응답
    - POST: 사용자 로그인 받아서 인증 *authentication
    """
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.add_message(request, messages.INFO, '로그인 되었습니다')

            # 만약 쿼리스트링에 next 인자가 있으면
            # 그곳으로 보내고, 그렇지 않으면 메인으로 리다이렉트

            next_url = request.GET.get('next')

            return redirect(next_url or 'movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
@require_POST
def logout(request):
    auth_logout(request)
    messages.add_message(request, messages.INFO, '로그아웃 되었습니다')
    return redirect('movies:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, '개인정보가 수정되었습니다')
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save() # 기존세션 만료 되서 form.user로 바인딩해줘야함
            update_session_auth_hash(request, form.user)
            messages.add_message(request, messages.INFO, '비밀번호가 변경되었습니다.')
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
        messages.add_message(request, messages.INFO, '계정이 삭제되었습니다.')
    return redirect('movies:index')