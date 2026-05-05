from django.urls import path
from ind_Ap import views
urlpatterns = [
    path("chittor/",views.chittor,name ="chittor"),
    path("kadapa/",views.kadapa,name ="kadapa"),
]
