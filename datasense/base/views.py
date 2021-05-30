from django.shortcuts import render
from .models import DataInfo
from django.utils import timezone


# Create your views here.

def data_list(request):
    datas = DataInfo.objects.all()
    return render(request, 'base/data_list.html', {'datas': datas})

def add_data(request):
    return render(request, 'base/add_data.html')
