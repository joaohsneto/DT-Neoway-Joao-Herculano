import requests
from parsel import Selector
from connection import insert_data, close_connection


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


# função auxiliar para coletar os nomes dos estudantes
def scrape_student_name(html_content):
    selector = Selector(html_content)
    result = selector.xpath("/html/body/div[1]/text()").get()
    return result


# função auxiliar para coletar os scores dos estudantes
def scrape_student_score(html_content):
    selector = Selector(html_content)
    result = selector.xpath("/html/body/div[2]/text()").get()
    return result


# função auxiliar para coletar o link de próxima página
def scrape_next_page_path(html_content):
    selector = Selector(html_content)
    result = selector.css("div:nth-child(12) > a ::attr(href)").get()
    return result


# Iniciando a coleta dos dados dos estudantes
if __name__ == "__main__":
    base_url = "https://sample-university-site.herokuapp.com"
    quotes_html = fetch_content(base_url)
    cpf_paths = scrape_cpf_path(quotes_html)


# coletando os links dos cpfs de todas as páginas
    print("Loading...")
    while True:
        next_page = scrape_next_page_path(quotes_html)
        if next_page == "/approvals/6":
            break
        quotes_html = fetch_content(base_url + next_page)
        cpf_paths.extend(scrape_cpf_path(quotes_html))


# coletando as informações dos estudantes e inserindo no banco de dados
    for path in cpf_paths:
        student_cpf = path.split("/")[-1].replace("-", "").replace(".", "")
        students_html = fetch_content(base_url + path)
        student_name = scrape_student_name(students_html).strip().upper()
        student_score = scrape_student_score(students_html).strip()
        insert_data(student_cpf, student_name, float(student_score))
    close_connection()
    print("Done!")
