
from django.shortcuts import render
from first_app.models import Product,Cart
from first_app.forms import ProductForm,RegisterForm
# from django.http import HttpResponse
# from first_app.models import crud_student
# from django.contrib import messages
# from first_app.forms import stform
# import pdb
# #from . import forms 
# # Create your views here.
# def stdisplay(request):
#     result = crud_student.objects.all()
#     return render (request,"index.html",{"crud_student":result})
# def stinsert(request):
#     if request.method == "POST":
#         if request.POST.get('name') and request.POST.get('email') and request.POST.get('address') and request.POST.get('mobile_no') and request.POST.get('gender'):
#             savest = crud_student()
#             savest.name = request.POST.get('name')
#             savest.email = request.POST.get('email')
#             savest.address = request.POST.get('address')
#             savest.mobile_no = request.POST.get('mobile_no')
#             savest.gender = request.POST.get('gender')
#             savest.save()
#             pdb.set_trace()
#             messages.success(request, "the record  "+ savest.name + " is saved successfully!!")
#             return render(request,"create.html")
#     else:
#          return render(request,"create.html")
        
# def stuedit(request,id):
#     get_student_details = crud_student.objects.get(id = id)
#     return render(request,'edit.html',{'crud_student':get_student_details})



# def stupdate(request,id):
#     stupdate = crud_student.objects.get(id = id)
#     form = stform(request.POST,instance = stupdate)
#     if form.is_valid():
#         form.save()
#         import ipdb;
#         pdb.set_trace()
#         messages.success(request,"the student record is updated successfully")
#         return render(request,'edit.html',{'crud_student':stupdate})
# def stdel(request,id):
#     delstudent = crud_student.objects.get(id = id)
#     delstudent.delete()
#     results = crud_student.objects.all()
#     return render(request,"index.html",{"crud_student":results})

def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
    return render(request, 'register.html',{'form':form})



def create_product(request):
    product  = ProductForm()
    if request.method  == 'POST':
        product  = ProductForm(request.POST)
        if product.is_valid():
            product.save()
    return render(request, 'product_create.html',{'form':product})

def list_of_products(request):
    if request.method  == 'GET':
        products = Product.objects.all()
    return render(request, 'product_list.html', {'products':products})

def add_product(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            product.save()
    return render(request,'add_product.html', {'form': form})

def product_detail(request):
    prod = Product.objects.all()
    return render(request,'details.html',{'prod':prod})

def add_to_cart(request,**kwargs):
    
    if id := kwargs.get('id'):
        products = Product.objects.get(id = id)
        context['data']=data

    context = {}   
    return render(request,'cart.html',context)
