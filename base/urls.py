from django.urls import path
from . import views



urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('addtasks/', views.addtasks, name='addtasks'),
    path('addactivities/', views.addactivities, name='addactivities'),
    path('edittask/<str:pk>/', views.edittask, name='edittask'),
    path('editactivities/<str:pk>/', views.editactivities, name='editactivities'),
    path('deletetasks/<str:pk>/', views.deletetasks, name='deletetasks'),
    path('home/', views.home, name='home'),
    path('setup/', views.setup, name='setup'),
    path('task/<str:pk>/', views.task, name='task'),
    
]
