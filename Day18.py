url = "https://google.com"

# Step 1: Separate the scheme (protocol) from the rest
# We split once at '://'
scheme, remaining = url.split("://", 5)

print("Scheme:", scheme)  # Output: Scheme: https
print("Remaining:", remaining)  # Output: Remaining: google.com