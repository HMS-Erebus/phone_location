
import subprocess

def enable_dhcp(interface_name):
    try:
        # 使用 netsh 命令开启 DHCP
        subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'address', interface_name, 'dhcp'])
        subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'dnsservers', interface_name, 'dhcp'])
        print("DHCP enabled successfully.")
    except Exception as e:
        print("Failed to enable DHCP:", str(e))

if __name__ == "__main__":
    interface_name = input("Enter the interface name (e.g., 'Ethernet', 'Wi-Fi'): ")
    enable_dhcp(interface_name)