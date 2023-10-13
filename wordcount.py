import requests
from collections import Counter
# Read the text file from python.org
response = requests.get("https://blog.python.org/about/gettingstarted/")
text = response.text
# Count the frequency of the word 'python' in the text
python_count = text.count('python')
# Print the frequency of the word 'python'
print(f"The word 'python' appears {python_count} times in the text.")