from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path("logout/", views.logout_user, name="logout"),
    path("viewbill/", views.view_bill, name="viewbill"),
    path("newbill/", views.new_bill, name="newbill"),
    path("viewbillform/<int:pk>", views.view_billform, name="viewbillform"),
    path("viewproduct/", views.view_product, name="viewproduct"),
    path("newproduct/", views.new_product, name="newproduct"),
    path("viewproductcat/", views.view_productcat, name="viewproductcat"),
    path("editproduct/<int:pk>", views.edit_product, name="editproduct"),
    path("deleteprod/<int:pk>", views.delete_product, name="deleteprod"),
    path("newproductcat/", views.new_productcat, name="newproductcat"),
    path("editproductcat/<int:pk>", views.edit_productcat, name="editproductcat"),
    path("deletecat/<int:pk>", views.delete_cat, name="deletecat"),
]