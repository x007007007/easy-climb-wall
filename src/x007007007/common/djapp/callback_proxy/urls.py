from django.urls import path
from . import views


urlpatterns = [
    path("<str:postfix>/", views.CallbackAPIView.as_view(), name='user-callback-url')
]