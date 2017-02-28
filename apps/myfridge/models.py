from __future__ import unicode_literals

from django.db import models
from ..login.models import User
from datetime import datetime, timedelta
import re

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class IngrManager(models.Manager):
    def validate(self, postData):
        errors = []
        if len(postData["name"]) == 0:
            errors.append("Please enter an ingredient name.")
        if len(postData["shelflife"]) == 0 or not re.search(r"^\d+$", postData["shelflife"]):
            errors.append("Please enter an integer for shelf life.")

        if len(errors) > 0:
            return {"success":False, "error_list":errors}
        else:
            if len(postData["suffix"]) == 0:
                return {"success":True, "ingred_object":Ingredient.objects.create(name=postData["name"],shelflife=postData["shelflife"],qty_suffix="x",temperature=postData["temp"])}
            else:
                return {"success":True, "ingred_object":Ingredient.objects.create(name=postData["name"],shelflife=postData["shelflife"],qty_suffix=postData["suffix"],temperature=postData["temp"])}


class Ingredient(models.Model):
    name = models.CharField(max_length=45)
    categories = models.ManyToManyField(Category, related_name="foods")
    shelflife = models.IntegerField()
    temperature = models.CharField(max_length=16)
    qty_suffix = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = IngrManager()

class InvManager(models.Manager):
    def validate(self, postData, user_id):
        errors = []
        if len(postData["addingr"]) == 0:
            errors.append("Please enter an ingredient name.")
        if len(postData["quantity"]) == 0:
            errors.append("Please enter a quantity.")
        if not re.search(r"^[-+]?\d+(\.\d+)?$", postData["quantity"]):
            errors.append("Please enter a valid decimal number quantity.")
        if len(postData["bestby"]) > 0:
            try:
                user_shelf = datetime.strptime(postData["bestby"],"%m/%d/%y")
            except ValueError:
                try:
                    user_shelf = datetime.strptime(postData["bestby"],"%m/%d/%Y")
                except ValueError:
                    errors.append("Please enter a valid best-by date.")
                    return {"success":False, "error_list":errors}
            # Valid Date Format -> check future date
            if user_shelf < datetime.now():
                errors.append("Please enter a future best-by date.")
        else:
            user_shelf = None
        if len(errors) > 0:
            return {"success":False, "error_list":errors}
        else:
            try:
                ingr = Ingredient.objects.get(name=postData["addingr"])
            except Ingredient.DoesNotExist:
                errors.append("Ingredient '{}' not found. Click <a href='myfridge/new'>here</a> to create.".format(postData["addingr"]))
                return {"success":False, "error_list":errors}
            if ingr:
                if user_shelf:
                    shelflife = user_shelf
                else:
                    shelflife = datetime.now()+timedelta(days=ingr.shelflife)
                listing = InvListing.objects.create(user_id=User.objects.get(id=user_id), ingr_id=Ingredient.objects.get(id=ingr.id), best_by=shelflife, quantity = postData["quantity"])
                return {"success":True, "inv_object":listing}
            else:
                return {"success":False, "error_list":errors}


class InvListing(models.Model):
    user_id = models.ForeignKey(User)
    ingr_id = models.ForeignKey(Ingredient)
    best_by = models.DateTimeField()
    quantity = models.DecimalField(max_digits=13, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = InvManager()
