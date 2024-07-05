from django.urls import path
from API import views
urlpatterns = [
    path('listapi/',views.Product_list.as_view()),
    path('createapi/',views.Product_create.as_view()),
    path('updateapi/<int:pk>',views.Product_update.as_view()),
    path('destroyapi/<int:id>',views.Product_destroy.as_view()),
    path('api-key/',views.APIKey_create.as_view())
]