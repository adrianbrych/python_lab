import matplotlib.pyplot as plt
import imageio
import numpy as np

#Htop:
#Podczas wykonywqania tego algorymtu
#Zuzcie procsora wynosilo:100%
#pamieci :40%

picture=imageio.imread("C:/Users/adria/PycharmProjects/pythonProject/pobrane.jpg")

plt.figure(1,figsize=(15,15))
plt.imshow(picture)




R_list=[]
G_list=[]
B_list=[]
RGB_list=[]
counts_tones=[]

hight=len(picture)
width=len(picture[0])

print('Maximum RGB tones in this image {}'.format(picture.max()))
print('Minimum RGB tones in this image {}'.format(picture.min()))

print("Piksel dimension of picutre ",width," x ",hight)



for i in range(0,width):
    for j in range(0,hight):
        R_list.append(picture[j,i,0])

for i in range(0,width):
    for j in range(0,hight):
        G_list.append(picture[j,i,1])

for i in range(0,width):
    for j in range(0,hight):
        B_list.append(picture[j,i,2])


for i in range(0,len(R_list)):
    value=R_list[i]+G_list[i]+B_list[i]
    RGB_list.append(value)



for i in range(0,255):
    value=RGB_list.count(i)
    counts_tones.append(value)


tones=[]

for i in range(picture.min(),picture.max()):
    tones.append(i)

poly=np.polyfit(tones,counts_tones,5)
poly_y=np.poly1d(poly)(tones)


plt.figure(2)
plt.title("Histogram")
plt.plot(tones,counts_tones,color='b') # mozna rowniez wyswitlic diagram  slupkowy -nie polecano bo ciezko czytac histogram
plt.plot(tones,poly_y,color='r')
plt.xlabel("Odcienie")
plt.ylabel("Ilosc tonow")

plt.show()