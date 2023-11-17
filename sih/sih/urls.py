"""
URL configuration for sih project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
# from sih.views import home
# from sih.views import signin
# from sih.views import signup
# from sih.views import profile
# from sih.views import index
# from sih.views import project
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login_student.html', views.login_student, name='login_student'),
    path('signupstudent.html', views.signupstudent, name='signupstudent'),
    path('profile.html', views.profile, name='profile'),
    path('projectsection.html', views.projectsection, name='projectsection'),
    path('projectsdisplay.html', views.projectdisplay, name='projectdisplay'),
    path('dropdownmenu.html', views.dropdownmenu, name='dropdownmenu'),
    path('first.html', views.first, name='first'),
    path('plagiarism.html', views.plagiarism, name='plagiarism')
]
