from django.db import models
import datetime
class Users(models.Model):
    username = models.CharField(primary_key = True, max_length = 20)
    password = models.CharField(max_length = 20)
    role = models.CharField(max_length = 15)
    def __str__(self):
        return '<User Name: {}, Role: {}>'.format(self.username, self.role)
    
class Customers(models.Model):
    fullname = models.CharField(max_length = 100)
    username = models.ForeignKey(Users, on_delete = models.CASCADE)
    gender = models.CharField(max_length = 6)
    dob = models.DateField()
    mobile = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    nationality = models.CharField(max_length = 12)

class Employee(models.Model):
    username = models.ForeignKey(Users, on_delete = models.CASCADE)
    fullname = models.CharField(max_length = 100)
    email = models.EmailField()
    mobile = models.IntegerField()
    branch = models.CharField(max_length = 20)
class Account(models.Model):
    account_number = models.CharField(primary_key = True, max_length = 16)
    username = models.ForeignKey(Users, on_delete = models.CASCADE)
    account_type = models.CharField(max_length = 20)
    amount = models.IntegerField()
    branch = models.CharField(max_length = 20)
    location = models.CharField(max_length = 25)
    issue_date = models.DateField(default = datetime.date.today)

class FixedDeposit(models.Model):
    account_number = models.ForeignKey(Account, on_delete = models.CASCADE)
    tenure = models.IntegerField()
    rate = models.IntegerField()

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key = True)
    account_number = models.ForeignKey(Account, on_delete = models.CASCADE)
    date = models.DateField(default = datetime.date.today)
    ttype = models.CharField(max_length = 6)
    amount = models.IntegerField()
    
    
