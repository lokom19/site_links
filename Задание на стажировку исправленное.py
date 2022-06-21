import threading
import time

import requests
from bs4 import BeautifulSoup as bs


def map(urls, i):
    start_time = time.time()
    for i in range(len(urls)):
        r = requests.get(urls[i])

        soup = bs(r.text, "html.parser")

        for link in soup.find_all('a'):
            urls.append(link.get('href'))
            print(urls)
        try:
            return map(urls, 1)
            time1 = time.time() - start_time
        except:
            continue


map([input('¬ведите URL сайта: ')], 0)


def map2(urls, i):
    start_time = time.time()

    for i in range(len(urls)):
        r = requests.get(urls[i])

        soup = bs(r.text, "html.parser")

        for link in soup.find_all('a'):
            urls.append(link.get('href'))
            print(urls)
        try:
            return map2(urls, 1)
            time2 = time.time() - start_time
        except:
            continue


map2([input('¬ведите URL сайта: ')], 0)


def map3(urls, i):
    start_time = time.time()
    for i in range(len(urls)):
        r = requests.get(urls[i])

        soup = bs(r.text, "html.parser")

        for link in soup.find_all('a'):
            urls.append(link.get('href'))
            print(urls)
        try:
            return map3(urls, 1)
            time3 = time.time() - start_time
        except:
            continue


map3([input('¬ведите URL сайта: ')], 0)


def map4(urls, i):
    start_time = time.time()
    for i in range(len(urls)):
        r = requests.get(urls[i])

        soup = bs(r.text, "html.parser")

        for link in soup.find_all('a'):
            urls.append(link.get('href'))
            print(urls)
        try:
            return map4(urls, 1)
            time4 = time.time() - start_time
        except:
            continue


map4([input('¬ведите URL сайта: ')], 0)


def map5(urls, i):
    for i in range(len(urls)):
        r = requests.get(urls[i])

        soup = bs(r.text, "html.parser")

        for link in soup.find_all('a'):
            urls.append(link.get('href'))
            print(urls)
        try:
            return map5(urls, 1)
            time5 = time.time() - start_time
        except:
            continue


map5([input('¬ведите URL сайта: ')], 0)


def main():
    start_time = time.time()
    t1 = threading.Thread(target=map)
    t2 = threading.Thread(target=map2)
    t3 = threading.Thread(target=map3)
    t4 = threading.Thread(target=map4)
    t5 = threading.Thread(target=map5)
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
    print(f'ќбщее врем€ выполнени€ программы: {time_waiting}')
