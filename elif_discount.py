a=float(input('enter amount'))
if a <=1000:
    dis=a*10/100
elif a >1000 and a<=5000:
    dis=a*20/100
elif a >5000 and a <=10000:
    dis=a*30/100
else:
    dis=a*50/100
totaldis=a-dis
print('pay',totaldis)