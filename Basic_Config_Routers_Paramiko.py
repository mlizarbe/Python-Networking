
import paramiko
import time
# import getpass

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# ssh_client.connect(hostname="10.1.1.10",port=22,username="u1",password="cisco",
# 					look_for_keys=False,allow_agent=False)
# password=getpass.getpass("Enter Password: ")
#Conecting to Router 1
router1={"hostname":"10.118.40.231","port":"22","username":"cisco","password":"cisco"}
router2={"hostname":"10.118.40.232","port":"22","username":"cisco","password":"cisco"}
router3={"hostname":"10.118.40.233","port":"22","username":"cisco","password":"cisco"}

routers=[router1,router2,router3]

for i in routers:
	print(f"Connecting to {i['hostname']}")
	ssh_client.connect(**i,look_for_keys=False,allow_agent=False)
	shell=ssh_client.invoke_shell()
	shell.send("enable\n")
	shell.send("cisco\n")
	shell.send("terminal length 0\n")
	shell.send("show ip int brief\n")
	time.sleep(2)
	output=shell.recv(10000).decode()
	print(output)


	# if ssh_client.get_transport().is_active()==True:
	# 	print("Closing Connection")
	# 	ssh_client.close()

