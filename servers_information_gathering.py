import shodan

# Function to authenticate with the Shodan API
def authenticate():
    api = shodan.Shodan(YOUR_API_KEY)
    return api

# Function to search Shodan for servers
def search_servers(api):
    # Search for servers using a specific query
    results = api.search('YOUR_QUERY')
    
    # Print the number of results
    print('Total Results:', results['total'])
    
    # Print the information for each result
    for result in results['matches']:
        print('IP:', result['ip_str'])
        print('Port:', result['port'])
        print('Organization:', result.get('org', 'n/a'))
        print('Operating System:', result.get('os', 'n/a'))
        print('Hostnames:', result.get('hostnames', 'n/a'))
        print('Vulnerabilities:', result.get('vulns', 'n/a'))
        print()

# Main function to execute the search
def main():
    # Authenticate with the Shodan API
    api = authenticate()
    
    # Search for servers
    search_servers(api)

if __name__ == '__main__':
    main()

