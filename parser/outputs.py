import csv
import logging
import datetime as dt

from prettytable import PrettyTable
from constants import BASE_DIR, DATETIME_FORMAT, DEST_RESULT_FOLDER


def control_output(results, cli_args):
    output = cli_args.output
    if output == 'pretty':
        pretty_output(results)
    elif output == 'file':
        file_output(results, cli_args)
    else:
        default_output(results)

def default_output(results):
    for row in results:
        print(*row)

def pretty_output(results):
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)

def file_output(results, cli_args):
    results_dir = BASE_DIR / DEST_RESULT_FOLDER
    results_dir.mkdir(exist_ok=True)
    parser_mode = cli_args.mode
    now = dt.datetime.now()
    # Сохраняем текущие дату-время в указанном формате.
    # Результат будет выглядеть вот так: 2021-06-18_07-40-41.
    now_formatted = now.strftime(DATETIME_FORMAT)
    # Собираем имя файла из полученных переменных:
    # «режим работы программы» + «дата и время записи» + формат (.csv).
    file_name = f'{parser_mode}_{now_formatted}.csv'
    file_path = results_dir / file_name

    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='unix')
        writer.writerows(results)
    logging.info(f'Файл с результатами был сохранён: {file_path}')
