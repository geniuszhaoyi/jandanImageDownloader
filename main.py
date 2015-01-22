#-*- encoding: utf-8 -*-

'''
Created on 2015-1-23
@author: ZhaoYi
'''

import urllib2, urllib
import re, time, os
import uuid

#全局变量
f=0
fe=0
image = urllib.URLopener()

#获取html文本
def getHtml(url):
    html = urllib2.urlopen(url).read().decode('utf-8')
    return html

#获得网址中的文件名
def getName(url):
    i=url.rfind('/')
    return url[i+1:]

#下载图片到本地
def download(uo, url):
    path='images/'
    uo.retrieve(url, path+getName(url))

#自动生成网址
def generateURL(page):
    return 'http://jandan.net/ooxx/page-'+str(page)+'#comments'

#获得引号中的内容
def getBrackets(html, i):
    l=html[:i].rfind('"')
    r=html[i:].find('"')
    return html[l+1:i+r]

#在 s 中找到所有的 key
def findall(s, key):
    arr=[]
    while s.find(key)!=-1:
        i=s.find(key)
        arr.append(i)
        s=s[i+len(key):]
    for i in range(1, len(arr)):
        arr[i]+=arr[i-1]+len(key)
    return arr

#列出网页中所有待下载图片网址
def listImage(html):
    arr=[]
    key='.sinaimg.cn/mw'
    list=findall(html, key)
    for i in list:
        arr.append((getBrackets(html, i),i))
    return arr

#获得 oo 或 xx 的具体数值（字符串）
def getNum(phtml,key):
    k1='">'
    k2='</span>'
    i1=phtml.find(key)+len(key)
    phtml=phtml[i1:]
    l=phtml.find(k1)+len(k1)
    r=phtml.find(k2)
    return phtml[l:r]

#获得一个图片的ooxx数
def getOXs(html,i):
    k1='>oo</a>'
    k2='>xx</a>'
    html=html[i:]
    oo=getNum(html,k1)
    xx=getNum(html,k2)
    return (oo,xx)

#处理一个页面，下载所有图片并记录
def downPage(page):
    html=getHtml(generateURL(page))
    arr=listImage(html)

    print str(page)+'*'*60

    for a in arr:
        try:
            download(image, a[0])
            oxs=getOXs(html,a[1])
            f.write(getName(a[0])+'\t'+oxs[0]+'\t'+oxs[1]+'\t'+a[0]+'\t'+str(page)+'\n')
            print oxs[0]+','+oxs[1]+'\t'+a[0]
        except Exception, e:
            fe.write('Download Error:\t'+a[0]+'\n')
            print 'Download Error: '+a[0]

if __name__ == '__main__':
    f=open('index.txt','a')
    fe=open('errorlog.txt','a')
    
    for i in range(1315,1316):
        try:
            downPage(i)
        except Exception, e:
            print 'DownPage Error: '+str(i)
    f.close()
    fe.close()
