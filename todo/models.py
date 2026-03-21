from django.db import models
from django.contrib.auth.models import User     # 追加

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('high',    '高'),
        ('medium',  '中'),
        ('low',     '低'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )

    def __str__(self):
        return self.title
    
    