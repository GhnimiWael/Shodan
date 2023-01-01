import shodan

# Replace YOUR_API_KEY with your actual API key
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Create a Shodan client
api = shodan.Shodan(api_key)

# Set the search query
query = "product:webcam"

# Perform the search
results = api.search(query)

# Print the results
print("Total Results: %s" % results["total"])
for result in results["matches"]:
  print("IP: %s" % result["ip_str"])
  print("Organization: %s" % result["org"])
  print("Operating System: %s" % result["os"])
  print("Hostnames: %s" % ", ".join(result["hostnames"]))
  print("====================")


