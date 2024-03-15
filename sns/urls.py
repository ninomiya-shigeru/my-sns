from django.urls import path
from . import views

# app_name='sns'

urlpatterns = [
    path('', views.top, name='top'),
    path('index', views.index, name='index'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('comment', views.comment, name='comment'),
    path('groups', views.groups, name='groups'),
    path('add', views.add, name='add'),
    path('join', views.join, name='join'),
    path('rjct', views.rjct, name='rjct'),
    path('creategroup', views.creategroup, name='creategroup'),
    path('post', views.post, name='post'),
    path('share/<int:share_id>', views.share, name='share'),
    path('good/<int:good_id>', views.good, name='good'),
]
