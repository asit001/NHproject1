import requests
from bs4 import BeautifulSoup

def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def main():
    url = 'https://blog.python.org/'
    data = get_data(url)
    print(data.prettify())

if __name__ == '__main__':
    main()