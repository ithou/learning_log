#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/9 0:34
# @Author: https://github.com/ithou

from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic  # 根据模型Topic创建表单
        fields = ['text']  # 字段为text
        labels = {'text': ''}  # 让Django不要为字段text生成标签


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}  # 让Django不要为字段text生成标签
        widgets = {'form': forms.Textarea(attrs={'cols': 80})}
