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
    
    context = {
        'current_users': User.objects.get(id=request.session['current_users']),
        'lure': Lure.objects.all(),
        'review': Review.objects.filter()[:20],
        'fish': Fish.objects.all(),
    }
    return render(request, 'dashboard.html', context)    

def logout_user(request):
    request.session.clear()
    return redirect('/')

def best_lure_form(request): 
    if 'current_users' not in request.session:
        messages.error(request, "Please register or log in first")
        return redirect('/')
    context = {
        'current_users': User.objects.get(id=request.session['current_users']),
        'all_fish': Fish.objects.filter(id__in=[12, 13, 14, 15, 16, 17, 18, 19]),
    }
    return render(request, "best_lure_form.html", context)

# def create_location(request):   
#     if request.method == "POST":
#         errors = Fish.objects.fish_validator(request.POST)
#         if len(errors) > 0:
#             for key, value in errors.items():
#                 messages.error(request, value, extra_tags=key)
#             return redirect('/lure/best_lure_form') 
        
#         location = Fish.objects.create(location=request.POST['location'])
#         user = User.objects.get(id=request.session['current_users'])
        
#         return redirect(f'/lure/best_lures/{location.id}')
#     return redirect('/')

def best_lures(request):
    errors = Fish.objects.fish_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/lure/best_lure_form')
    
    fish= Fish.objects.get(id=request.POST['this_fish'])
    context = {
        'fish': Fish.objects.get(id=request.POST['this_fish']),
        'current_users': User.objects.get(id=request.session['current_users']),
        "location":request.POST['location'],
        "all_lures": Lure.objects.filter(this_fish__fish_breed=fish.fish_breed),
        
    }
    return render(request, "show_lure.html", context)

def lure_form(request):
    if 'current_users' not in request.session:
        messages.error(request, "Please register or log in first")
        return redirect('/')
    context = {
        'current_users': User.objects.get(id=request.session['current_users']),
    }
    return render(request, "add_lure.html", context)

def create_lure(request):
    if request.method == "POST":
        lure_errors = Lure.objects.lure_validator(request.POST)
        fish_errors = Fish.objects.lure_fish_validator(request.POST)
        review_errors = Review.objects.review_validator(request.POST)
        errors = list(lure_errors.values())+list(fish_errors.values())+list(review_errors.values())
        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
            return redirect('/lure/lure_form')
        this_fish = Fish.objects.create(fish_breed=request.POST['fish_breed'])

        user = User.objects.get(id=request.session['current_users'])
        lure = Lure.objects.create(name=request.POST['name'])
        review = Review.objects.create(comment=request.POST['comment'], rating=int(request.POST['rating']), user_review=user, lure_reviewed=lure, fish_reviewed=this_fish )
        return redirect('/user/dashboard')
    return redirect('/')

def delete_review(request, review_id):
    if 'current_users' not in request.session:
        messages.error(request, "Please register or log in first!")
        return redirect('/')
    review = Review.objects.get(id=review_id)
    review.delete()
    return redirect('/user/dashboard')

def lure_edit(request, review_id):
    
        
    if request.method == "POST":
        review = Review.objects.get(id=review_id)
        # errors = Review.objects.review_validator(request.POST)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request, value, extra_tags=key)
        #     return redirect(f'/lure/{review.id}/edit_form')      
        # if request.POST['comment'] == request.POST['comment']:
        #     if request.POST['rating'] == request.POST['rating']:
        #         return redirect('/user/dashboard')
        errors = Review.objects.review_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect(f'/lure/{review.id}/edit_form')         
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        review.rating = request.POST['rating']
        review.save()
        return redirect('/user/dashboard')
    return redirect(f'/lure/{review.id}/edit_form') 

def edit_form(request, review_id):
    if 'current_users' not in request.session:
        messeges.error(request, "Please register or log in first")
        return redirect('/')
    
    review = Review.objects.get(id=review_id)
    context = {
        'current_users': User.objects.get(id=request.session['current_users']),
        'review': Review.objects.get(id=review_id),
    }
    return render(request, "one_lure.html", context)