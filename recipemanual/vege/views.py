from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def recipe(request):
    if request.method=='POST':
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_desc=data.get('recipe_description')
        recipe_file=request.FILES.get('recipe_image')
        Recipe.objects.create(recipe_name=recipe_name,
                            recipe_description=recipe_desc,recipe_image=recipe_file)
        return redirect('/recipe/')
    recipe_list=Recipe.objects.all()
    # context={'recipes':recipe_list}
    # print('context',context)
    if request.GET.get('search'):
        recipe_list=Recipe.objects.filter(recipe_name__icontains=request.GET.get('search'))
    context={'recipes':recipe_list}
    return render(request, 'recipe.html',context)

@login_required(login_url='login')
def delete_recipe(request,id):
    print('id',id)
    querset=Recipe.objects.get(id=id)
    querset.delete()
    return redirect('/recipe/')

@login_required(login_url='login')
def update_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    if request.method=='POST':
        queryset.recipe_name=request.POST.get('recipe_name')
        queryset.recipe_description=request.POST.get('recipe_description')
        if(request.FILES.get('recipe_image')):
            print('image--->',request.FILES.get('recipe_image'))
            queryset.recipe_image=request.FILES.get('recipe_image')
        queryset.save()
        return redirect('/recipe/')
    context={'recipe':queryset}
    return render(request,"update_recipe.html",context)

def register(request):
    if request.method=='POST':
        fn=request.POST.get('firstname')
        ln=request.POST.get('lastname')
        un=request.POST.get('username')
        pw=request.POST.get('password')
        user=User.objects.filter(username=un)
        if user.exists():
            messages.error(request, "username already taken")
            return redirect('/register/')
        user=User.objects.create(
            first_name=fn,
            last_name=ln,
            username=un,
        )
        user.set_password(pw)
        user.save()
        messages.success(request, "Account created")
        return redirect('/register/')
    return render(request,'register.html') 

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            print('user exists')
            return render(request,'login.html')
          
        user=authenticate(username=username, password=password)
          
        if user is None:
            print('user is none')
            messages.error(request,'Invalid password')
            return render(request,'login.html')
        else:
            print('user')
            messages.success(request,'Login Successful!')
            login(request,user)
            return render(request,'recipe.html')
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('/login/')