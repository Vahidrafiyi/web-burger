from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('profile', ProfileView, basename='profile')

urlpatterns = [
    path('otp/', OTPView.as_view(), name="otp_view"),
    path('profilee/', ProfileApi.as_view()),
]
urlpatterns += router.urls
