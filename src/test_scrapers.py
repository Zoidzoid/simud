import requests
from bs4 import BeautifulSoup


def test_futebolinterior():
    url = 'https://www.futebolinterior.com.br/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Add logic to parse the Serie D standings
    print('Futebol Interior Scraping:')
    # Example selector - change according to the website's structure
    standings = soup.find_all('div', class_='standings')
    print(standings)


def test_ge_globo():
    url = 'https://ge.globo.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Add logic to parse the Serie D standings
    print('GE Globo Scraping:')
    # Example selector - change according to the website's structure
    standings = soup.find_all('div', class_='table')
    print(standings)


def test_flashscore():
    url = 'https://www.flashscore.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Add logic to parse the Serie D standings
    print('Flashscore Scraping:')
    # Example selector - change according to the website's structure
    standings = soup.find_all('div', class_='results')
    print(standings)


if __name__ == '__main__':
    test_futebolinterior()
    test_ge_globo()
    test_flashscore()