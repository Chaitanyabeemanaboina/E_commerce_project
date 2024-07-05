from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('cat/<str:category>/',views.category),
    path('buy/<int:id>/<str:name>',views.buy),
    path('add/<int:id>/<str:name>',views.add_to_cart),
    path('red/<int:id>/<str:name>',views.reduce),
    path('bill/',views.bill),
    path('cancel/<int:id>',views.cancel),
    path('add_disp/',views.add_disp),
    path('cancel_add/<int:id>',views.cancel_add),
    path('search/',views.search),
    path('buy_bill/<int:id>',views.buy_bill),
    path('pay/',views.pay),
    path('logout/',views.custom_logout_view),
    path('api/',views.api)
]