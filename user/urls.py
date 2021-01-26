from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
        path('login/', LoginView.as_view(template_name='user/login.html')),
        path('logout/', LogoutView.as_view(next_page='/user/login/')),
        path('profile/', views.profile),
        path('register/', views.register),
        path('password_change/', views.password_change),
        ]

