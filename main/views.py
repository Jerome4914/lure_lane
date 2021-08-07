from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Fish, Lure, Review
import bcrypt

# Create your views here.
def index(request):
    return render(request, "reg_login.html")

def create_user(request):
    if request.method == "POST":
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hash_pw
        )
        request.session['current_users'] = new_user.id
        return redirect('/user/dashboard')
    return redirect('/')

def login_user(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['current_users'] = this_user[0].id
        return redirect('/user/dashboard')
    return redirect('/')    

def dashboard(request):
    if 'current_users' not in request.session:
        return redirect('/')
    current_users = User.objects.get(id=request.session['current_users'])
    context = {
        'current_users': User.objects.get(id=request.session['current_users']),
        # 'every_jobs': Job.objects.all(),
        # "current_user_jobs": Job.objects.filter(all_jobs=current_users.id, user_jobs=True),
        # "this_user": User.objects.filter(id=request.session['current_users']),
    }
    return render(request, 'dashboard.html', context)    

def logout_user(request):
    request.session.clear()
    return redirect('/')

def lure_form(request):
    context = {
        'current_users': User.objects.get(id=request.session['current_users']),
    }
    return render(request, "lure_form.html", context)

def create_location(request):
    if request.method == "POST":
        errors = Fish.objects.fish_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/lure/lure_form')  
    
        location = Fish.objects.create(location=request.POST['location'], all_fish = request.POST['all_fish'])
        user = User.objects.get(id=request.session['current_users'])
        return redirect(f'/lure/best_lures/{location.id}')
    return redirect('/')

def best_lures(request, id):
    
    context = {
        'current_users': User.objects.get(id=request.session['current_users']),
        'fish': Fish.objects.get(id=id),
        'one_fish': Fish.objects.get(id=1)
    }
    return render(request, "show_lure.html", context)