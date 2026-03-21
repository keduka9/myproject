from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'タスクを入力',
                'class': 'border border-gray-300 rounded-lg px-3 py-2 text-sm'
                        ' forcus:outline-none focus:ring-2 focus:fing-blue-300',
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date',     # ブラウザのカレンダーUIが表示される
                'class': 'border border-gray-300 rounded-lg px-3 py-2 text-sm'
                        ' focus:outline-none focus:ring-2 focus:fing-blue-300',
            }),
            'priority': forms.Select(attrs={ # これを明示的に追加
                'classs': 'border border-gray-300 rounded-lg px-3 py-2 text-sm'
                        ' focus:outline-none focus:ring-2 focus:ring-blue-300',
            }),
        }
        labels = {
            'title':        'タスク名',
            'due_date':     '期限',
            'priority':     '優先度',
        }