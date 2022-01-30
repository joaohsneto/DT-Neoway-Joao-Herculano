import requests
from parsel import Selector


# função auxiliar para requisição html
def fetch_content(html_content):
    try:
        res = requests.get(html_content)
        res.raise_for_status()
    except requests.HTTPError:
        return res.status_code
    return res.text


# função auxiliar para coletar os links dos cpfs
def scrape_cpf_path(html_content):
    selector = Selector(html_content)
    result = selector.css("li a ::attr(href)").getall()
    return result


if __name__ == "__main__":
    base_url = "https://sample-university-site.herokuapp.com"
    quotes_html = fetch_content(base_url)
    cpf_paths = scrape_cpf_path(quotes_html)
