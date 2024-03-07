from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
import uuid

def upload_avatar_path(instance, filename):
    ext = filename.split('.')[-1] # 拡張子を取得
    return '/'.join(['avatars', str(instance.user_profile.id) + str(".")+str(ext)])
class Profile(models.Model):
    # Djangoの既存のUserモデルを拡張するためのモデル
    # uuidを使用してより安全なユーザー識別子を作成する
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    img = models.ImageField(upload_to=upload_avatar_path, blank=True, null=True)

    def __str__(self):
        return self.user_profile.username

class Category(models.Model):
    items = models.CharField(max_length=100)

    def __str__(self):
        return self.items

class Task(models.Model):
    STATUS = (
        ('1', '未着手'),
        ('2', '進行中'),
        ('3', '完了'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, max_length=500)
    criteria = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS, default='1')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    estimate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responsible")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task