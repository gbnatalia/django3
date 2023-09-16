from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

def hello(request):
    return HttpResponse("hello from function")

class HelloView(View):
    def get(self, request):
        return HttpResponse("hello from class")

class MounthPost(View):
    def get(self, request, year, mounth):
        text = ""
        return HttpResponse(f"Posts from {mounth}/{year}<br>{text}")
def year_post(request, year):
    text = ""
    #
    return HttpResponse(f"Posts from {year}<br>{text}")

def post_detail(request, year, mounth, slug):
   post =     {
    'year': year,
    'mounth': mounth,
    'slug': slug,
    'title': "Заголовок",
    'content': "текст статьи"
    }
   return JsonResponse(post, json_dumps_params={'enchore_ascii':False})

def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp3/my_template.html", context)

class TemplIf(TemplateView):
    template_name = "myapp3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/templ_for.html', context)

