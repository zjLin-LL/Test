from django.urls import path

from app2 import views

urlpatterns = [
    path('app2/test_get/',views.test_get),
    path('app2/test_post/', views.test_post),
]
