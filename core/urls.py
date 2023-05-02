from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.frontpage_view, name='frontpage'),
    path('signup/', views.signup_view, name='signup'),
    # Login/Logout Redirect URL in settings.py
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
 
# Note: Logout view doesn't render a template because it only logouts the user and redirects
#       to the specified page. But Login view class is responsible for rendering a template,
#       by default looks for 'registration/login.html'. Logout view doesn't need it but can also 
#       specify a template to override.