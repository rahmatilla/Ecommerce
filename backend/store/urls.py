from django.urls import path
from .views import ProductList, ProducDetail, CategoryList, CategoryDetail

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),
    path('product/', ProductList.as_view()),
    path('product/<int:pk>', ProducDetail.as_view())

]