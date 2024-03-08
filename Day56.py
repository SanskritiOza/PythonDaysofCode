import re

def extract_urls(text):
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/?'  # Regular expression pattern for URLs
    return re.findall(url_pattern, text)

# Example usage:
text = "Here is a sample text with a URL https://www.example.com and another URL http://example.org"
urls = extract_urls(text)
print(urls)
