def converte_mes(mes_texto):
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    for i, mes in enumerate(meses):
        if mes == mes_texto.lower():
            return i + 1
    return 0
