from django.urls import path
from Backend import views

urlpatterns = [
     path('index_page/', views.index_page, name="index_page"),
     path('category_page/', views.category_page, name="category_page"),
     path('product_page/', views.product_page, name="product_page"),
     path('category_save/', views.category_save, name="category_save"),
     path('product_save/', views.product_save, name="product_save"),
     path('display_category/', views.display_category, name="display_category"),
     path('display_product/', views.display_product, name="display_product"),
     path('display_contact/', views.display_contact, name="display_contact"),
     path('edit_category/<int:c_id>/', views.edit_category, name="edit_category"),
     path('edit_product/<int:p_id>/', views.edit_product, name="edit_product"),
     path('update_category/<int:c_id>/', views.update_category, name="update_category"),
     path('update_product/<int:p_id>/', views.update_product, name="update_product"),
     path('delete_category/<int:c_id>/', views.delete_category, name="delete_category"),
     path('delete_product/<int:p_id>/', views.delete_product, name="delete_product"),
     path('delete_contact/<int:z_id>/', views.delete_contact, name="delete_contact"),
     path('admin_login_page/', views.admin_login_page, name="admin_login_page"),
     path('AdminLogin/', views.AdminLogin, name="AdminLogin"),
     path('AdminLogout/', views.AdminLogout, name="AdminLogout"),
]