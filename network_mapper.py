import shodan

# Replace YOUR_API_KEY with your actual API key
api_key = "YOUR_API_KEY"

# Create a Shodan object using your API key
shodan_api = shodan.Shodan(api_key)

# Set the IP range to search
start_ip = "192.168.0.1"
end_ip = "192.168.0.255"

# Perform the search using the IP range as the query
results = shodan_api.search(f"ip:{start_ip}-{end_ip}")

# Print the total number of results
print(f"Total results: {results['total']}")

# Iterate over the results and print the IP and hostname of each device
for result in results['matches']:
    print(f"IP: {result['ip_str']}, Hostname: {result['hostnames']}")
