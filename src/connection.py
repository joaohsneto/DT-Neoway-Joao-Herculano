import pymysql

# abrir conexáo
conn = pymysql.connect(
    host="localhost",
    port=3306,
    database="dt-neoway",
    user="root",
    password="",
    autocommit=True
)


def insert_data(cpf, name, score):
    # criar cursor
    cursor = conn.cursor()
    # inserir no banco
    sql = "INSERT INTO students(cpf, name, score) values (%s, %s, %s)"
    values = (cpf, name, score)
    cursor.execute(sql, values)


def close_connection():
    # fechar conexão
    conn.close()
