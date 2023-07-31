from django.shortcuts import render

# Create your views here.
#FBV for returning String
from django.http import HttpResponse
from django.views.generic import View,TemplateView
def fbv_string(request):
    return HttpResponse('This FBV string')

#CBV for returning string as a response

class CbvString(View):
    def get(self,request):
        return HttpResponse('<h1>This is CBV string</h1>')

class Cbv_first(View):
    def get(self,request):
        return render(request,'Cbv_first.html')

class CbvTemp(TemplateView):
    template_name='temp.html'

















