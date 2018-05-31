#-*- coding:UTF-8 -*-
import dns.resolver
import os,time
import httplib2
import asyncio
now = lambda : time.time()#定义一个获取当前时间的匿名函数
start=now()#获取程序开始执行的时间

#appdomain = 'xn--164b'

async def dns_query(domain):#定义dns查询函数，该函数的dns查询过程会消耗比较多的时间
  iplist = []
  domain_ips=dns.resolver.query(domain,'A')
  for i in domain_ips.response.answer:
    for j in i.items:
      if j.rdtype==28:
        iplist.append(j.address)
  return iplist
async def get_iplist(domain = ''):
  try: 
    A = await dns_query(domain)#将消耗比较多的操作放到await后，执行时挂起。#await 后边必须跟一个awaitable对象，须是协程
    for ip in A:
      checkurl=ip+":80"
      getcontent=""
      httplib2.socket.setdefaulttimeout(5)
      conn=httplib2.Http()
      try:
        resp,getcontent=conn.request("http://"+checkurl)
      finally:
        if resp['status']=='200':
          print("{} is ok!".format(ip))
          return ip      
  except Exception as e:
    print("dns resolver error %s" % str(e))
    return

#def callback(future):#绑定回调函数
#  for ip in future.result():
#    checkurl=ip+":80"
#    getcontent=""
#    httplib2.socket.setdefaulttimeout(5)
#    conn=httplib2.Http()
#    try:
#      resp,getcontent=conn.request("http://"+checkurl)
#    finally:
#      if resp['status']=='200':
#        print("{} is ok!".format(ip))
if __name__="__main__":
  tasks=[]
  with open('domain_list.txt','r') as file:
    for domain_line in file:
      coroutine=get_iplist(domain_line.strip())
      task=asyncio.ensure_future(coroutine)
#     task.add_done_callback(callback)
      tasks.append(task)  
  #couortine1=get_iplist('xn--zf')
  loop=asyncio.get_event_loop()
  #task1=asyncio.ensure_future(couortine1)
  #task1.add_done_callback(callback)
  loop.run_until_complete(asyncio.wait(tasks))
  loop.close()
  print("Time Cost is:",now() - start)