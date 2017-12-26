# Create your views here.
from django.http import HttpResponse
def Server_status(request):
        return HttpResponse("Hello world ! ")
