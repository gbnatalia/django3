#from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)
index_cnt = 0
about_cnt = 0


def index(request):
    global index_cnt
    my_index = '<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><title>Главная</title></head>\
                <body>Мой первый Django сайт</body></html>'
    index_cnt = index_cnt + 1
    logger.info(f'Число посещений  страницы "Главная" - {index_cnt}')
    return HttpResponse(my_index)


def about(request):
    global about_cnt
    my_about = '<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><title>О себе</title></head>\
                <body> Данный сайт разработан студентом GeekBrains курса Веб-разработки на Python </body></html>'
    about_cnt = about_cnt + 1
    logger.info(f'Число посещений страницы "Обо мне" - {about_cnt}')
    return HttpResponse(my_about)
