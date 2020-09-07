import random
import csv
import codecs
import matplotlib.pyplot as plt

ans1 = []
ans2 = []
ans3 = []

def process(x):
    random.seed(x)
    plt.style.use('ggplot')

    plt.rcParams['savefig.dpi'] = 100 #图片像素
    plt.rcParams['figure.dpi'] = 100 #分辨率

    scale = 10000
    num1 = num2 = num3 = 0
    customer = []
    yogurt = []
    pos1 = []
    pos2 = []
    pos3 = []

    for i in range(0,scale):
        temp = random.randint(0,100)
        if(temp <= 38): num1 = num1 + 1
        elif(temp <= 80): num2 = num2 + 1
        else: num3 = num3 + 1
            
        customer.append(temp)
        pos1.append(float(num1)/(i+1))
        pos2.append(float(num2)/(i+1))
        pos3.append(float(num3)/(i+1))
    # print(pos1[9999])
    # with open("data.csv","w") as csvfile: 
    #     writer = csv.writer(csvfile)

    #先写入columns_name
        # writer.writerow(["num","customer","type","pos1","pos2","pos3"])
        # #写入多行用writerows
        # for i in range(0,scale):
        #     writer.writerow([i, customer[i], pos1[i], pos2[i], pos3[i]])
        # print("保存文件成功，处理结束")
    # print(len(customer))
    for i in range(0,scale):
        temp = customer[i]
        if(temp <= 38): customer[i] = "chocolate"
        elif(temp <= 80): customer[i] = "vanilla"
        else: customer[i] = "strawberry"

    # for i in customer:
    # print(pos1[len(pos1)-1])
    # print(pos2[len(pos2)-1])
    # print(pos3[len(pos3)-1])

    ans1.append(pos1[len(pos1)-1])
    ans2.append(pos2[len(pos2)-1])
    ans3.append(pos3[len(pos3)-1])

for i in range(0,200):
    process(i)

plt.figure()

plt.xlabel('Randem.seed(n)') 
plt.ylabel('Possibility') 
plt.plot(range(0,200), ans1, label="chocolate")
plt.plot(range(0,200), ans2, label="vanilla")
plt.plot(range(0,200), ans3, label="strawberry")
plt.legend()
plt.show()