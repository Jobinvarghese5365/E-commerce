from django.shortcuts import render,redirect
from Backend.models import productdb,categorydb
from frontend.models import contactdb,registerdb,cartdb
from django.contrib import messages

# Create your views here.
def Homepage(request):
    pro = productdb.objects.all()
    cat = categorydb.objects.all()
    return render(request,"homepage.html",{'pro':pro,'cat':cat})
def products_page(request,catname):
    pro = productdb.objects.filter(Category_name=catname)
    return render(request,"products.html",{'pro':pro})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def single_product(request,proid):
    pro = productdb.objects.get(id=proid)
    return render(request,"singleproduct.html",{'pro':pro})
def contact_save(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        obj = contactdb(contact_name=nam,contact_email=em,contact_subject=sub,contact_message=msg)
        obj.save()
        return redirect(contact)
def register_save(request):
    if request.method == "POST":
        na = request.POST.get('reg_name')
        em = request.POST.get('reg_email')
        pas = request.POST.get('reg_password')
        obj = registerdb(name=na,email_id=em,password=pas)
        obj.save()
        return redirect(user_login)
def user_login(request):
    return render(request,"login.html")

def userlogin(request):
    if request.method == "POST":
        un = request.POST.get('un_name')
        pwd = request.POST.get('un_password')
        if registerdb.objects.filter(name=un,password=pwd).exists():
            messages.success(request, "welcome")
            request.session['name']=un
            request.session['password']=pwd
            return redirect(Homepage)
        else:
            messages.error(request, "invalid username or password")
            return redirect(user_login)
    else:
        messages.error(request, "invalid username or password")
        return redirect(user_login)

def user_logout(request):
    del request.session['name']
    del request.session['password']
    return redirect(user_login)

def Save_Cart(request):
    a = request.POST.get('uname')
    p = request.POST.get('proname')
    b = request.POST.get('quantity')
    c = request.POST.get('price')
    d =request.POST.get('totalprice')
    obj = cartdb(Username=a,Productname=p,Quantity=b,Price=c,TotalPrice=d)
    obj.save()
    messages.success(request,"added to cart...!")
    return redirect(Homepage)

def cart_page(request):
    data = cartdb.objects.filter(Username=request.session['name'])
    total_price=0
    for i in data:
        total_price=total_price+i.TotalPrice
    return render(request,"cart.html",{'data':data,'total_price':total_price})
def cart_delete(request,p_id):
    x = cartdb.objects.filter(id=p_id)
    x.delete()
    return redirect(cart_page)

def checkout(request):
    data = cartdb.objects.filter(Username=request.session['name'])
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    return render(request,"checkout.html",{'data':data,'total_price':total_price})