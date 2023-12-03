from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import get_user_model


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username', 'email', 'nickname', 'age', 'money', 'salary', 'financial_products'  )



class CustomLoginSerializer(LoginSerializer):
    def validate(self, data):
        # 기본 validate 호출
        data = super().validate(data)

        # email로 로그인 가능하도록 변경
        email = data.get('email', None)
        if email:
            # get_user_model()은 현재 사용 중인 User 모델을 반환합니다.
            user = get_user_model().objects.filter(email=email).first()

            # user가 존재하면 해당 user를 사용하여 로그인
            if user:
                data['username'] = user.username
            else:
                # user가 존재하지 않으면 에러 처리
                raise serializers.ValidationError("User not found")

        return data