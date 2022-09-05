from store import views
from django.urls import path,include

urlpatterns = [
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),

    path('update_item/',views.updateItem,name='update_sItem'),
    path('process_order/',views.processOrder,name='process_order'),
]
