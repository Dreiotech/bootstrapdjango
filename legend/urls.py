from django.urls import path
from legend import views

urlpatterns=[
    path('index/',views.index,name='my_index'),
    path('trainer/',views.trainer,name='my_trainer'),
    path('why/',views.why,name='my_why'),
    path('contact/',views.contact,name='my_contact')



]
