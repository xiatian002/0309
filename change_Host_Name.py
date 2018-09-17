import os,sys
import socket
import re

service_host=''
filepath = 'minion'
network_file = 'network'
host_name = socket.gethostname()
zabbix_file = 'zabbix_agentd.conf'
change_str = lambda file_line : file_line.replace(host_name,service_host)

def get_salt_host(filepath):#获取本地salt id
    lines = open(filepath,'r').readlines()
    id_line = lines[-1]
    #print(id_line)
    service_host = id_line.split(':')[1]
    return service_host

def change_network_host(network_file,service_host,host_name):#更新hostname
    if host_name  != service_host:
        with open(network_file,'r') as net_file:
            lines=net_file.readlines()
        with open(network_file,'w') as new_net_file:
            for line in lines:
                if re.match('HOSTNAME',line):
                    line=change_str(line)
                new_net_file.write(line) 

def change_zabbix_conf(service_host,zabbix_conf=zabbix_file):#更新zabbix配置文件中host
    with open(zabbix_conf,'r') as zab_file:
        lines = zab_file.readlines()
    with open(zabbix_conf,'w') as new_zab_file:
        for line in lines:
            if re.match('Hostname',line):
                zabbix_host=line.split('=')[1]
                line=line.replace(zabbix_host,service_host)
            new_zab_file.write(line)
    
if __name__=="__main__":
    service_host = get_salt_host(filepath)
    change_network_host(network_file,service_host,host_name)
    change_zabbix_conf(service_host,zabbix_conf=zabbix_file)
    os.system('hostname '+service_host)