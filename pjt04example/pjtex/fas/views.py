from django.shortcuts import render
import matplotlib.pyplot as plt

# io : 입출력 연산을 위한 python 표준 입출력 라이브러리
from io import BytesIO
import base64
# Create your views here.

def index(request):


    x = [1,2,3,4,5]
    y = [1,4,9,16,25]
    
    # 그래프 초기화
    plt.clf()

    # plot 생성
    plt.plot(x,y)
    plt.title('Title')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)


    # 그래프 이미지를 임시로 저장할 비어있는 버퍼 생성
    buffer = BytesIO()

    # 그래프를 버퍼에 저장, 이미지 형식은 png로 생성
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    
    context = {
        # 저장된 이미지의 경로를 전달(이미지를 웹 페이지에 표시하기 위해)
        'chart_img' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'index.html', context)


import pandas as pd
csv_path = 'fas/data/austin_weather.csv'

def example(request):
    dataframe = pd.read_csv(csv_path)
    context =  {
        'dataframe' : dataframe
    }
    return render(request, 'example.html', context)