import sqlite3


def conexao_db():
    conn = sqlite3.connect('db.observatorio')
    cursor = conn.cursor()

    return [conn, cursor]


def get_noticias():
    conn, cursor = conexao_db()
    cursor.execute(f"""SELECT * FROM app_noticias;""")

    noticias = None

    list_noticias = []
    for linha in cursor.fetchall():
        noticias = {
            "id": linha[0],
            "titulo": linha[1],
            "url": linha[2],
            "resumo": linha[3],
            "imagem": linha[4],
            "data": linha[5],
            "publicar": linha[6],
            "autor_id": linha[7],
            "fonte": linha[8],
        }

        list_noticias.append(noticias)

    conn.close()

    if not list_noticias:
        return list_noticias

    return list_noticias


def get_pluviograma():
    conn, cursor = conexao_db()
    cursor.execute(f"""SELECT * FROM app_pluviograma;""")

    pluviograma = None

    list_pluviograma = []
    for linha in cursor.fetchall():
        pluviograma = {
            "id": linha[0],
            "titulo": linha[1],
            "data": linha[2],
            "publicar": linha[3],
            "autor_id": linha[4],
            "imagem_mini_post": linha[5],
            "fonte": linha[6],
        }

        list_pluviograma.append(pluviograma)

    conn.close()

    if not list_pluviograma:
        return list_pluviograma

    return list_pluviograma


def get_dashboard():
    conn, cursor = conexao_db()
    cursor.execute(f"""SELECT * FROM app_dashboard;""")

    dashboards = None

    list_dashboards = []
    for linha in cursor.fetchall():
        dashboards = {
            "id": linha[0],
            "titulo": linha[1],
            "data": linha[2],
            "publicar": linha[3],
            "autor_id": linha[4],
            "imagem_post": linha[5],
            "fonte": linha[6],
        }

        list_dashboards.append(dashboards)

    conn.close()

    if not list_dashboards:
        return list_dashboards

    return list_dashboards
