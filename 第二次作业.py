#第一题
alist=list(map(float,input().split()))#进行列表的输入，中间以空格作为分隔符
a=len(alist)#求出列表的长度
nums=[]#创建另外一个列表用来按照从大到小顺序接收输入的列表的值
for i in range(a):
    nums.append(max(alist))#找出当前列表的最大值，并加入另一个列表
    alist.remove(max(alist))#去除当前列表的最大值
print(nums)#打印列表
'''
测试：
输入：
-1 0 0.3 -2 6 4.2 5.8 7 1 0.3
输出：
[7.0, 6.0, 5.8, 4.2, 1.0, 0.3, 0.3, 0.0, -1.0, -2.0]
'''

#第二题由于我智商有限，用了一个蠢办法
names=['guoyuhui','zengqianhan','zhangmengzhuo','zhuyuxuan','zhangjiawei','xiezejun','liuhaoyu','jiangyan','hechenxuan']#初始化，按照题意创建列表
a=len(names)
yunmu=['a','o','e','i','u','v','ai','ei','ui','ao','ou','iu','ie','ve','er','an','en','in','un','vn','ang','eng','ing','ong']
b=len(yunmu)
for t in range(a):#第一轮循环，把zh/ch/sh全部换成z/c/s
    names[t]=names[t].replace('zh','z')
    names[t]=names[t].replace('ch','c')
    names[t]=names[t].replace('sh','s')
for t in range(a):#第二轮使用双重循环，按照韵母长度从大到小的顺序进行删除，最后每个名字就只剩第一个字母了
    for i in range(b):
        names[t]=names[t].replace(yunmu[b-i-1],'')
print(names)
'''
测试：
输出：
['gyh', 'zqh', 'zmz', 'zyx', 'zjw', 'xzj', 'lhy', 'jy', 'hcx']
'''