# -*- coding:utf-8 -*-

#######测试两种排序算法#######
##张鹏##
##2018年7月30日##
#######符号排序#######
def StringSort(data):#该排序的重点是前后的两个list元素都需要进行位置更换。
    startIndex=0
    endIndex=0
    count=len(data)
    while startIndex + endIndex < count:
        if data[startIndex] == '-':
            data[startIndex],data[count - endIndex - 1 ]=data[count - endIndex - 1],data[startIndex]
            endIndex += 1
        else:
            startIndex += 1
    return data
#######快速排序#######
'''def fastSort(arry,left,right): #代码不整齐还需修正
    if left >= right:
        return
    low = left
    hight = right
    key = arry[low]
    while left<right:
        while left < right and arry[right-1] > key:
            right -= 1
        #arry[left] = arry[right]
        while left < right and arry[left] <= key:
            left += 1
        arry[right-1],arry[left] = arry[left],arry[right-1]
#    arry[right],arry[left] = arry[left],arry[right]
    fastSort(arry,low,left)#左右分片递归
    fastSort(arry,left + 1,right-1)
'''
def quick_sort(array,left,right):#算法导论中快速排序算法
    if left < right :
        q=partition(array,left,right)
        quick_sort(array,left,q-1)
        quick_sort(array,q+1,right)

def partition(array,left,right):
    x = array[right]
    i = left - 1
    for j in range(left,right):
        if array[j] <= x:
            i += 1
            array[i],array[j] = array[j],array[i]
    array[i + 1],array[right] = array[right],array[i +1]
    return i + 1


data=['-','-','+','+','-','+','-','+','+','-']
print(StringSort(data))

array=[1,3,4,6,18,68,23,99,1000,8,43,332]
print(quick_sort(array,0,len(array) - 1))