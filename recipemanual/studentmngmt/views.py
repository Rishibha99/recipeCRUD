from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser
# from django.conf import settings
from django.contrib.auth.models import User

from django.contrib import messages
# from recipemanual.settings import AUTH_USER_MODEL
# UserModel =AUTH_USER_MODEL
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def welcome(request):
    return render(request,'login.html')
    
    # return HttpResponse("<p>Hi Welcome to Student Management!</p>")

def login_page(request):
    if request.method=='POST':
        pass
    else:
        return render(request,'login.html')

def logout_page(request):
    return render(request,'login.html')


def delete_user(request,id):
    pass
def update_user(request,id):
    pass
def register(request):
    registered_users=User.objects.all()
    context={'registered_users':registered_users}
    print('registered users', registered_users)
    if request.method=='POST':
        try:
           
            print('request=>', request.POST.get('username'))
            username=request.POST.get('username')
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            phone=request.POST.get('phone')
            email=request.POST.get('email')
            user_type=request.POST.get('user_type')
            password=request.POST.get('password')
            user_profile_image=request.FILES.get('filename')
            user=User.objects.filter(username=username)
            if user.exists():
                messages.error(request,'username already taken')
            else:    
                user=User.objects.create(
                    username=username,
                first_name=firstname,
                last_name=lastname,
                phone_number=phone,
                email=email,
                user_type=user_type,
                password=password,
                user_profile_image=user_profile_image,
                )
                user.save()
                messages.success(request,'user created')
                
            return render(request,'register.html', context)
        except Exception as ex:
            messages.error(request, str(ex))
            return render(request,'register.html')

    else:
      
        return render(request, 'register.html',{registered_users:registered_users})