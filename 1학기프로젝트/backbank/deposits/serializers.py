from rest_framework import serializers
from .models import DepositOptions, DepositProducts, SavingOptions, SavingProducts



class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'


class DepositOptionsSerializer(serializers.ModelSerializer):
    # product = DepositProductSerializer(many=True, read_only=True)

    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)


class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'


class SavingOptionsSerializer(serializers.ModelSerializer):
    # product = DepositProductSerializer(many=True, read_only=True)

    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)







# class SubscribedProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubscribedProduct
#         fields ='__all__'
#         read_only_fields = ('user',)


# class SubscribedSavingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubscribedSaving
#         fields ='__all__'
#         read_only_fields = ('user',)