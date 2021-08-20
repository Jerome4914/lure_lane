from django.db import models
import bcrypt, re
# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be more than 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be more than 2 characters"
        if len(postData['email']) == 0:
            errors['register_email'] = "You must enter an email"
        if not EMAIL_REGEX.match(postData['email']):
            errors['register_email'] = "Invalid email address"
        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) > 0:
            errors['register_email'] = "That email already exists"
        if len(postData['password']) < 8:
            errors['register_password'] = "Password should be at least 8 characters"
        if (postData['password']) != (postData['confirm_password']):
            errors['register_password'] = "Passwords do not match"  
        return errors

    def login_validator(self, postData):
        errors = {}
        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) != 1:
            errors['login_email'] = "User does not exist"
        elif bcrypt.checkpw(postData['password'].encode(), current_users[0]. password.encode()) != True:
            errors['login_password'] = "Email or Password do not match"
        if len(postData['email']) == 0:
            errors['login_email'] = "Email must be entered"
        # if len(postData['password']) < 8:
        #     errors['login_password'] = "Password should be at least 8 characters"
        if len(postData['password']) == 0:
            errors['login_password'] = "Password must be entered"
        return errors

class FishManager(models.Manager):
    def fish_validator(self, postData):
        errors = {}
        if len(postData['location']) == 0:
            errors['location'] = "Location must be entered"
        return errors

    def lure_fish_validator(self, postData):
        errors = {}
        if len(postData['fish_breed']) == 0:
            errors['fish_breed'] = "Type of fish must be entered"
        return errors

class LureManager(models.Manager):
    def lure_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Lure name must be more than 2 characters"
        return errors

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}
        if len(postData['comment']) < 3:
            errors["comment"] = "Comment should be at least 3 characters"
        if (postData['rating']) == "Rate this lure!":
            errors['rating'] = "Please select a rating"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    #"user_reviews"

class Fish(models.Model):
    location = models.CharField(max_length=50, null=True)
    fish_breed = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FishManager()
    #"this_lure"


class Lure(models.Model):
    name = models.CharField(max_length=50)
    this_fish = models.ManyToManyField(Fish, related_name="this_lure")
    description = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LureManager()
    #"lure_reviews"

class Review(models.Model):
    comment = models.TextField(null=True)
    rating = models.IntegerField()
    user_review = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    lure_reviewed = models.ForeignKey(Lure, related_name="lure_reviews", on_delete=models.CASCADE, null=True)
    fish_reviewed = models.ForeignKey(Fish, related_name="fish_reviews", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()