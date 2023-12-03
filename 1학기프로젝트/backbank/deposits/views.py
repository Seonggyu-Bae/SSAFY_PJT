from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .models import DepositOptions, DepositProducts, SavingProducts, SavingOptions
from .serializers import DepositOptionsSerializer, DepositProductSerializer, SavingProductSerializer, SavingOptionsSerializer
from django.http import JsonResponse

# Create your views here.
api_key = settings.API_KEY 




######## 예금


@api_view()
def deposit_index(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
def save_deposit_products(request):

    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    res = response['result']
    
    product = DepositProducts.objects.all()
    options = DepositOptions.objects.all()
    product.delete()
    options.delete()

    for li in res['baseList']:
        save_data = {
            'dcls_month' : li['dcls_month'],    # 공시 제출월
            'fin_prdt_cd' : li['fin_prdt_cd'],
            'kor_co_nm' : li['kor_co_nm'],  # 금융 회사 명
            'mtrt_int' : li['mtrt_int'],    # 만기 후 이자율
            'fin_prdt_nm' :  li['fin_prdt_nm'],
            'etc_note' : li['etc_note'],
            'join_deny' : li['join_deny'],
            'join_member':  li['join_member'],
            'join_way' : li['join_way'],
            'spcl_cnd' : li['spcl_cnd'],
            'max_limit' : li['max_limit'],
        }
        serializer= DepositProductSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    
    
    for li2 in res['optionList']:
        product_instance = DepositProducts.objects.get(fin_prdt_cd = li2['fin_prdt_cd'])
        save_op_data = {
            'fin_prdt_cd' :  li2['fin_prdt_cd'],
            'intr_rate_type_nm' : li2['intr_rate_type_nm'],
            'intr_rate' : li2['intr_rate'],
            'intr_rate2' : li2['intr_rate2'],
            'save_trm' : li2['save_trm'],
        }
        for key, value in save_op_data.items():
            if not value:
                save_op_data[key] = -1
        
        # DepositOptions.product = DepositProducts.objects.get(fin_prdt_cd=li2['fin_prdt_cd'])
        serializer2 = DepositOptionsSerializer(data=save_op_data)
        if serializer2.is_valid(raise_exception=True):
            serializer2.save(product=product_instance)

    return JsonResponse({'message':'depositProducts & Options Saved in DB'})


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == "GET":
        products = DepositProducts.objects.all()
        serializer = DepositProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DepositProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def deposit_product_options(request):
    options = DepositOptions.objects.all()
    # product = get_list_or_404(DepositOptions, fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(options,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)





################# 아래부터 적금






@api_view()
def saving_index(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    print(response)
    return Response(response)


@api_view(['GET'])
def save_saving_products(request):

    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    res = response['result']


    product = SavingProducts.objects.all()
    options = SavingOptions.objects.all()

    product.delete()
    options.delete()
    
    for li in res['baseList']:
        save_data = {
            'dcls_month' : li['dcls_month'],    # 공시 제출월
            'fin_prdt_cd' : li['fin_prdt_cd'],
            'kor_co_nm' : li['kor_co_nm'],  # 금융 회사 명
            'mtrt_int' : li['mtrt_int'],    # 만기 후 이자율
            'fin_prdt_nm' :  li['fin_prdt_nm'],
            'etc_note' : li['etc_note'],
            'join_deny' : li['join_deny'],
            'join_member':  li['join_member'],
            'join_way' : li['join_way'],
            'spcl_cnd' : li['spcl_cnd'],
            'max_limit' : li['max_limit'],
        }
        serializer= SavingProductSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    
    for li2 in res['optionList']:
        product_instance = SavingProducts.objects.get(fin_prdt_cd = li2['fin_prdt_cd'])
        save_op_data = {
            'fin_prdt_cd' :  li2['fin_prdt_cd'],
            'intr_rate_type_nm' : li2['intr_rate_type_nm'],
            'rsrv_type_nm' : li2['rsrv_type_nm'],
            'intr_rate' : li2['intr_rate'],
            'intr_rate2' : li2['intr_rate2'],
            'save_trm' : li2['save_trm'],
        }
        for key, value in save_op_data.items():
            if not value:
                save_op_data[key] = -1
        
        # DepositOptions.product = DepositProducts.objects.get(fin_prdt_cd=li2['fin_prdt_cd'])
        serializer2 = SavingOptionsSerializer(data=save_op_data)
        if serializer2.is_valid(raise_exception=True):
            serializer2.save(product=product_instance)

    return JsonResponse({'message':'okay'})


@api_view(['GET', 'POST'])
def saving_products(request):
    if request.method == "GET":
        products = SavingProducts.objects.all()
        serializer = SavingProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SavingProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def saving_product_options(request):
    options = SavingOptions.objects.all()
    serializer = SavingOptionsSerializer(options,many=True)
    return Response(serializer.data)




###################################
#################상품가입###########
###################################


# @api_view(['GET','POST'])
# def signup_deposit(request,option_pk,amount):
#     user=request.user
#     deposit_options_instance = DepositOptions.objects.get(pk=option_pk)
#     deposit_product_instance = deposit_options_instance.deposit_product
#     if SubscribedProduct.objects.filter(fin_prdt_cd=deposit_product_instance.fin_prdt_cd, save_trm=deposit_options_instance.save_trm):
#         return JsonResponse({'message': 'already'})

#     save_data = {
#             'type' : 'D',
#             'fin_prdt_cd': deposit_product_instance.fin_prdt_cd,
#             'kor_co_nm': deposit_product_instance.kor_co_nm,
#             'fin_prdt_nm': deposit_product_instance.fin_prdt_nm,
#             'max_limit': deposit_product_instance.max_limit,
#             'amount': amount,
#             'dcls_end_day': deposit_product_instance.dcls_end_day,
#             'intr_rate_type': deposit_options_instance.intr_rate_type,
#             'intr_rate_type_nm': deposit_options_instance.intr_rate_type_nm,
#             'save_trm': deposit_options_instance.save_trm,
#             'intr_rate': deposit_options_instance.intr_rate,
#             'intr_rate2': deposit_options_instance.intr_rate2,
#     }
#     serializer = SubscribedProductSerializer(data=save_data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=user)
#         return JsonResponse({'message': 'okay'})


# @api_view(['GET','POST'])
# def signup_saving(request,option_pk,amount):
#     user=request.user
#     saving_options_instance = SavingOptions.objects.get(pk=option_pk)
#     saving_product_instance = saving_options_instance.saving_product
#     if SubscribedProduct.objects.filter(fin_prdt_cd=saving_product_instance.fin_prdt_cd, save_trm=saving_options_instance.save_trm):
#         return JsonResponse({'message': 'already'})
    
#     save_data = {
#             'type': 'S',
#             'fin_prdt_cd': saving_product_instance.fin_prdt_cd,
#             'kor_co_nm': saving_product_instance.kor_co_nm,
#             'fin_prdt_nm': saving_product_instance.fin_prdt_nm,
#             'max_limit': saving_product_instance.max_limit,
#             'amount': amount,
#             'dcls_end_day': saving_product_instance.dcls_end_day,
#             'intr_rate_type': saving_options_instance.intr_rate_type,
#             'intr_rate_type_nm': saving_options_instance.intr_rate_type_nm,
#             'save_trm': saving_options_instance.save_trm,
#             'intr_rate': saving_options_instance.intr_rate,
#             'intr_rate2': saving_options_instance.intr_rate2,
#     }
#     serializer = SubscribedProductSerializer(data=save_data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


