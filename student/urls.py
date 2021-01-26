from django.urls import path
from student import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
        path('login/', LoginView.as_view(template_name='student/login.html')),
        path('logout/', LogoutView.as_view(next_page='/student/login/')),
        path('register/', views.register),
        path('profile/', views.profile),
        ]

