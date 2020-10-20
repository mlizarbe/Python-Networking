from netmiko import ConnectHandler

router1={
    "host":"10.118.40.231",
    "port":"22",
    "username":"cisco",
    "password":"cisco",
    "secret":"cisco",       #Mode privileged
    "device_type":"cisco_ios"
    }

connection= ConnectHandler(**router1)
prompt=connection.find_prompt()
print(prompt)
if ">" in prompt:
    connection.enable()

prompt=connection.find_prompt()
print(prompt)


output=connection.send_command("show run")
print(output)

if not connection.check_config_mode():
    connection.config_mode()

print(connection.check_config_mode())
output=connection.send_command("do show ip int br")
print(output)

connection.exit_config_mode()
print(connection.check_config_mode())


print("closing connection")
connection.disconnect()


# router1={"hostname":"10.118.40.231","port":"22","username":"cisco","password":"cisco"}
# router2={"hostname":"10.118.40.232","port":"22","username":"cisco","password":"cisco"}
# router3={"hostname":"10.118.40.233","port":"22","username":"cisco","password":"cisco"}

# routers=[router1,router2,router3]