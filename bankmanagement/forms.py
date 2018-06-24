from django import forms
import datetime
from .models import Users
class LogInForm(forms.Form):
    username = forms.CharField(max_length = 20, 
    widget= forms.TextInput(attrs={'type': 'text', 'placeholder': 'Username'}))
    password = forms.CharField(max_length = 20,
    widget= forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password'}))

class AddCustomerForm(forms.Form):
    fullname = forms.CharField(max_length= 250, 
    widget= forms.TextInput(attrs={'type': 'text', 'placeholder': 'Full Name'}))
    username = forms.CharField(max_length= 20, 
    widget= forms.TextInput(attrs={'type': 'text', 'placeholder': 'Username'}))
    password = forms.CharField(max_length= 20, 
    widget= forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices = (('male','male'), ('female', 'female')))
    dob = forms.DateField(initial=datetime.date.today)
    mobile = forms.IntegerField(max_value=10, min_value=10, 
    widget= forms.TextInput(attrs={'type': 'number', 'placeholder': 'mobile'}))
    email = forms.EmailField( widget= forms.TextInput(attrs={'type': 'email', 'placeholder': 'Email'}) )
    address = forms.CharField(widget= forms.Textarea(attrs={'placeholder': 'Address'}))
    nationality = forms.CharField(max_length=12, 
    widget= forms.TextInput(attrs={'type': 'text', 'placeholder': 'Nationality'}))

class AddAccountForm(forms.Form):
    list = list(Users.objects.all())
    print(list)
    for x in list:
        if x.role == 'Bank Executive':
            list.remove(x)
    choice = []
    for x in list:
        choice.append((x.username, x.username))
    account_number = forms.CharField(max_length = 11, min_length=11, required=True,
    widget= forms.TextInput(attrs={'type': 'number', 'placeholder': 'Account Number'}))
    username = forms.ChoiceField(required = True, choices = choice)
    account_type = forms.ChoiceField(required = True, choices = (('saving','Savings Account'), ('fixed', 'Fixed deposit')))
    amount = forms.IntegerField(max_value=99999999, min_value=100)
    branch = forms.CharField(max_length = 20,
    widget= forms.TextInput(attrs={'type': 'text', 'placeholder': 'Branch'}))
    location = forms.CharField(max_length = 25,
    widget= forms.TextInput(attrs={'type': 'text', 'placeholder': 'Location'}))

class FixedDepositForm(forms.Form):
    tenure = forms.IntegerField(max_value=30, min_value = 3, widget = forms.NumberInput(attrs = {'type':'number', 'size' : '25'}))
    rate = forms.IntegerField(max_value=15, min_value = 5, widget = forms.NumberInput(attrs = {'type':'number', 'size': '25'}))

class BETransactionForm(forms.Form):
    ttypes = (('credit','Credit'), ('debit', 'Debit'))
    account_number = forms.CharField(max_length = 11, min_length=11, required=True,
    widget= forms.TextInput(attrs={'type': 'number', 'placeholder': 'Account Number'}))
    ttype = forms.ChoiceField(required = True, choices = (('credit','Credit'), ('debit', 'Debit')))
    amount = forms.IntegerField(max_value=99999999, min_value=100)

class ChangePasswordForm(forms.Form):
    oldpassword = forms.CharField(max_length = 20, 
    widget= forms.TextInput(attrs={'type': 'password', 'placeholder': 'Old Password'}))
    newpassword = forms.CharField(max_length = 20,
    widget= forms.TextInput(attrs={'type': 'password', 'placeholder': 'New Password'}))