from django.shortcuts import render
from django.views import View
from .texts_for_page import texts_for_home

class HomePage(View):
    def get(self, request):
        context = {
            'texts': texts_for_home,
        }
        return render(request, 'home.html', context)
