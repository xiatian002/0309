# -*- coding:utf-8 -*-

#创建一个person类，用来创建person对象，包含设置姓名，年龄，性别的set函数,和一个显示姓名函数
#创建一个使用yield的生成器函数，用来返回person的基本信息
#验证yield的作用是返回值后函数挂起，待调用生成器的函数后续语句执行完毕后继续执行生成器。
import time,os,sys
class person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
#    def setinfo(self,name,age,sex):
#        self.name = name
#        self.age = age
#        self.sex = sex
    def displayname(self):
        return self.name
    def displayage(self):
        return self.age

def showName(persions):
    for per in persions:
        yield per.name#,':',per.age#可行但是两个返回值会自动组成一个元组

def showInfo(persons):
    for personName in showName(persons):
        print('person name is:{}'.format(personName))

if __name__=='__main__':
    p1=person('Joy','31','female')
    p2=person('Bob','18','female')
    p3=person('Lily','25','male')
#    p1.setinfo("joy",'31','female')
#    p2.setinfo("bob","18","female")
#    p3.setinfo('lily','25','male')
    persons=[p1,p2,p3]
    showInfo(persons)