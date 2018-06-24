from django.contrib import admin
from .models import Users
from .models import Customers
from .models import Employee
from .models import Account
from .models import FixedDeposit
from .models import Transaction

admin.site.register(Users)
admin.site.register(Customers)
admin.site.register(Employee)
admin.site.register(Account)
admin.site.register(FixedDeposit)
admin.site.register(Transaction)