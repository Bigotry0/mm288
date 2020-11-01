import time
import requests
from bs4 import BeautifulSoup
import random
import os


class download(object):
    
    def __init__(self) -> None:
        self.home='http://www.mm288.com'
        self.pic_firurl_list=[]     #储存从首页获取来的套图名地址（首张图片地址）
        self.pic_url_list=[]          #储存每张图片的网页地址
        self.pic_name_list=[]         #储存依次命名后的图片名
        self.pic_name_list_tmp=[]      #储存从首页获取来的套图名
        self.pic_dl_list=[]          #储存每张图片的下载地址
        self.pic_path_list=[]       #储存每张图片的下载保存路径
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
        pass  
    
    def get_picurl(self,url):   #获取图片url
        req=requests.get(url=url,headers=self.headers)
        html=req.text
        bf=BeautifulSoup(html)
        pic_url=bf.find_all('div',id='big-pic')
        bf=BeautifulSoup(str(pic_url))
        pic_url=bf.find_all('img')
        pic_url=pic_url[0].get('src')
        self.pic_dl_list.append(pic_url)
        pass
        
    def download_pic(self,url,name,path):    #下载写入图片  
        #time.sleep(random.uniform(1,3))
        req=requests.get(url=url,headers=self.headers)
        with open(path+'\\'+name,'wb') as f:
            f.write(req.content)
        pass
    
    def get_list(self,num):    #获取最新图片列表     传入数值表示下载套图数
        i=0
        req=requests.get(self.home,headers=self.headers)
        req.encoding='utf-8'
        html=req.text
        bf=BeautifulSoup(html)
        name_url=bf.find_all('p',class_='name')
        bf=BeautifulSoup(str(name_url))
        name_url=bf.find_all('a')
        for each in name_url:
            i=i+1
            if i>num:
                break
            print(each.get('href'))
            self.pic_name_list_tmp.append(each.text)
            self.pic_firurl_list.append(each.get('href')) 
        pass
    
    def get_all_pic(self,url,name):    #获取整个套图
        path=os.getcwd()+'\\'+str(name)
        if os.path.isdir(os.getcwd()+'\\'+name)!=True:
            os.mkdir(os.getcwd()+'\\'+name)
        
        url_tmp=url
        self.pic_url_list.append(url)
        self.pic_name_list.append(name+'1')
        self.pic_path_list.append(path)
        for i in range(2,300):
            url=url_tmp
            tmp=list(url)
            tmp.insert(len(tmp)-5,'_'+str(i))
            url=''.join(tmp)
            #print(url)
            req=requests.get(url,headers=self.headers)
            html=req.text
            bf=BeautifulSoup(html)
            pic_url=bf.find_all('div',class_='big-pic')
            bf=BeautifulSoup(str(pic_url))
            pic_url=bf.find_all('a')
            if len(pic_url)==0:
                break
            a=pic_url[0].get('href')
            
            self.pic_url_list.append(url)
            self.pic_name_list.append(name+str(i))
            self.pic_path_list.append(path)
            if a[0]=='/':
                break
        pass
    


def download_new(num):      
    meinv=download()
    meinv.get_list(num)    #下载最新n套图
    
    for i in range(0,len(meinv.pic_firurl_list)):
        print(meinv.home+meinv.pic_firurl_list[i])
        meinv.get_all_pic(meinv.home+meinv.pic_firurl_list[i],meinv.pic_name_list_tmp[i])
        
    for url in meinv.pic_url_list:
        meinv.get_picurl(url)
    for i in range(0,len(meinv.pic_url_list)):
        meinv.download_pic(meinv.pic_dl_list[i],meinv.pic_name_list[i]+'.jpg',meinv.pic_path_list[i])
        
def download_ones(pic_url,name):     #下载一套图，传入   地址+名称        http://www.mm288.com/
    taotu=download()
    taotu.get_all_pic(pic_url,name)
    
    for url in taotu.pic_url_list:
        taotu.get_picurl(url)
    for i in range(0,len(taotu.pic_url_list)):
        taotu.download_pic(taotu.pic_dl_list[i],taotu.pic_name_list[i]+'.jpg',taotu.pic_path_list[i])

def download_a_pic(pic_url,name):    #下载单张图    传入图片地址+图片名     
    if os.path.isdir(os.getcwd()+'\\'+name)!=True:
        os.mkdir(os.getcwd()+'\\'+name)
    tu=download()
    tu.get_picurl(pic_url)
    tu.download_pic(tu.pic_dl_list[0],name+'.jpg',os.getcwd()+'\\'+name)    

if __name__ == "__main__":
    
    #download_new(2)
    #download_ones('http://www.mm288.com/meinv/rtys/82058.html','好色风情女郎阿朱黑丝制服惨遭锁链调教')
    #download_a_pic('http://www.mm288.com/meinv/rtys/85288_41.html','激情曼妙傲人红娘利世情趣美乳超清细节特写')
    #download_ones('http://www.mm288.com/xgmn/81722.html','风骚人妻久久手遮半乳大秀蜜汁美臀')
    download_ones('http://www.mm288.com/mvtp/dlmn/85277.html','[喵糖映画] VOL.210 《贝法红蓝礼服》 写真集')