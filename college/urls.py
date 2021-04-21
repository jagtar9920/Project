#Created by Amarjot Singh

from django.urls import path
from .import views

urlpatterns = [                
                   path('', views.index, name = 'index'),
                   path('symptoms/',views.symptoms,name='symptoms'),
                   path('prevention/',views.prevention,name='prevention'),
                   path('hospitals/',views.hospitals,name='hospitals'),
                   path('displayForm/',views.displayForm,name='display'),
                   path('BookAppointment/',views.BookAppointment,name='BookAppointment'),
                   path('showAppointment/',views.showAppointment,name='showAppointment'),
                   path('edit/<int:id>',views.edit,name='edit'),
                   path('update/<int:id>',views.update,name='update'),
                   path('delete/<int:id>',views.delete,name='delete'),
              ]
