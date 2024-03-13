from django.urls import path
from frontend import views

urlpatterns=[
    path('Homepage/',views.Homepage,name="Homepage"),
    path('products_page/<catname>/',views.products_page,name="products_page"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('user_login/',views.user_login,name="user_login"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('contact_save/',views.contact_save,name="contact_save"),
    path('register_save/',views.register_save,name="register_save"),
    path('single_product/<int:proid>/',views.single_product,name="single_product"),
    path('Save_Cart/',views.Save_Cart,name="Save_Cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('checkout/',views.checkout,name="checkout"),
    path('cart_delete/<int:p_id>/',views.cart_delete,name="cart_delete"),
]