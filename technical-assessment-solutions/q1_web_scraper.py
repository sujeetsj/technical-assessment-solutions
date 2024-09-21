import requests
from bs4 import BeautifulSoup
import time


def scrape_news_articles(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    article_containers = soup.find_all('div', class_='articles')

    results = []
    for container in article_containers:
        articles = container.find_all('div', class_='snaps')

        for article in articles:
            link_element = article.find('a')
            if link_element:
                title = link_element.get('title')
                article_url = link_element.get('href')

                img_context = article.find_next_sibling('div', class_='img-context')
                if img_context:
                    date_element = img_context.find('div', class_='date')
                    date = date_element.text.strip() if date_element else "Date not available"
                else:
                    date = "Date not available"

                results.append({'title': title, 'url': article_url, 'date': date})

    return results


if __name__ == "__main__":
    news_url = "https://indianexpress.com/latest-news/"
    articles = scrape_news_articles(news_url)

    if not articles:
        print("No articles found. The website structure might have changed.")
    else:
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"URL: {article['url']}")
            print(f"Date: {article['date']}")
            print("---")
            time.sleep(0.1)