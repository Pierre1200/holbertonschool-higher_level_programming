#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetches and prints the titles of the first 10 posts from the API.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches posts from the JSONPlaceholder API and saves them to a file.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        list_filtred = []
        for post in posts:
            list_filtred.append({
                'userId': post.get('userId'),
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['userId', 'id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in list_filtred:
                writer.writerow(post)
