from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import UserListSerializer, UserSerializer
from .models import User
import json

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    if request.method == 'GET':
        users = get_list_or_404(User)
        serializer = UserListSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def user(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def add_product(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    existing_data = user.financial_products
    new_data = request.data['financial_products']
    print(new_data)

    if existing_data:
        # 이미 있는 경우 중복 체크
        existing_values = set(existing_data.split(','))  # 기존 데이터를 쉼표로 나눠 집합으로 만듦
        new_values = set(new_data.split(','))  # 새로운 데이터를 쉼표로 나눠 집합으로 만듦

        if not new_values.isdisjoint(existing_values):
            # 기존 데이터와 새로운 데이터에 중복된 값이 있다면 저장하지 않음
            return Response({'detail': 'Duplicate values found. No data saved.'}, status=status.HTTP_400_BAD_REQUEST)

        # 중복된 값이 없다면 데이터를 합침
        updated_data = existing_data + ',' + new_data
    else:
        updated_data = new_data
    

    user.financial_products = updated_data
    serializer = UserSerializer(user, data={'financial_products': updated_data}, partial=True)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_financial_products(request, user_id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        product_to_remove = data.get('productToRemove')

        try:
            user = User.objects.get(id=user_id)

            if user != request.user:
                return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

            products = [product.strip() for product in user.financial_products.split(',')]

            if product_to_remove in products:
                products.remove(product_to_remove)

            user.financial_products = ','.join(products)
            user.save()

            return Response({'message': 'Financial product removed successfully', 'user_id': user.id})
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)