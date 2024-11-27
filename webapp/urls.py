from django.urls import path
from webapp import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('product_page/',views.product_page,name="product_page"),
    path('about_page/',views.about_page,name="about_page"),
    path('service_page/',views.service_page,name="service_page"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('products_filtered/<cat_name>/',views.products_filtered,name="products_filtered"),
    path('single_product/<int:pro_id>/',views.single_product,name="single_product"),
    path('',views.sign_in,name="sign_in"),
    path('sign_up/',views.sign_up,name="sign_up"),
    path('save_user/',views.save_user,name="save_user"),
    path('UserLogin/',views.UserLogin,name="UserLogin"),
    path('userLogout/',views.userLogout,name="userLogout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('deleteproduct/<int:cart_id>/', views.deleteproduct, name='deleteproduct'),
    path('checkout_page/',views.checkout_page,name='checkout_page'),
    path('save_checkout/',views.save_checkout,name="save_checkout"),
    path('payment_page/',views.payment_page,name="payment_page"),
    path('blog_page/',views.blog_page,name="blog_page")



]
