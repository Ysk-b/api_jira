from django.contrib import admin
from .models import Profile, Category, Task

# admin.pyに記載したモデルは、管理画面で確認できるようになる
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Task)