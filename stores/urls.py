from django.urls import path
from . import views

urlpatterns = [
    path('',views.PizzeriaListAPIView.as_view(),name="pizzeria_list"),
    
    path('update/<int:id>/',views.PizzeriaUpdateAPIView.as_view(),name="pizzeria_update"),
    
    path('delete/<int:id>/',views.PizzeriaDeleteAPIView.as_view(),name="pizzeria_delete"),
    
    path('<int:id>/',views.PizzeriaDetailAPIView.as_view(),
    name="pizzeria_detail"),
    
    
    path('create/',views.PizzeriaCreateAPIView.as_view(),name="pizzeria_create"),
]



