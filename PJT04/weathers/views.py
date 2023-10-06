from django.shortcuts import render
import pandas as pd
csv_path = 'weathers/data/austin_weather.csv'
from io import BytesIO
import base64
import matplotlib.pyplot as plt
from matplotlib import dates
# Create your views here.

dataframe = pd.read_csv(csv_path)

def problem1(request):
    
    context =  {
        'df' : dataframe
    }
    
    return render(request,'weathers/problem1.html',context)

def problem2(request):

    plt.clf()
    date = pd.to_datetime(dataframe['Date'])
    highT = dataframe.TempHighF
    avgT = dataframe.TempAvgF
    lowT = dataframe.TempLowF

    plt.figure(figsize=(10,6))

    plt.plot(date,highT, label = 'High Temperature')
    plt.legend()

    plt.plot(date,avgT, label = 'Average Temperature')
    plt.legend()

    plt.plot(date,lowT, label = 'Low Temperature')
    plt.legend()
  
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    context = {
        'chart_img' : f'data:image/png;base64,{image_base64}',
    }
  
    return render(request,'weathers/problem2.html', context)

def problem3(request):
    dataframe = pd.read_csv(csv_path)
    dataframe = dataframe[['Date','TempHighF','TempAvgF','TempLowF']]
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])

    monthly_data = dataframe.groupby(dataframe['Date'].dt.to_period('M')).mean()

    # 다른 view 함수에서 plt를 이미 그린 상태에서
    # 다시 그리는 경우를 대비하여, 초기화를 진행
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data['Date'], monthly_data['TempHighF'])
    plt.plot(monthly_data['Date'], monthly_data['TempAvgF'])
    plt.plot(monthly_data['Date'], monthly_data['TempLowF'])
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.legend(('High Temperature', 'Average Temperature', 'Low Temperature'))
    
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace("\n", '')
    buffer.close()

    context = {

        'chart_img' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem3.html', context)


def problem4(request):
    data = dataframe.Events

    no, rain, thun, fog, snow = 0, 0, 0, 0, 0
   
    for x in data:
        if  x==' ':
            no += 1
        if 'Rain' in x:
            rain += 1
        if 'Thunderstorm' in x:
            thun += 1
        if 'Fog' in x:
            fog += 1
        if 'Snow' in x:
            snow += 1

    x= ['No Events','Rain','Thunderstorm','Fog','Snow']
    y= [no,rain,thun,fog,snow]

    plt.figure(figsize=(10,6))
    plt.bar(x,y)
    plt.title('Event Counts')
    plt.xlabel('Event')
    plt.ylabel('Count')
    plt.grid(True)
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    context = {
        'chart_img' : f'data:image/png;base64,{image_base64}',
    }

    return render(request,'weathers/problem4.html',context)

