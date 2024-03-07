# フロントエンドからのGETリクエストに対して、どのようなJSONの形式でレスポンスを返すか定義するファイル
# 基本的には、作成したModels1つ1つに対して、それぞれのSerializerを作成する
from .models import Profile, Category, Task
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'img')
        extra_kwargs = {'password': {'write_only ': True, 'required': True}}

    # 今回、passwordをハッシュ化して返すというカスタム処理を追加しているので、createメソッドをオーバーライドする必要がある
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user_profile', 'img')
        extra_kwargs = {'user_profile': {'read_only': True}}