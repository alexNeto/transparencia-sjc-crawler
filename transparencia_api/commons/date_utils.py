import datetime
import time


def converte_mes(mes_texto):
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    for i, mes in enumerate(meses):
        if mes == mes_texto.lower():
            return i + 1
    return 0


def get_last_available_date():
    now = time.localtime()
    last = datetime.date(now.tm_year, now.tm_mon, 1) - datetime.timedelta(1)
    last_month = last.replace(day=1)
    return f"{last_month.month}/{last_month.year}"


def month_year(date=None):
    if date is None:
        return get_last_available_date()
    else:
        return date.replace('-', '/')
