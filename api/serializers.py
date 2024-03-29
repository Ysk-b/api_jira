# フロントエンドからのGETリクエストに対して、どのようなJSONの形式でレスポンスを返すか定義するファイル
# 基本的には、作成したModels1つ1つに対して、それぞれのSerializerを作成する
from .models import Profile, Category, Task
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password':{'write_only': True, 'required': True}}

    # 今回、passwordをハッシュ化して返すというカスタム処理を追加しているので、createメソッドをオーバーライドする必要がある
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user_profile', 'img')
        extra_kwargs = {'user_profile': {'read_only': True}}

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'items')

class TaskSerializer(serializers.ModelSerializer):
    category_item = serializers.ReadOnlyField(source='category.item', read_only=True)
    owner_username = serializers.ReadOnlyField(source='owner.username', read_only=True)
    responsible_username = serializers.ReadOnlyField(source='responsible.username', read_only=True)
    status_name = serializers.CharField(source='get_status_display', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'task', 'description', 'criteria', 'status', 'status_name', 'category', 'category_item',
                  'estimate','responsible','responsible_username','owner','owner_username', 'created_at','updated_at']
        extra_kwargs = {'owner': {'read_only': True}}