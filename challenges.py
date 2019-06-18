def main_menu():
    print('Please choose an exercise: ' + '\n'
        '1. Filesystem,' + '\n'
        '2. Users,' + '\n'
        '3. Security,' + '\n'
        '4. Package management,' + '\n'
        '5. Kernel tuning,' + '\n'
        '6. Log management,' + '\n'
        '7. Exit')

def fs(fsname):
    print('a - Create filesystem {}'.format(fsname) + '\n'
          'b - Use your skills to fill {}'.format(fsname) + '\n'
          'c - Grow filesystem')

def check_users(user):
    print('a - Create a {} user with the following specs: '.format(user) + '\n'
            'a1 - User shell to zsh' + '\n'
            'a2 - User home dir to /tmp/{} '.format(user))
          
def security():
    print('A - Ensure previously created user can sudo without password \n'
          'B - Ensure user can use fdisk command (and only fdisk) as sudo \n'
          'C - Ensure Selinux is enabled \n'
          'D - Ensure iptables/firewalld is enabled')

def package_mgmt():
    print('A - Install any package \n'
          'B - Remove previously installed package \n'
          'C - Check if a package is installed \n'
          'D - List installed packages \n'
          'E - List files installed by X package')

def kernel_mgmt():
    print('A - List kernel parameters \n'
          'B - Change any bool kernel parameter \n'
          'C - Reboot and ensure new parameter is applied \n')

def log_mgmt():
    print('A - Review dmesg and /var/log directories \n'
          'B - Use yum to install a package and found the log lines showing your last installation at /var/log \n'
          'C - Use daemon config to change location of default logs, and prove you\'ve done it')

