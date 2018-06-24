from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('isvalid/', views.isLoginValid, name='isvalid'),
    path('BEHome/', views.beHome, name='behome'),
    path('contact/', views.contact, name='contact'),
    path('examples/', views.examples, name='examples'),
    path('page/', views.page, name='page'),
    path(r'^another_page/(?P<account_number>[0-9]+)/$', views.anotherpage, name='another_page'),
    path('add_customer/', views.addCustomer, name='addcustomer'),
    path('add_account/', views.addAccount, name='addaccount'),
    path('addfixeddeposit/', views.addfixeddeposit, name='addfixeddeposit'),
    path('transaction/', views.transaction, name = 'transaction'),
    path('CHome/', views.cHome, name='chome'),
    path('ClickPass/', views.clickPass, name='clickpass'),
    path('ChangePassword/', views.changePass, name='changepass'),
    path('ClickTransferMoney/', views.clickTransferMoney, name='clicktransfermoney'),
    #path('TransferMoney/', views.transferMoney, name ='transfermoney'),
    path('ClickTransactions/', views.clickTransactions, name='clicktransactions'),
    #path('Transactions/', views.transactions, name='transactions'),
    path('clickAccountInfo/', views.clickAccountInfo, name='clickaccountinfo'),
    #path('AccountInfo/', views.accountInfo, name='accountinfo'),
]