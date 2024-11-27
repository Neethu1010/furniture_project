from django.shortcuts import render,redirect
from furapp.models import Category_Db,Product_Db
from webapp.models import ContactDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
import datetime
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index(req):
    date=datetime.datetime.now()
    cate = Category_Db.objects.count()
    prd = Product_Db.objects.count()
    return render(req,"index.html",{
        'date': date,
        'cate': cate,
        'prd': prd
    }
)

def add_category(req):
    return render(req,"AddCategory.html")
def save_Category(request):
    if request.method=="POST":
        cat=request.POST.get('cname')
        desc= request.POST.get('desc')
        img=request.FILES['image']
        obj= Category_Db(Category_Name=cat,Description=desc, Category_Image=img)
        obj.save()
        messages.success(request,"category saved....!")
        return redirect(add_category)
def display_category(req):
    cat = Category_Db.objects.all()
    return render(req,"DisplayCategory.html",{'cat':cat})


def edit_category(req ,cat_id):
    cat=Category_Db.objects.get(id=cat_id)
    return render(req,"EditCategory.html",{'cat':cat})
def update_category(req,cat_id):
    if req.method=="POST":
        cat = req.POST.get('cname')
        desc = req.POST.get('desc')

        try:
            # Try to get the image file from the request
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            # If no new image is uploaded, keep the current image from the database
            file = Category_Db.objects.get(id=cat_id).Category_Image

        # Update the course with the new or existing data
        Category_Db.objects.filter(id=cat_id).update(
            Category_Name=cat,
            Description=desc,
            Category_Image=file,

        )
        messages.success(req, "category updated....!")

    # Redirect to the display course view (use the correct URL name here)
    return redirect('display_category')
def delete_category(req, cat_id):
    x=Category_Db.objects.filter(id=cat_id)
    x.delete()
    messages.error(req, "product deleted....!")
    return redirect(display_category)

def addproduct(req):
    return render(req,"AddProduct.html")
def saveproduct(request):
    if request.method=="POST":
        pcate=request.POST.get('pc')
        pn= request.POST.get('pname')
        quan = request.POST.get('qua')
        mrp = request.POST.get('mrp')
        desc= request.POST.get('desc')
        coun = request.POST.get('cou')
        manu= request.POST.get('man')
        img=request.FILES['img1']
        imge = request.FILES['img2']
        img3 = request.FILES['img3']
        obj= Product_Db(Category=pcate,Product_name=pn,Quantity=quan,MRP=mrp,Country=coun,Description=desc, Product_Image1=img,
                        Manufactured=manu,Product_Image2=imge,Product_Image3=img3)
        obj.save()
        messages.success(request, "product saved....!")
        return redirect(addproduct)
def displayproduct(req):
    pro= Product_Db.objects.all()
    return render(req,"DisplayProduct.html",{'pro':pro})
def editproduct(req ,pro_id):
    pro=Product_Db.objects.get(id=pro_id)
    return render(req,"EditProduct.html",{'pro':pro})
def updateproduct(request,pro_id):
    if request.method=="POST":
        pcate = request.POST.get('pc')
        pn = request.POST.get('pname')
        quan = request.POST.get('qua')
        mrp = request.POST.get('mrp')
        desc = request.POST.get('desc')
        coun = request.POST.get('cou')
        manu = request.POST.get('man')
        try:
            # Try to get the image file from the request
            im1 = request.FILES['img1']
            fs = FileSystemStorage()
            file1 = fs.save(im1.name, im1)
        except MultiValueDictKeyError:
            # If no new image is uploaded, keep the current image from the database
            file1 = Product_Db.objects.get(id=pro_id).Product_Image1
            try:
                # Try to get the image file from the request
                im2 = request.FILES['img2']
                fs = FileSystemStorage()
                file2 = fs.save(im2.name, im2)
            except MultiValueDictKeyError:
                # If no new image is uploaded, keep the current image from the database
                file2 = Product_Db.objects.get(id=pro_id).Product_Image2
            try:
                # Try to get the image file from the request
                im3 = request.FILES['img3']
                fs = FileSystemStorage()
                file3 = fs.save(im3.name, im3)
            except MultiValueDictKeyError:
                # If no new image is uploaded, keep the current image from the database
                file3 = Product_Db.objects.get(id=pro_id).Product_Image3

        Product_Db.objects.filter(id=pro_id).update(
                Category=pcate,Product_name=pn,Quantity=quan,MRP=mrp,Country=coun,Description=desc, Manufactured=manu,Product_Image2=file2,Product_Image3=file3,
                Product_Image1=file1

        )
        messages.success(request, "product updated....!")
        return redirect('displayproduct')
def deleteproduct(req, pro_id):
    x=Product_Db.objects.filter(id=pro_id)
    x.delete()
    messages.error(req, "product deleted....!")
    return redirect(displayproduct)
def login_page(req):
    return render(req,"login_page.html")
def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pswd=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pswd)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=pswd
                messages.success(request,"Welcome...!")
                return redirect(index)
            else:
                messages.error(request, "Please check your password...!")

                return redirect(login_page)
        else:
            messages.warning(request, "invalid username...!")
            return redirect(login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "successfully logout..!")
    return redirect(login_page)

def contact_details(req):
    data=ContactDb.objects.all()
    return render(req,"contact_data.html",{'data':data})
def delete_contact(req,c_id):
    x=ContactDb.objects.filter(id=c_id)
    x.delete()
    return redirect(contact_details)