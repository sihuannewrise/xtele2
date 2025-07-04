import argparse

MURZIK = '=^..^=______/'
BOLT = '8==>'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Вежливый скрипт')
    parser.add_argument('name', help='Имя')
    parser.add_argument('-s', '--surname', help='Фамилия')
    parser.add_argument(
        '-c',
        '--city',
        help='Город',
        choices=['Chekhov', 'Dublin', 'Minsk', 'Simbirsk'],
    )
    parser.add_argument(
        '-m',
        '--murzik',
        action='store_true',
        help=f'Отправить кота Мурзика {MURZIK}'
    )
    parser.add_argument(
        '-b',
        '--bolt',
        action='store_false',
        help=f'Отправить болт {BOLT}'
    )
    args = parser.parse_args()

    parts = []
    parts.append(f'Hello, {args.name}')
    if args.surname is not None:
        parts.append(args.surname)
    if args.city is not None:
        parts.append(f'from {args.city}')
    if args.murzik:
        parts.append(MURZIK)
    if args.bolt:
        parts.append(BOLT)
    print(*parts)
