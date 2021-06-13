import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect('192.168.1.11', username='poweruser', 
    password='ub326#rpi')
# stdin, stdout, stderr = ssh.exec_command("uptime")
stdin, stdout, stderr = ssh.exec_command(
    "sudo -S hdparm -B /dev/sda1")
stdin.write('ub326#rpi\n')
print(stderr.readlines())
stdin.flush()
print (stdout.readlines())