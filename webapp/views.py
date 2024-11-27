import razorpay
from django.shortcuts import render,redirect
from furapp.models import Product_Db,Category_Db
from webapp.models import ContactDb,RegisterDb,CardDb,orderDb
from django.contrib import messages

# Create your views here.     
def  homepage(req):
    categories=Category_Db.objects.all()
    cart=CardDb.objects.filter( Username=req.session['Username']).count()

    return render(req,"Home.html",{'categories':categories,'cart':cart})
def product_page(req):
    products=Product_Db.objects.all()
    cart = CardDb.objects.filter(Username=req.session['Username']).count()
    return render(req,"products.html",{'products':products,'cart':cart})
def about_page(req):
    cart = CardDb.objects.filter(Username=req.session['Username']).count()
    return render(req,"About.html",{'cart':cart})
def contact_page(req):
    cart = CardDb.objects.filter(Username=req.session['Username']).count()
    return render(req,"contact.html",{'cart':cart})
def service_page(req):
    cart = CardDb.objects.filter(Username=req.session['Username']).count()
    return render(req,"services.html",{'cart':cart})
def save_contact(req):
    if req.method=="POST":
        name=req.POST.get('name')
        mob=req.POST.get('mobile')
        email=req.POST.get('email')
        msg=req.POST.get('message')
        obj=ContactDb(Name=name,Mobile=mob,Email=email,Message=msg)
        obj.save()
        messages.success(req, "sign in successfully..!")
        return redirect(contact_page)
def  products_filtered(req,cat_name):
    data=Product_Db.objects.filter(Category=cat_name)
    return render(req,"products_filtered.html",{'data':data})
def single_product(req,pro_id):
    data=Product_Db.objects.get(id=pro_id)
    return render(req,"single_product.html",{'data':data})
def  sign_in(req):
    return render(req,"signin.html")

def  sign_up(req):
    return render(req,"signup.html")
def save_user(req):
  if req.method == "POST":
    na=req.POST.get('uname')
    em=req.POST.get('email')
    p1=req.POST.get('pass')
    p2=req.POST.get('re_pass')
    mob=req.POST.get('mobile')
    obj=RegisterDb(Username=na,Email=em,Password=p1,ConfirmPassword=p2,Mobile=mob)
    if RegisterDb.objects.filter(Username=na).exists():
        messages.warning(req,"User already exists..!")
        return redirect(sign_up)
    elif RegisterDb.objects.filter(Email=em).exists():
         messages.warning(req, "Email address already exists..!")
         return redirect(sign_up)
    obj.save()
    return redirect(sign_in)
def UserLogin(req):
    if req.method=="POST":
        un=req.POST.get('uname')
        pwd=req.POST.get('password')
        if RegisterDb.objects.filter(Username=un,Password=pwd).exists():
            req.session['Username']=un
            req.session['Password']=pwd
            messages.success(req,"welcome..!")
            return redirect(homepage)
        else:
            messages.error(req, "Please check your password...!")
            return redirect(sign_in)
    else:
        messages.warning(req, "invalid username...!")
        return redirect(sign_in)

def userLogout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "successfully logout..!")
    return redirect(sign_in)
def save_cart(req):
 if req.method == "POST":
    na=req.POST.get('uname')
    pri=req.POST.get('price')
    pn=req.POST.get('pname')
    tt=req.POST.get('total')
    qn=req.POST.get('quan')
    try:
        x=Product_Db.objects.get(Product_name=pn)
        img=x.Product_Image1
    except Product_Db.DoesNotExist:
        img=None

    obj=CardDb(Username=na,Price=pri,Product_name=pn,Total_price=tt,Quantity=qn,Prod_Image=img)
    obj.save()
    messages.success(req, "saved to cart..!")
    return redirect(homepage)
def cart_page(request):
    data=CardDb.objects.filter(Username=request.session['Username'])
    subtotal=0
    shipping_amount=0
    total_amount=0
    for i in data:
        subtotal= subtotal + i.Total_price
        if subtotal>50000:
            shipping_amount=100
        else:
            shipping_amount=250
        total_amount=shipping_amount+subtotal
    return render(request,"cart.html",{'data':data,'subtotal':subtotal,'shipping_amount':shipping_amount,'total_amount':total_amount}
                  )



def deleteproduct(req, cart_id):
    x=CardDb.objects.filter(id=cart_id)
    x.delete()
    messages.error(req, "product deleted....!")
    return redirect(cart_page)
def checkout_page(req):
    data = CardDb.objects.filter(Username=req.session['Username'])

    subtotal=0
    shipping_amount=0
    total_amount=0
    for i in data:
        subtotal= subtotal + i.Total_price
        if subtotal>50000:
            shipping_amount=100
        else:
            shipping_amount=250
        total_amount=shipping_amount+subtotal
    return render(req, "checkout.html", {'data': data,'subtotal':subtotal,'shipping_amount':shipping_amount,'total_amount':total_amount})


def save_checkout(req):
    if req.method == "POST":
        na = req.POST.get('c_fname')
        pri = req.POST.get('total')
        plc = req.POST.get('place')
        add= req.POST.get('c_address')
        ms = req.POST.get('c_order_notes')
        mb=req.POST.get('c_phone')
        em=req.POST.get('c_email_address')

        obj = orderDb(Username=na, Total_price=pri, Message=ms, Mobile=mb, Email=em,Address=add,Place=plc)
        obj.save()
        return redirect(payment_page)

def payment_page(req):
    #retrieve the data from oderdb with the specified id
    customer=orderDb.objects.order_by('-id').first()

    #get the payment amount of the specified customer
    payy=customer.Total_price

    # convert the amount into paisa(smallest currency unit)
    amount=int(payy*100)    #assuming the payment amount in rupees

    payy_str=str(amount)

    for i in payy_str:
        print(i)
    if req.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_EhR5teqxNvqOIe','jlQBOT4F4aXLepvzkYELSgcr'))
        payment=client.order.create({'amount':amount,'currency':order_currency})

    return render(req,"payment.html",{'customer':customer, 'payy_str':payy_str})
def blog_page(req):
    return render(req,"blog.html")