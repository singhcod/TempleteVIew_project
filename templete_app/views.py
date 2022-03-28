from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
#
# class HomeTempleteView(TemplateView):
#     template_name = 'home.html'



class HomeTempleteView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'singh'
        context['rall'] =1010
        print(kwargs)
        return context

