from first_app import views 
from django.urls import path
app_name = 'first_project'
urlpatterns = [
    #path('',views.form_name_view),
#     path('',views.stdisplay,name ="stdisplay" ),
#    path('create', views.stinsert,name = "stinsert"),
#    path('edit/<int:id>',views.stuedit,name = "stedit"),
#    path('update/<int:id>',views.stupdate,name = "stupdate"),
#    path('delete/<int:id>',views.stdel,name = "stdel"),
    #path('', views.product_detail, name='product_detail'),
    path('', views.register_user),
   path('list_of_products/', views.list_of_products),
   path('product_detail/', views.product_detail, name='product_detail'),
   path('add_cart/', views.add_to_cart, name='add_cart'),
   path('create_product/', views.create_product, name='create_product'),
]