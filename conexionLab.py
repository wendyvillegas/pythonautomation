from virl2_client import ClientLibrary

client = ClientLibrary(
    "https://10.10.20.161",
    "developer",
    "C1sco12345",
    ssl_verify=False
)

labs = client.find_labs_by_title("exam")
lab = labs[0]
lab.sync()   
print("Lab encontrado:", lab.title)
lab.sync()

for node in lab.nodes():
    print("Nodo:", node.label)
    print("Estado:", node.state)
    console_key = node.console_key()
    print("Console key:", console_key)
    console_url = f"telnet 10.10.20.40 {console_key}"
    print("Comando consola:", console_url)


##sudo ip addr add 192.168.20.10/24 dev eth0


#sudo ip route add default via 192.168.20.1 dev eth0
