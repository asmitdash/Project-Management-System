from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import pyrebase
config = {
  'apiKey': "AIzaSyDQRPK7_LtWi3vkhf_Bmuixk7vvplj6r_o",
  'authDomain': "loginsystem-338eb.firebaseapp.com",
  'databaseURL': "https://loginsystem-338eb-default-rtdb.firebaseio.com",
  'projectId': "loginsystem-338eb",
  'storageBucket': "loginsystem-338eb.appspot.com",
  'messagingSenderId': "356492263374",
  'appId': "1:356492263374:web:982499f256264ffbd9759f"
};


firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def home(request):
    return render(request, 'index.html')

def login_student(request):
    return render(request, 'login_student.html')

def signupstudent(request):
    return render(request, 'signupstudent.html')

def profile(request):
    return render(request, 'profile.html')

def projectdisplay(request):
    return render(request, 'projectsdisplay.html')

def projectsection(request):
    return render(request, 'projectsection.html')

def dropdownmenu(request):
    return render(request, 'dropdownmenu.html')

def first(request):
    return render(request, 'first.html')

def plagiarism(request):
    return render(request, 'plagiarism.html')


def LoginUser(request):
    #print(settings.SECRET_KEY)
    if request.user==None or request.user =="" or request.user.username=="":
        return render(request,"login_student.html")
    else:
        return HttpResponseRedirect("/mainpage")

def RegisterUser(request):
    if request.user==None:
        return render(request,"signupstudent.html")
    else:
        return HttpResponseRedirect("/mainpage")

def SaveUser(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')

        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username,email,password)
            messages.success(request,"User Created Successfully")
            return HttpResponseRedirect('/register_user')
        else:
            messages.error(request,"Email or Username Already Exist")
            return HttpResponseRedirect('/register_user')
    