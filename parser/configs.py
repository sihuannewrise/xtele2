import argparse
import logging

from logging.handlers import RotatingFileHandler
from constants import BASE_DIR, DEST_LOGS_FOLDER, LOG_FILE_NAME, DATETIME_FORMAT, LOG_FORMAT


def configure_argument_parser(available_modes):
    parser = argparse.ArgumentParser(description='Парсер документации Python')
    parser.add_argument(
        'mode',
        choices=available_modes,
        help='Режимы работы парсера'
    )
    parser.add_argument(
        '-c',
        '--clear-cache',
        action='store_true',
        help='Очистка кеша'
    )
    parser.add_argument(
        '-o',
        '--output',
        choices=('pretty', 'file'),
        help='Дополнительные способы вывода данных'
    )
    return parser

def configure_logging():
    log_dir = BASE_DIR / DEST_LOGS_FOLDER
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / LOG_FILE_NAME

    rotating_handler = RotatingFileHandler(
        log_file,
        maxBytes=10 ** 6,
        backupCount=5,
        encoding='utf-8',
    )
    logging.basicConfig(
        datefmt=DATETIME_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler())
    )
