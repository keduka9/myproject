from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Task

# 既存のUserAdminを拡張
admin.site.unregister(User)     # 一度解除

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # 一覧にタスク数を表示するカラムを追加
    list_display = ('username', 'email', 'is_staff', 'task_count')

    def task_count(self, obj):
        return obj.task_set.count()
    
    task_count.short_description = 'タスク数'

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # 一覧画面に表示するカラム
    list_display = ('title', 'user', 'priority', 'due_date', 'done')

    # 右側にフィルターパネルを表示
    list_filter = ('priority', 'done', 'user')

    # 上部に検索バーを表示
    search_fields = ('title', 'user__username')

    # 一覧画面から直接 done を編集できるようにする
    list_editable = ('done',)

    # デフォルトの並び順（期限が近い順）
    ordering = ('due_date',)

    # 詳細画面のレイアウト
    fieldsets = (
        ('基本情報', {
            'fields': ('user', 'title')
        }),
        ('詳細設定', {
            'fields': ('priority', 'due_date', 'done')
        }),
    )