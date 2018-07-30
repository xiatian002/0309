# -*- coding:utf-8 -*-

#######测试两种排序算法#######
##张鹏##
##2018年7月30日##
#######符号排序#######
def StringSort(data):
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
def fastSort(arry,left,right):
    if left >= right:
        return
    low = left
    hight = right
    key = arry[low]
    while left<right:
        while left < right and arry[right] > key:
            right -= 1
        #arry[left] = arry[right]
        while left < right and arry[left] <= key:
            left += 1
        arry[right],arry[left] = arry[left],arry[right]
    arry[right],arry[left] = arry[left],arry[right]
    fastSort(arry,low,left - 1)
    fastSort(arry,left + 1,right)

data=['-','-','+','+','-','+','-','+','+','-']
print(StringSort(data))