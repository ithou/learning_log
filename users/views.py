from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """注销"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()  # 如果输入数据有效，则将用户名和密码散列值保存到数据库
            # 让用户自己登录
            authenticate_user = authenticate(username=new_user.username,
                                             password=request.POST['password1'])
            login(request, authenticate_user)

            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)