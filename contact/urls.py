
from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [

    path('search/', views.search, name='search'),  # type: ignore
    path('', views.index, name='index'),  # type: ignore

    path('contact/<int:contact_id>/', views.contact,
         name='contact'),  # type: ignore
    path('contact/create/', views.create, name='create'),  # type: ignore

]
