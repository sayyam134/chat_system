import socket

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        
        return ip_address
    except socket.error:
        return "Unable to get IP address."

if __name__ == "__main__":
    ip_address = get_ip_address()
    print("Your IP address is:", ip_address)
