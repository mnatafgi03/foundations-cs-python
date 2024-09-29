def validate_ipv4(ip_address):
    octets = ip_address.split('.')
    
    if len(octets) != 4:
        return "Invalid IPv4 address"
    
    for octet in octets:
        if not octet.isdigit() or (octet[0] == '0' and len(octet) > 1):
            return "Invalid IPv4 address"
        
        num = int(octet)
        if num < 0 or num > 255:
            return "Invalid IPv4 address"
    
    return "Valid IPv4 address"

ip_address = input("Please enter an IP address: ")
print(validate_ipv4(ip_address))
