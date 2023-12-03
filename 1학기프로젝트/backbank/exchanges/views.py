from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.response import Response
import requests


# 한국 수출입 은행 URL
URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

# Create your views here.
@api_view(['GET'])
def exchanges(request):
    if request.method == 'GET':
        API_KEY = settings.KOREAEXIM_API_KEY
        # print(API_KEY)
        params = {
            'authkey' : API_KEY,
            'data': 'AP01'
        }
        response = requests.get(URL, params)
       
        data = response.json()

        return Response(data)