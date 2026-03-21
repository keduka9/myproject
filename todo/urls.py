from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),    # 追加
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),    # 追加
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),    # 追加
]