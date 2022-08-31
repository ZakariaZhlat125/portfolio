from dataclasses import field
from tkinter import Widget
from xml.parsers.expat import model
from django import forms
from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):

    class Meta:
            model = Post
            fields = '__all__'
            widgets = {
                'tags':forms.CheckboxSelectMultiple(),
            }
