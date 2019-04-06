import requests as re
from bs4 import BeautifulSoup as bs
from os import makedirs
from time import sleep

makedirs(r'C:\\xkcd')
url='https://xkcd.com/'
i,j=0,0
x,a,b,z='','','',''
print('There are several thousand images to download, so please be patient')
sleep(2)
for i in range(1,10000):
    if (re.get(url+str(i))).status_code==200:
        x=re.get(url+str(i))
        a=bs(x.text,'html.parser')
        x=a.find('div',id='middleContainer')
        x=x.text
        a=x.split('\n')
        for j in a:
            if j.startswith('Image URL'):
                x=j
        b=x.split(':')
        a='https:'+b[2]
        x=re.get(a)
        open('C:\\xkcd\\'+str(i)+'.jpg','wb').write(x.content)
        print('Downloaded image '+str(i))
    else:
        print('we\'ve run out of comics to download, it\'s over. Thank you :)')
        break;

