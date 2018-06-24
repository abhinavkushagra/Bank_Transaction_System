from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LogInForm
from .models import Users
from .models import Customers
from .models import Account
from .models import Transaction
from .models import Employee
from .models import FixedDeposit
from .forms import AddCustomerForm
from .forms import AddAccountForm
from .forms import FixedDepositForm
from .forms import BETransactionForm
from .forms import ChangePasswordForm

def index(request):
    form = LogInForm()
    context = {'form' : form}
    return render(request, 'bankmanagement/index.html', context)

def beHome(request):
    return render(request, 'bankmanagement/BEHome.html')

def isLoginValid(request):
    if request.method == "POST":
        form = LogInForm(request.POST)

        if form.is_valid:
            new_user = request.POST['username']
            is_user = Users.objects.get(pk = new_user)
            if is_user != None and is_user.password == request.POST['password']:
                if is_user.role == 'Bank Executive':
                    emp = Employee.objects.get( username = new_user )
                    context = {'user': emp}
                    return render(request, 'bankmanagement/BEHome.html', context)
                else:
                    user = Users.objects.get(pk = new_user)
                    customer = Customers.objects.get( username = user)
                    context = {'user' : customer}
                    return render(request, 'bankmanagement/CHome.html', context)
    else:
        return redirect('index')

def addCustomer(request):
    if request.method == "POST":
        form = AddCustomerForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            role = "Customer"
            new_user = Users(username=username, password=password, role=role)
            fullname = request.POST['fullname']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            email = request.POST['email']
            address = request.POST['address']
            nationality = request.POST['nationality']
            new_user.save()
            new_customer = Customers(fullname = fullname, username = Users.objects.get(pk=new_user.username), gender = gender, dob = dob, mobile = mobile, email = email, address= address, nationality = nationality)
            new_customer.save()
            return redirect('behome')
    else:
        return redirect('examples')
def addAccount(request):
    if request.method == "POST":
        form = AddAccountForm(request.POST)
        if form.is_valid:
            account_number = request.POST['account_number']
            username = Users.objects.get(pk = request.POST['username'])
            account_type = request.POST['account_type']
            amount = request.POST['amount']
            branch = request.POST['branch']
            location = request.POST['location']
            new_account = Account(account_number = account_number,username = username, account_type = account_type,amount = amount,branch = branch,location = location)
            new_account.save()
            
            if account_type == 'fixed':
                context = {'account_number' : account_number}
                return redirect('another_page', account_number)
            else:
                return redirect('behome')
        else:
            return redirect('behome')
    else:
        return redirect('behome')

def page(request):
    form = AddAccountForm()
    context = {'form' : form}
    return render(request, 'bankmanagement/page.html', context)

def anotherpage(request, account_number):
    form = FixedDepositForm()
    context = {'form' : form}
    context['account_number'] = account_number
    return render(request, 'bankmanagement/another_page.html', context)

def examples(request):
    form = AddCustomerForm()
    context = {'form' : form}
    return render(request, 'bankmanagement/examples.html', context)

def contact(request):
    form = BETransactionForm()
    context = {'form' : form}
    return render(request, 'bankmanagement/contact.html', context)

def addfixeddeposit(request):
    if request.method == "POST":
        var = request.GET.get('account_number')
        print(var)
        form = FixedDepositForm(request.POST)
        if form.is_valid:
            acc = Account.objects.get(pk = var)
            tenure = request.POST['tenure']
            rate = request.POST['rate']
            new_fixed = FixedDeposit(account_number = acc, tenure = tenure, rate = rate)
            new_fixed.save()
            return redirect('behome')
    return redirect('behome')

def transaction(request):
    if request.method == "POST":
        form = BETransactionForm(request.POST)
        if form.is_valid:
            acc = Account.objects.get(pk = request.POST['account_number'])
            ttype = request.POST['ttype']
            amount = request.POST['amount']
            if acc.account_type == 'saving':
                if ttype == 'credit':
                    acc.amount += int(amount)
                else:
                    acc.amount += int(amount)
                acc.save()
                new_transaction = Transaction(account_number = acc, ttype = ttype, amount = amount)
                new_transaction.save()
                return redirect('behome')
    return redirect('contact')

def cHome(request):
    context = {'user' : request.GET.get('customer')}
    return render(request, 'bankmanagement/CHome.html', context)

def clickPass(request):
    form = ChangePasswordForm()
    context = {'form' : form}
    context['username'] = request.GET.get('username')
    return render(request, 'bankmanagement/change_pass.html', context)

def changePass(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid:
            username = request.GET.get('username')
            password = request.POST['newpassword']
            user = User.objects.get(pk = username)
            user['password'] = password
            user.save()
            return redirect('chome')

def clickTransferMoney(request):
   # form = TransferMoneyForm()
    #context = {'form' : form}
    #context['username'] = request.GET.get('username')
    return render(request, 'bankmanagement/transfer_money.html', context)

def clickTransactions(request):
    return render(request, 'bankmanagement/transactions.html', context)

def clickAccountInfo(request):
    return render(request, 'bankmanagement/account_info.html', context)




