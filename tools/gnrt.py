
f=open('../index.txt')
lines=f.readlines()[1:]
f.close()

arr=[]

for line in lines:
    x=line.split('\t')
    if len(x)!=5:
        continue
    arr.append((x[0],x[1]))

arr.sort(key=lambda x:x[1])

for i in range(len(arr)-1,-1,-1):
    fo=open('html/'+str(i)+'.html','w')
    if i!=0:
        fo.write('<a href='+str(i-1)+'.html>')
    fo.write('<img src="../../images/'+arr[i][0]+'" /></a>')
    fo.close()

fo=open('html/index.html','w')
fo.write('<a href='+str(len(arr)-1)+'.html>'+str(len(arr)-1)+'</a>')
fo.close()
