from django.urls import path
from . import views
from . views import *

app_name = 'core'

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('list/', views.employee_list, name='employee_list'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('home_page', views.home_page, name = 'home_page')
]
