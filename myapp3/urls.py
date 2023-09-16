from django.urls import path
from .views import hello, HelloView
from .views import year_post, MounthPost, post_detail
from .views import my_view
from .views import TemplIf
from .views import view_for

urlpatterns = [
    path('hello/',  hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:mounth>/', MounthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:mounth>/<slug:slug>/', post_detail, name='post_detail'),
    path('', my_view, name='index'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='templ_for'),
]