"""project_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from home.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentsignin/', studentsignin, name = 'studentsignin'),
    path('studentsignup/', studentsignup, name = 'studentsignup'),
    path('teachersignin/', teachersignin,name = 'teachersignin'),
    path('teachersignup/', teachersignup, name = 'teachersignup'),
    path('logout/', signout, name = 'logout'),
    path('', home, name = 'home'), 
    path('teacherlist/',teacherlist,name="teacherlist"),
    path('teacherview/<int:pid>/',teacherview,name='teacherview'),
    path('submit/', submit , name = 'submit'),
    path('update/<int:project_id>/',update, name = 'update'),
    path('mysubmissions/',mysubmission,name = 'mysubmission'),
    path('branch/<str:dept>',deptProjects,name="department-projects"),
    path('projects/<int:pid>',project,name="project"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
