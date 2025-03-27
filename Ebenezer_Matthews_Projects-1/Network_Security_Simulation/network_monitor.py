import psutil
import time

# Function to monitor ongoing network connections
def monitor_network():
    while True:
        print("Monitoring active network connections...")
        for conn in psutil.net_connections(kind='inet'):
            print(f"Connection: {conn.laddr} -> {conn.raddr}")
        time.sleep(5)

if __name__ == "__main__":
    monitor_network()