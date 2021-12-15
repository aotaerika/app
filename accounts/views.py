from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import path
import sys
sys.path.append('../')
from nlp.views import index
from nlp.views import tf_idf


# Create your views here.
