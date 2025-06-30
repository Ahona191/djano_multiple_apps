"""
URL configuration for studymart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Machine_Learning import views as ml 
from Blogs import views as blg
from Deep_Learning import views as dpl 
from Data_Analysis import views as da 
from About_Us import views as abu
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', ml.machine_learning), 
    path('dl/', ml.deep_learning), 
    path('about/',ml.about_us), 
    path('blog/',blg.blog1), 
    path('deepl/',dpl.deep_learning), 
    path('analysis/', da.data_analysis ), 
    path('aboutUS/',abu.about_us),
    
]
