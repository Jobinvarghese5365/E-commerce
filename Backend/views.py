from django.shortcuts import render,redirect
from Backend.models import categorydb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from frontend.models import contactdb
from django.contrib import messages
# Create your views here.
def index_page(request):
    return render(request,"index.html")
def category_page(request):
    return render(request,"addcategory.html")
def product_page(request):
    data = categorydb.objects.all()
    return render(request,"addproduct.html",{'data':data})
def category_save(request):
    if request.method == "POST":
        a = request.POST.get('cat_name')
        b = request.POST.get('Description')
        img = request.FILES['cat_image']
        obj = categorydb(Name=a,Description=b,Image=img)
        obj.save()
        messages.success(request,"category saved successfully")
        return redirect(category_page)
def product_save(request):
    if request.method == "POST":
        a = request.POST.get('Category_name')
        b = request.POST.get('Product_name')
        c = request.POST.get('Price')
        d = request.POST.get('Description')
        img = request.FILES['Product_image']
        obj = productdb(Category_name=a,Product_name=b,Price=c,Description=d,Product_image=img)
        obj.save()
        messages.success(request,"product saved successfully")
        return redirect(product_page)

def display_category(request):
    data = categorydb.objects.all()
    return render(request,"displaycategory.html",{'data': data})
def display_product(request):
    x = productdb.objects.all()
    return render(request,"displayproduct.html",{'x': x})

def display_contact(request):
    y = contactdb.objects.all()
    return render(request,"displaycontact.html",{'y': y})
def edit_category(request,c_id):
    category = categorydb.objects.get(id=c_id)
    return render(request,"editcategory.html",{'category':category})
def edit_product(request,p_id):
    product = productdb.objects.get(id=p_id)
    data = categorydb.objects.all()
    return render(request,"editproduct.html",{'product':product,'data': data})
def update_category(request,c_id):
    if request.method == 'POST':
        a = request.POST.get('cat_name')
        b = request.POST.get('Description')
        try:
            f = request.FILES['cat_image']
            fs = FileSystemStorage()
            file = fs.save(f.name,f)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=c_id).Image
        categorydb.objects.filter(id=c_id).update(Name=a,Description=b,Image=file)
        return redirect(display_category)

def update_product(request,p_id):
    if request.method == 'POST':
        a = request.POST.get('Category_name')
        b = request.POST.get('Product_name')
        c = request.POST.get('Price')
        d = request.POST.get('Description')
        try:
            f = request.FILES['Product_image']
            fs = FileSystemStorage()
            file = fs.save(f.name,f)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=p_id).Product_image
        productdb.objects.filter(id=p_id).update(Category_name=a,Product_name=b,Price=c,Description=d,Product_image=file)
        return redirect(display_product)

def delete_category(request,c_id):
    data = categorydb.objects.get(id=c_id)
    data.delete()
    return redirect(display_category)

def delete_product(request,p_id):
    x = productdb.objects.get(id=p_id)
    x.delete()
    return redirect(display_product)
def delete_contact(request,z_id):
    z = contactdb.objects.get(id=z_id)
    z.delete()
    return redirect(display_contact)
def admin_login_page(request):
    return render(request,"adminlogin.html")
def AdminLogin(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pwd = request.POST.get('password')

        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                messages.success(request,"welcome")
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(index_page)
            else:
                messages.error(request,"invalid username or password")
                return redirect(admin_login_page)
        else:
            messages.error(request,"invalid username or password")
            return redirect(admin_login_page)

def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)