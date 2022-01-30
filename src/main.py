import requests


# função auxiliar para requisição html
def fetch_content(html_content):
    try:
        res = requests.get(html_content)
        res.raise_for_status()
    except requests.HTTPError:
        return res.status_code
    return res.text


if __name__ == "__main__":
    base_url = "https://sample-university-site.herokuapp.com/"
    quotes_html = fetch_content(base_url)
