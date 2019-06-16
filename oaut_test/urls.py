from django.urls import path , include
from . import views

urlpatterns = [
    path('post_list/',views.post_list,name = 'post_list'),
    path('',views.post_list,name = 'post-list'),
    path('nextpage/',views.next_page,name = 'next_page'),
    path('new_post/',views.new_post,name = 'publish')
]
