from django.urls import path
from .views import BookAPiView

urlpatterns = [
    path('', BookAPIView.as_view())
]