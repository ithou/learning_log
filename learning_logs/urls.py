

"""定义learning_logs的模式"""

from django.urls import path

from . import views

app_name = 'learning_logs'  # Django 2.0+ 必须用app_name=''定义命名空间

urlpatterns = [
    # 主页
    # 第二个实参指定了要调用的视图函数，第三个将URL模式指定为index，需要提供主页链接时，使用名称，而非编写URL
    path('', views.index, name='index'),

    # 显示所有主题的网页
    path('topics/', views.topics, name='topics'),

    # 单个主题详细信息
    path('topic/<int:topic_id>/', views.topic, name='topic'),

    # 用于添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),

    # 添加新条目的页面，这个URL模式与http://IP/new_entry/id/的URL匹配
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # 编辑条目
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),

]

