# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Listingphotos(models.Model):
    listingphotoid = models.AutoField(primary_key=True)
    listingid = models.ForeignKey('Listings', db_column='listingid', blank=True, null=True)
    photodir = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listingphotos'


class Listings(models.Model):
    listingid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', db_column='userid', blank=True, null=True)
    isbn = models.CharField(max_length=17, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    edition = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    condition = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, null=True)
    negotiable = models.NullBooleanField()
    postdate = models.DateField(blank=True, null=True)
    expirationdate = models.DateField(blank=True, null=True)
    longitute = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listings'

		
class Reviews(models.Model):
    reviewid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', db_column='userid', blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    body = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    phonenum = models.CharField(max_length=10, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    photodir = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    transactioncount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
