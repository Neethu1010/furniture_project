from django.urls import path
from furapp import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('add_category/', views.add_category, name="add_category"),
    path('save_Category/', views.save_Category, name="save_Category"),
    path('display_category/', views.display_category, name="display_category"),
    path('edit_category/<int:cat_id>/', views.edit_category, name="edit_category"),
    path('update_category/<int:cat_id>/', views.update_category, name="update_category"),
    path('delete_category/<int:cat_id>/', views.delete_category, name="delete_category"),
    path('addprodcut/', views.addproduct, name="addproduct"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:pro_id>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:pro_id>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:pro_id>/', views.deleteproduct, name="deleteproduct"),
    path('login_page/', views.login_page, name="login_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('contact_details/', views.contact_details, name="contact_details"),
    path('delete_contact/<int:c_id>/', views.delete_contact, name="delete_contact")

]
