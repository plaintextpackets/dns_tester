import time
import dns.resolver

# Pre-defined list of websites
websites = [
    "powells.com",
    "vermontcountrystore.com",
    "mcmenamins.com",
    "banningsrestaurant.com",
    "zankouchicken.com",
    "bigbadtoystore.com",
    "techbargains.com",
    "powscience.com",
    "chuaochocolatier.com",
    "santacruzshakespeare.org",
    "kayakconnection.com",
    "mountaincrestgardens.com",
    "railtown1897.org",
    "tenayalodge.com",
    "birchlane.com",
    "bbtheatres.com",
    "seeedstudio.com",
    "gardensalive.com",
    "batteriesplus.com",
    "sciencebuddies.org"
]


# Example usage
print("List of websites:")
for website in websites:
    print(website)


# Pre-defined list of public DNS servers
dns_servers = [
    {"name": "Google", "address": "8.8.8.8"},
    {"name": "Quad9", "address": "9.9.9.9"},
    {"name": "OpenDNS", "address": "208.67.222.222"},
    {"name": "Cloudflare", "address": "1.1.1.1"},
    {"name": "Level3", "address": "4.2.2.2"},
    {"name": "Norton ConnectSafe", "address": "199.85.126.10"},
    {"name": "Comodo Secure DNS", "address": "8.26.56.26"},
    {"name": "Verisign", "address": "64.6.65.6"},
    {"name": "Yandex.DNS", "address": "77.88.8.8"},
    {"name": "Neustar", "address": "156.154.70.5"}
]

# Function to perform DNS queries and measure response time
def test_dns_performance(server_name, server_address=None):
    response_times = []
    resolver = dns.resolver.Resolver()
    if server_address:
        resolver.nameservers = [server_address]

    for website in websites:
        try:
            start_time = time.time()
            resolver.resolve(website)
            end_time = time.time()
            response_times.append(end_time - start_time)
        except Exception as e:
            print(f"Error querying {website} with {server_name}: {e}")

    average_time = sum(response_times) / len(response_times) if response_times else float('inf')
    print(f"Average response time for {server_name}: {average_time:.4f} seconds")
    return average_time

# Test with the system's default DNS resolver
print("Testing with the system's default DNS resolver...")
default_dns_time = test_dns_performance("Default DNS Resolver")

# Test with each public DNS server
dns_performance = []
for dns_server in dns_servers:
    print(f"Testing with {dns_server['name']} DNS server...")
    avg_time = test_dns_performance(dns_server['name'], dns_server['address'])
    dns_performance.append((dns_server['name'], avg_time))

# Summary

print("\nDNS Performance Summary:")
print(f"Default DNS Resolver: {default_dns_time:.2f} ms")  # Print in milliseconds
for server, time in dns_performance:
    print(f"{server}: {time:.2f} ms")  # Print in milliseconds