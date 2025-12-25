from django.urls import path
from .views import home,project,page_404


urlpatterns =[
    path('',home,name='home'),
    path('page_404',page_404,name='page_404'),
    path('project/<int:pk>',project,name='project')

]