import requests
import urllib
import pandas as pd
from requests_html import HTMLSession


def get_source(url):
    """Return the source code for the provided URL.

    Args:
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html.
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

# links = scrape_google("co working london")
#
# print(links)


def get_results(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    return response


def parse_results(response):
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"

    results = response.html.find(css_identifier_result)

    output = []

    for result in results:

        try:
            item = {
                'title': result.find(css_identifier_title, first=True).text,
                'link': result.find(css_identifier_link, first=True).attrs['href'],
                'text': result.find(css_identifier_text, first=True).text
            }

            output.append(item)
        except AttributeError as e:
            print(e)
            continue
    return output


def google_search(query):
    response = get_results(query)
    df = pd.DataFrame(parse_results(response))
    return df


results = google_search("web scraping")
print(results)


