#MAQUINA HABILITAR
#ssh -L 2222:localhost:2222 -L 2223:localhost:2223 developer@10.10.20.50
    #'username wen secret wen',
    #'crypto key generate rsa modulus 1024',
    
    #'ip route ....0 ...225.0 ip interfaz salida/ingreso al otro router',

    #router rip
    #network .0 red vecinos

    #route ospf 123
    #network ...0 ...255 area 0

    #stanby version 2
    #standby 1 ip iproutervirtual
    #standy 1 priority 150 ##Solo al router principal
    #stanby 1 preempt

    #ip dhcp excluded-address 192.168.10.1 192.168.10.9
    #interface g1
    #ip dhcp pool REDA
    #network 192.168.10.0 255.255.255.0
    #default-router 192.168.10.1
    #dns-server 8.8.8.8
    #domain-name uisrael.edu.com

    #ipv6 unicast-routing 
    # ipv6 address2001:ABC::100/64
    #ipv6 addrees FE80::1/64 link-local


from netmiko import ConnectHandler

r1={
    'device_type':'cisco_ios',
    'host':'10.10.20.48',
    'username':'developer',
    'password':'C1sco12345',
    'port':22
}



con1= ConnectHandler(**r1)

comR=[
    'hostname Router1',
    #'enable secret password',
    'service password-encryption',
    'no ip domain lookup',
    'banner motd $SOLO PERSONAL AUTORIZADO$',

    'interface g2.10',
    'encapsulation dot1q 10',
    'ip address 192.168.10.1 255.255.255.0', 

    'interface g2.20',
    'encapsulation dot1q 20',
    'ip address 192.168.20.1 255.255.255.0', 

    'interface g2',
    'no shutdown',

    'ip dhcp excluded-address 192.168.10.1 192.168.10.9',
    'ip dhcp pool RED30',
    'network 192.168.10.0 255.255.255.0',
    'default-router 192.168.10.1',
    'exit',


    'ip dhcp excluded-address 192.168.20.1 192.168.20.9',
    'ip dhcp pool RED40',
    'network 192.168.20.0 255.255.255.0',
    'default-router 192.168.20.1',
    'exit'

]

salida1=(con1.send_config_set(comR))
print('Configuracio para router en progreso')
print(salida1)
print('Conf finalizada de router')

salida2=(con1.send_command('show ip interface brief'))
print('Interfaces  configuradas')
print(salida2)
salida2=(con1.send_command('show running-config'))
print('dhcp  configurado')
print(salida2)

con1.disconnect()
