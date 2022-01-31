# Desafio Técnico Neoway

Esse é um desafio técnico de seleção para ser apresentado a empresa Neoway, que visa criar um serviço para capturar a lista de pessoas listadas como aprovadas em um vestibular, e persistir o serviço em Banco de Dados.
<div align="center">
  <img src="https://raw.githubusercontent.com/joaohsneto/DT-Neoway-Joao-Herculano/main/src/public/script.gif"/>
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/joaohsneto/DT-Neoway-Joao-Herculano/main/src/public/approved_candidates.jpg" width="350"/>
  <img src="https://raw.githubusercontent.com/joaohsneto/DT-Neoway-Joao-Herculano/main/src/public/db_dt_neoway.jpg" width="369"/>
</div>

## 🛠️ Desenvolvido com:

* [Python](https://www.python.org/)
* [MySql](https://www.mysql.com/)

## 👨‍💻 Bibliotecas utilizadas para raspagem

* Requests
* Parsel

```
É necessário ter instalado o Python e MySql para instalação local.
```

### 🔧 Instalação

Em sua máquina abra uma instância do terminal:

Faça um clone desse repositório.

```
git clone git@github.com:joaohsneto/DT-Neoway-Joao-Herculano.git
```

Entre na pasta do repositório.

```
cd DT-Neoway-Joao-Herculano
```

Crie o ambiente virtual para o projeto

```
python3 -m venv .venv && source .venv/bin/activate
```

Instale as dependências digitando:

```
python3 -m pip install -r requirements.txt
```

CRIANDO O BANCO DE DADOS 

Abra o MySql Workench ou o gerenciador de MySql que preferir

Execute o script sql do arquivo dt-neoway.sql que está na raiz da pasta do repositório

<img src="https://raw.githubusercontent.com/joaohsneto/DT-Neoway-Joao-Herculano/main/src/public/img_dt_neoway00.sql.jpg"/>

Será criado um banco de dados com a estrutura abaixo:

<img src="https://raw.githubusercontent.com/joaohsneto/DT-Neoway-Joao-Herculano/main/src/public/bd_structure_img.jpg"/>


EXECUTANDO:

Retorne a pasta do repositório DT-Neoway-Joao-Herculano e entre na pasta src

```
cd src
```

Execute o arquivo main.py

```
python3 main.py
```
<img src="https://raw.githubusercontent.com/joaohsneto/DT-Neoway-Joao-Herculano/main/src/public/script.gif"/>
