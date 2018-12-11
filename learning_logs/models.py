from django.db import models

# Create your models here.

"""模型就是一个类，包含属性和方法。models.py定义要在应用程序中管理的数据"""


class Topic(models.Model):  # Topic类继承了Model
    """用户学习的主题"""
    text = models.CharField(max_length=200)  # models.CharField存储少量数据
    date_added = models.DateTimeField(auto_now_add=True)  # 记录日期和时间的数据，auto_now_add记录当前时间

    def __str__(self):  # 如果是Python2.7，这里应该是def __unicode__()
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # 外键，关联Topic类
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:  # 不知道什么用
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."

