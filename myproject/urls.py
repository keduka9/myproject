"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 管理画面のタイトルをカスタマイズ
admin.site.site_header  = 'Todo 管理画面'
admin.site.site_title   = 'Todo 管理'
admin.site.index_title  = 'メニュー'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('', include('django.contrib.auth.urls')),      # 追加（login/logoutを自動提供）
]
