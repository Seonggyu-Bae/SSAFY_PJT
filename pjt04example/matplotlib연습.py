import matplotlib.pyplot as plt


plt.plot([1,2,3,4],[1,2,3,4])

#plt.clf() : 이때까지 그렸던 plot 지우기

#plt.clf()

x = [1,2,3,4]
y = [1,4,9,16]




plt.plot(x,y)
plt.title('Title')

plt.ylabel('y')
plt.xlabel('x')



#plt.show()

# 파일로 저장하기 -> show가 없어야함

plt.savefig('plot.png')