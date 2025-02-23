import paramiko
import time

#Settings
ip_list = ["YOUR_IP1","YOUR_IP2","YOUR_IP3","YOUR_IP4"]
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Print list ip dan mesin
x=0;
for ipaddr in ip_list:
    x=x+1
    print("Mesin", x,":", ipaddr)

#Pilihan untuk memilih salah satu mesin
def pilihanpertama():
    mesin = input("Masukkan nomor mesin : ")
    mesin = int(mesin)
    ssh_client.connect(hostname=ip_list[mesin-1],username=username,password=password)
    print ("Sukses login ke {0} (Mesin {1})".format(ip_list[mesin-1], (mesin)))
    conn = ssh_client.get_transport().open_session()
    conn.invoke_shell()

    #commandline
    conn.send("cd tugas_pp\n")
    conn.send("python3 t1\n")

    time.sleep(1)
    output = conn.recv(65535).decode('ascii')
    print(output)

#Pilihan untuk memilih semua mesin
def pilihankedua ():
    x=1
    for ip_address in ip_list:
        ssh_client.connect(hostname=ip_address,username=username,password=password)
        print ("Sukses login ke {0} (Mesin {1})".format(ip_address, x))
        x=x+1
        conn = ssh_client.get_transport().open_session()
        conn.invoke_shell()

        #commandline
        conn.send("cd tugas_pp\n")
        conn.send("python3 t1\n")

        time.sleep(1)
        output = conn.recv(65535).decode('ascii')
        print(output)
        print()

#Menu Pilihan
print("\n1. Ambil salah satu mesin\n2. Ambil semua\n")
x = input("Pilihan : ")
x = int(x)
if (x==1):
    pilihanpertama()
if (x==2):
    pilihankedua()
    
ssh_client.close()
