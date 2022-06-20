# -*- coding: utf-8 -*-

import threading
import time
import pandas
from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient


def google():
    global urls
    global time1
    global url1
    start_time = time.time()
    # Define URL with a dynamic web content
    url1 = "https://www.google.com/"

    # Create a ScrapingAntClient instance
    client = ScrapingAntClient(token='94e8c1cf026941afa60c4bcf1c885d65')

    # Get the HTML page rendered content
    page_content = client.general_request(url1).content

    # Parse content with BeautifulSoup
    soup = BeautifulSoup(page_content)

    urls = []

    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    time1 = time.time() - start_time
    print(f'Время выполнения работы google: {time1}')
    print(len(urls))


def vk():

    global urls1
    global time2
    global url2

    start_time = time.time()

    # Define URL with a dynamic web content
    url2 = "https://vk.com/"

    # Create a ScrapingAntClient instance
    client = ScrapingAntClient(token='94e8c1cf026941afa60c4bcf1c885d65')

    # Get the HTML page rendered content
    page_content = client.general_request(url2).content

    # Parse content with BeautifulSoup
    soup = BeautifulSoup(page_content)
    urls1 = []
    for link in soup.find_all('a'):
        urls1.append(link.get('href'))
    time2 = time.time() - start_time
    print(f'Время выполнения работы vk: {time2}')
    print(len(urls1))


def crawler_test():
    global url3
    global time3
    global urls2

    start_time = time.time()

    # Define URL with a dynamic web content
    url3 = "http://crawler-test.com/"

    # Create a ScrapingAntClient instance
    client = ScrapingAntClient(token='94e8c1cf026941afa60c4bcf1c885d65')

    # Get the HTML page rendered content
    page_content = client.general_request(url3).content

    # Parse content with BeautifulSoup
    soup = BeautifulSoup(page_content)
    urls2 = []
    for link in soup.find_all('a'):
        urls2.append(link.get('href'))
    time3 = time.time() - start_time
    print(f'Время выполнения работы crawler_test: {time3}')
    print(len(urls2))


def habr():
    global url4
    global time4
    global urls3

    start_time = time.time()

    # Define URL with a dynamic web content
    url4 = "https://habr.com/ru/all/"

    # Create a ScrapingAntClient instance
    client = ScrapingAntClient(token='94e8c1cf026941afa60c4bcf1c885d65')

    # Get the HTML page rendered content
    page_content = client.general_request(url4).content

    # Parse content with BeautifulSoup
    soup = BeautifulSoup(page_content)
    urls3 = []
    for link in soup.find_all('a'):
        urls3.append(link.get('href'))
    time4 = time.time() - start_time
    print(f'Время выполнения работы habr: {time4}')
    print(len(urls3))


def sof():
    global url5
    global urls4
    global time5

    start_time = time.time()

    # Define URL with a dynamic web content
    url5 = "https://stackoverflow.com/"

    # Create a ScrapingAntClient instance
    client = ScrapingAntClient(token='94e8c1cf026941afa60c4bcf1c885d65')

    # Get the HTML page rendered content
    page_content = client.general_request(url5).content

    # Parse content with BeautifulSoup
    soup = BeautifulSoup(page_content)
    urls4 = []
    for link in soup.find_all('a'):
        urls4.append(link.get('href'))
    time5 = time.time() - start_time
    print(f'Время выполнения работы stackoverflow: {time5}')
    print(len(urls4))


start_time = time.time()




def main():
    global time_waiting

    start_time = time.time()
    t1 = threading.Thread(target=google)
    t2 = threading.Thread(target=vk)
    t3 = threading.Thread(target=crawler_test)
    t4 = threading.Thread(target=sof)
    t5 = threading.Thread(target=habr)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    time_waiting = time.time() - start_time
    print(f'Общее время выполнения программы: {time_waiting}')


if __name__ == "__main__":
    main()

df = pandas.DataFrame({"Url сайта" : [url1, url2, url3, url4, url5], "Время обработки" : [time1, time2, time3, time4, time5], "Количество ссылок": [len(urls), len(urls1), len(urls2), len(urls3), len(urls4)]})
print(df)