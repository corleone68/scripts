import sys
import time
import select
from getpass import getpass
import netmiko
import re
import os
from netmiko import Netmiko
from netmiko import ConnectHandler

platform = 'cisco_ios'
#type/change username
username: ''
password = getpass()

#specify path
ip_add_file = open(r'/home/','r')

for host in ip_add_file:
    host = host.strip()
    #Checking if Host is up...
    response = os.system("ping -c 2 -w 2 " + host)
    if response != 0:
      print(host, 'is down! skiping to next in list...')
      print()
      continue
    else:
      print(host, 'is up!')
    print()
    net_connect = Netmiko(ip = host, username='', password=password, device_type = platform)
    net_connect.find_prompt()
    net_connect.send_command("show ip int brief")   
    config_commands = ['int Loopback0', 'ip address 192.168.70.1 255.255.255.255']
    output2 = net_connect.send_config_set(config_commands)
    print(output2)
    output = net_connect.send_command("wr")
    print(output)
