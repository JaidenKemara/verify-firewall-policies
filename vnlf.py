from multiprocessing import Pool
import socket

# Colors
RED = "\033[91m"
GREEN = "\033[32m"
GREY = "\033[90m"
BOLD = "\033[1m"
ITALIC = "\x1B[3m"
END = "\033[0m"

# Test this host.
test_host = "scanme.nmap.org" 

# Test if connections on these ports can make it past the firewall.
# Change these to match any policies you may have on the firewall.
test_ports = [80, 9929, 31337, 22] 

# Function for sending a connection to each port on the host.
def test_port(port):

    # https://docs.python.org/3/library/socket.html
    s = socket.socket()

    # Set the timeout in seconds. This will delay the output while it waits for the response. In this case, the delay is 3 seconds.
    # Usually this would lead to a 12 second delay if each of the 4 connection has to wait the full 3 seconds for the response.
    # Since Pool() from multiprocessing is used, the delay is only 3 seconds since the connections are ran concurrently rather than sequentially.
    s.settimeout(3)

    try:
        # Try the connection
        s.connect((test_host, port))

        # Close the connection, it doesn't need to stay open after the response.
        s.close()

        # If connection is successful, print the port and "SUCCESS".
        return (port, f"{GREEN}SUCCESS{END}")
    
    # If the connection is refused, print the port and "FAILED (refused)".
    except ConnectionRefusedError:
        s.close()
        return (port, f"{RED}FAILED{END} {GREY}(refused){END}")
    
    # If no response is heard within the limit set on line 24, the port is likely filtered.
    except socket.timeout:
        s.close()
        return (port, f"{RED}FAILED{END} {GREY}(timeout){END}")
    
    # If it fails due to another error, print the reason.
    except Exception as e:
        s.close()
        return (port, f"{RED}ERROR{END}: {e}")
    
if __name__ == "__main__":
    print(f"\n-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~\n\nTESTING TARGET: {ITALIC}{test_host}{END}\nTESTING PORTS: {ITALIC}[{test_ports[0]}, {test_ports[1]}, {test_ports[2]}, {test_ports[3]}]{END}\n\n-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~\n")

    # Use Pool() from multiprocessing to create a process for each tested port. 
    # https://docs.python.org/3/library/multiprocessing.html
    with Pool(4) as p:
        results = p.map(test_port, test_ports)

    # Print info for each port and status in the results Pool.
    for port, status in results:
        # :<6 is used to align the output
        # https://www.delftstack.com/howto/python/python-print-column-alignment/
        print(f"* {BOLD}{port:<6}{END} - {status}")
    print("\n")

