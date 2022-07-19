from curses.panel import update_panels
from django.urls import path
from . import views


urlpatterns = [
    path('get_users/', views.get_all_users, name='get-users'),
    path('create_user/', views.create_user, name='create-user'),
    path('login/', views.login_user, name='login'),
    path('get_user/<int:id>/', views.get_user, name='get-user'),
    path('update_user/<int:id>', views.update_user, name='update-user')
    # path('get_accounts/<str:name>/<str:password>/', views.get_accounts, name='get-accounts')
]

