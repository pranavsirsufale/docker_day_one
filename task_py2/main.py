import subprocess


def run_command(command):
    result = subprocess.run(command,stdin=True ,shell = True, capture_output=True,text=True)
    return result.stdout

'''
#? here are the rerences I am sharing
ifconfig ( MAC addres ) : https://itsfoss.com/find-mac-address-linux/

log files : https://ubuntu.com/tutorials/viewing-and-monitoring-log-files#1-overview

python subprocess : https://www.geeksforgeeks.org/python-subprocess-module/





Authorization log. Location: /var/log/auth.log. ...
Daemon Log. Location: /var/log/daemon.log. ...
Debug log. Location: /var/log/debug. ...
Kernel log. Location: /var/log/kern.log. ...
System log. Location: /var/log/syslog. ...
Apache logs. Location: /var/log/apache2/ (subdirectory) ...
X11 server logs. ...
Login failures log.

cat /var/log/dmesg /var/log/auth.log 2>/dev/null | grep -Ei "error|failed"



	command > /dev/null 2>&1

'''






try:
    def capture_sys_config():
        ifconfig_output = run_command('ifconfig')
        print("___-----ifconfig----------")
        print(ifconfig_output)


        print('__________Save the MAC addresses in a file ___________')
        print('''
  =======================================================
              MAC ADDRESSES HAVE SAVED

              AND BEING READED FROM THE SAVED FILE
    =======================================================

''')
        mac_addresses = run_command("ifconfig | grep ether")


        with open("MAC_address.txt","w") as file:
            file.write(mac_addresses)
            file.close()
        print('the mac addresses have been saved here again reading saved file')

        with open('MAC_address.txt','r') as file:
            content = file.read()
            print(content)
            file.close()

        ip_add = run_command('ip -c addr')
        print("============================= IP Address =================")
        print(ip_add)

        iostat_output = run_command('iostat')
        print('----------------iostat-----------------')
        print(iostat_output)


        df_output = run_command('df -h')
        print('----------------df -h -----------------')
        print(df_output)

        top_output = run_command('top -b -d ')
        print('===================top ======================')
        run_command('^C')  
        
        print(top_output)

        run_command('exit')
except Exception as e:
    print(str(e))


try:
    def log_print():
        print('''
        Auth logs
    =======================================================
              NOTE : only printing tail ( last logs )
    =======================================================
              ''')
        auth_log = run_command('tail /var/log/auth.log')
        print(auth_log)

        print('----------------error ------------------------')
        
        print(run_command("cat /var/log/auth.log |grep -Ei 'error|failed' | tail"))
        print('----------------error ------------------------')
        
        
        print("""
========================================
              bootstrap logs 
""")
        boot_log = run_command('tail /var/log/bootstrap.log')
        print(boot_log)

        print('----------------error ------------------------')
        
        print(run_command('cat /var/log/bootstrap.log | grep -Ei "error|failed|failure|unable" | tail'))
        print('----------------error ------------------------')
        

        print("""
========================================
              dmesg  

""")    
        print(run_command('tail /var/log/dmesg'))
        print('----------------error ------------------------')
        
        print(run_command("cat /var/log/dmesg |grep -Ei 'error|failed|failure' | tail"))
        
        print('----------------error ------------------------')
        

        print("""
========================================
              kernel logs 
""")    
        print(run_command('tail /var/log/kern.log'))

        print('============================error log ===============')
        
        print(run_command("cat /var/log/kern.log | grep -Ei 'error|failed|failure' | tail"))

        print('============================error log ===============')
        


        print("""
========================================
              SYSTEM LOGS 
""")    
        print(run_command('tail /var/log/syslog'))


        print('============================error log ===============')
        
        print(run_command("cat /var/log/syslog |grep -Ei 'error|failed' | tail"))
        
        print('============================error log ===============')
              
except Exception as e:
    print(str(e))


print('''
1. Press 1 to print system configurations.
2. Press 2 to print System logs 
''')




try:
    operations = int(input("Enter for the valid input for the above mentioned operations : "))
    
    match operations:
        case 1:
            capture_sys_config()

        case 2:
            log_print()
except Exception as e:
    print(str(e))
