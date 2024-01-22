from django.contrib import admin
from django.urls import path, include
from ApiAplication import views 
from django.urls import path, include # Import the views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ApiAplication.urls')), 

]