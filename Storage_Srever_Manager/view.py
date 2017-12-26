
#from django.http import HttpResponse
from base_models.models import *
from django.http import QueryDict

from django.shortcuts import render




def get_server(request):

    context  = {}
    server_all = Server.objects.all()
    name_list = Server.objects.distinct().values("name")
    os_list = Server.objects.distinct().values("os")
    kernel_list = Server.objects.distinct().values("kernel")
    nic_list = Server.objects.distinct().values("nic")
    owner_list = Server.objects.distinct().values("owner")
    context['hello'] = 'Hello World!'
    context['name'] = name_list
    context['server_all'] = server_all
    return render(request, 'Server.html', context)
