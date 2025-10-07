from django.urls import path
from main.views import home_page, show_xml, show_json, show_xml_by_id, show_json_by_id, create_product, show_product, register, login_user, logout_user, edit_product, delete_product, create_product_ajax, edit_product_ajax, delete_product_ajax

app_name = 'main'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('create-product/', create_product, name='create_product'),
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('edit-product/<str:id>/', edit_product, name='edit_product'),
    path('edit-product-ajax/<str:id>/',
         edit_product_ajax, name='edit_product_ajax'),
    path('delete-product/<str:id>/', delete_product, name='delete_product'),
    path('delete-product-ajax/<str:id>/',
         delete_product_ajax, name='delete_product_ajax'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
