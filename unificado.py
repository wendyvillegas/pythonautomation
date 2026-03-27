from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException

print("\n==============================")
print(" AUTOMATIZACION DE RED PYTHON ")
print("==============================\n")


# =========================
# DATOS DE DISPOSITIVOS
# =========================

switch = {
    'device_type': 'cisco_nxos',
    'host': '10.10.20.40',
    'username': 'admin',
    'password': 'RG!_Yw200'
}

router = {
    'device_type': 'cisco_ios',
    'host': '10.10.20.48',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 22
}


# =========================
# CONFIGURACION SWITCH
# =========================

config_switch = [

    'vlan 10',
    'name RED1',

    'vlan 20',
    'name RED2',

    'interface Eth1/10',
    'switchport',
    'switchport mode access',
    'switchport access vlan 10',
    'no shutdown',

    'interface Eth1/20',
    'switchport',
    'switchport mode access',
    'switchport access vlan 20',
    'no shutdown',

    'interface Eth1/2',
    'switchport',
    'switchport mode trunk',
    'switchport trunk allowed vlan 10,20'
]


# =========================
# CONFIGURACION ROUTER
# =========================

config_router = [

    'hostname Router1',
    'service password-encryption',
    'no ip domain lookup',
    'banner motd $SOLO PERSONAL AUTORIZADO$',
    'ip domain name uisrael.edu.com',

    'interface g2.10',
    'encapsulation dot1q 10',
    'ip address 192.168.10.1 255.255.255.0',

    'interface g2.20',
    'encapsulation dot1q 20',
    'ip address 192.168.20.1 255.255.255.0',

    'interface g2',
    'no shutdown',

    'ip dhcp excluded-address 192.168.10.1 192.168.10.9',

    'ip dhcp pool RED10',
    'network 192.168.10.0 255.255.255.0',
    'default-router 192.168.10.1',

    'ip dhcp excluded-address 192.168.20.1 192.168.20.9',

    'ip dhcp pool RED20',
    'network 192.168.20.0 255.255.255.0',
    'default-router 192.168.20.1'
]


# =========================
# CONFIGURACION SWITCH
# =========================

try:

    print("Conectando al SWITCH...\n")

    con_sw = ConnectHandler(**switch)

    print("Configurando SWITCH...\n")

    salida = con_sw.send_config_set(config_switch)
    print(salida)

    print("\nVerificando VLANs")
    print(con_sw.send_command("show vlan brief"))

    print("\nGuardando configuracion")
    con_sw.save_config()

    con_sw.disconnect()

    print("\nSWITCH CONFIGURADO CORRECTAMENTE\n")

except NetmikoAuthenticationException:
    print("Error de autenticacion en el SWITCH")

except NetmikoTimeoutException:
    print("Tiempo de conexion agotado con el SWITCH")


# =========================
# CONFIGURACION ROUTER
# =========================

try:

    print("\nConectando al ROUTER...\n")

    con_rt = ConnectHandler(**router)

    print("Configurando ROUTER...\n")

    salida = con_rt.send_config_set(config_router)
    print(salida)

    print("\nVerificando interfaces")
    print(con_rt.send_command("show ip interface brief"))

    print("\nVerificando DHCP")
    print(con_rt.send_command("show ip dhcp binding"))

    print("\nGuardando configuracion")
    con_rt.save_config()

    con_rt.disconnect()

    print("\nROUTER CONFIGURADO CORRECTAMENTE\n")

except NetmikoAuthenticationException:
    print("Error de autenticacion en el ROUTER")

except NetmikoTimeoutException:
    print("Tiempo de conexion agotado con el ROUTER")


print("\n=================================")
print(" AUTOMATIZACION FINALIZADA ")
print("=================================\n")
