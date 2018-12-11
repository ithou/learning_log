from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.
"""视图函数接受请求中的信息，准备好生成网页所需的数据，再将这些数据发送给浏览器——这通常是使用定义了网页是什么模板实现的"""


def index(request):
    """学习笔记的主页"""

    """ 当URL请求与app_name/urls定义的模式匹配时，Django将调用views.py中的index()函数
    再将请求对象传递给视图函数
    """
    # 第一个实参，请求对象；第二个实参用于创建网页的模板
    return render(request, 'learning_logs/index.html')  # 注意这里是index.html（有后缀）


def topics(request):  # 第一个需要使用数据（库）的网页
    """显示所有主题的网页"""
    topics = Topic.objects.order_by('date_added')  # 查询数据——请求提供Topic对象，并对date_added排序
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """显示单个主题及其所有条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 如果不是POST请求，则创建一个新表单
        form = TopicForm()  # 创建一个TopicForm实例
    else:
        # 如果是POST提交的数据，则对数据进行处理
        form = TopicForm(request.POST)

        # 检查确定是否是有效的数据
        if form.is_valid():
            form.save()  # 若有效，则写入数据库
            return HttpResponseRedirect(reverse('learning_logs:topics'))  # 重定向至所有主题的/topics页面

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """在特定的主题中添加项目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':  # 这里我少写了method，出错了半天找不出来
        form = EntryForm()
    else:

        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)  # 不将其保存到数据库中
            new_entry.topic = topic

        new_entry.save()
        return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic  # ?

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)  # 使用既有条目编辑它
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

