from django.shortcuts import render,redirect
from .models import Products
from .forms import Signup
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .Program_data import Ecommerce_items
from django.db import connection
from django.http import JsonResponse
# Create your views here.
def items():
    a = Ecommerce_items()
    dict = a.items()
    return dict
def users_list():
    prod = Products.objects.all()
    list =[]
    for a in prod:
        list.append(a.user)
    return list
def index1(request):
    return render(request, 'firstapp/index1.html')
@login_required
def index(request):
    user = request.user
    return render(request,'firstapp/index.html',{'user':user})
def logout(request):
    return render(request, 'firstapp/index1.html')
def api(request):
    return render(request,'firstapp/api.html')
@login_required
def category(request,category=None):
    prod = Products.objects.all()
    items_dict = items()
    try:
        with connection.cursor() as cursor:
            if len(prod) == 0:
                for key in items_dict:
                    cursor.execute(
                        'insert into firstapp_products(name,prize,quantity,category,bill,add_to_cart,image,user_id) values(%s,%s,%s,%s,%s,%s,%s,%s)',
                        params=[key, items_dict[key][0], items_dict[key][1], items_dict[key][2], items_dict[key][3],
                                items_dict[key][4], items_dict[key][5], request.user.id])
            else:
                user = users_list()
                if request.user not in user:  
                    for key in items_dict:
                        cursor.execute(
                            'insert into firstapp_products(name,prize,quantity,category,bill,add_to_cart,image,user_id) values(%s,%s,%s,%s,%s,%s,%s,%s)',
                            params=[key, items_dict[key][0], items_dict[key][1], items_dict[key][2], items_dict[key][3],
                                    items_dict[key][4], items_dict[key][5], request.user.id])
        cat = Products.objects.filter(category=category, user=request.user)
        return render(request, 'firstapp/cat.html', {'cat': cat})
    except:
        return redirect('/accounts/login')
@login_required
def buy(request,id,name):
    prod = Products.objects.get(id=id,user=request.user)
    prod.quantity = prod.quantity + 1
    prod.save()
    if name == 'cat':
        return JsonResponse({"status":"success","quantity":prod.quantity})
    value = request.session['query']
    prod = Products.objects.filter(name=value,user=request.user)
    return render(request, 'firstapp/search.html', {'prod': prod})
@login_required
def buy_bill(request,id):
    prod = Products.objects.get(id=id,user=request.user)
    if not prod.bill:
        prod.bill = True
        if prod.quantity == 0:
            prod.quantity = 1
            prod.save()
        else:
            prod.save()
    if prod.bill == True and prod.quantity == 0:
        prod.quantity = 1
        prod.save()
    return JsonResponse({"status": "success","quantity":prod.quantity})
@login_required
def add_to_cart(request,id,name):
    prod = Products.objects.get(id=id,user=request.user)
    if not prod.add_to_cart:
        prod.add_to_cart = True
    prod.save()
    if name == 'add_to_cart':
        return render(request, 'firstapp/index.html')
    return JsonResponse({"status": "success"})
@login_required
def bill(request):
    prod1 = Products.objects.filter(user=request.user)
    for i in prod1:
        if i.quantity == 0:
            i.bill = False
            i.save()
    prod = Products.objects.filter(bill=True,user=request.user)
    sum = 0
    for p in prod:
        sum = sum + (int(p.prize) * int(p.quantity))
    return render(request,'firstapp/bill.html',{'prod':prod,'sum':sum})
@login_required
def reduce(request,id,name=None):
    prod = Products.objects.get(id=id,user=request.user)
    if prod.quantity != 0:
        prod.quantity = prod.quantity - 1
        prod.save()
    if name == 'search':
        value = request.session['query']
        prod1 = Products.objects.filter(name=value,user=request.user)
        return render(request, 'firstapp/search.html', {'prod': prod1})
    return JsonResponse({"status": "success", "quantity": prod.quantity})
@login_required
def cancel(request,id):
    prod = Products.objects.get(id=id,user=request.user)
    prod.bill = False
    prod.quantity = 0
    prod.save()
    prod1 = Products.objects.filter(user=request.user)
    for i in prod1:
        if i.quantity == 0:
            i.bill = False
            i.save()
    prod = Products.objects.filter(bill=True,user=request.user)
    sum = 0
    for p in prod:
        sum = sum + (int(p.prize) * int(p.quantity))
    return JsonResponse({"status": "success","sum":sum})
@login_required
def add_disp(request):
    prod = Products.objects.filter(add_to_cart=True,user=request.user)
    return render(request, 'firstapp/add_disp.html', {'prod': prod})
@login_required
def cancel_add(request,id):
    prod = Products.objects.get(id=id,user=request.user)
    prod.add_to_cart = False
    prod.save()
    return JsonResponse({"status": "success"})
@login_required
def search(request):
    query = request.GET.get('query')
    request.session['query'] = query
    prod = Products.objects.filter(name=query,user=request.user)
    return render(request, 'firstapp/search.html', {'prod': prod})

def signup(request):
    form = Signup()
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/')
    return render(request,'firstapp/signup.html',{'form':form})
@login_required
def pay(request):
    bill = Products.objects.filter(bill=True,user=request.user)
    if len(bill) == 0:
        return redirect('/ec/bill')
    prod = Products.objects.filter(user=request.user)
    for i in prod:
        i.quantity = 0
        i.bill = False
        i.save()
    return render(request, 'firstapp/pay.html')
@login_required
def custom_logout_view(request):
    logout(request)
    return redirect('/i')

