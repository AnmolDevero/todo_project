from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('task/list/', views.task_list, name='task_list'),
    path('task/add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('signup/', views.signup_view, name= 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password/change', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='password_change'),
    path('password/change/done', auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'), name='passwrod_change_done'),
    path('delete_acount/',  views.delete_acount, name='delete_acount')
]

