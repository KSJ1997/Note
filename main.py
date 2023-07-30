import json
import argparse
from note import add_note, read_notes, edit_note, delete_note

def main():
    parser = argparse.ArgumentParser(description='Консольное приложение заметки')
    parser.add_argument('command', choices=['add', 'read', 'edit', 'delete'], help='Команда: add, read, edit, delete')
    parser.add_argument('--title', help='Заголовок заметки')
    parser.add_argument('--msg', help='Тело заметки')
    parser.add_argument('--id', type=int, help='Идентификатор заметки для edit и delete команд')
    parser.add_argument('--date', help='Дата для фильтрации списка заметок (формат: ГГГГ-ММ-ДД)')

    args = parser.parse_args()

    if args.command == 'add':
        if not args.title or not args.msg:
            print('Ошибка: Необходимо указать заголовок (--title) и тело (--msg) заметки.')
        else:
            add_note(args.title, args.msg)
    elif args.command == 'read':
        notes = read_notes(args.date)
        if notes:
            print(json.dumps(notes, indent=4))
        else:
            print('Нет заметок.')
    elif args.command == 'edit':
        if not args.id or not args.title or not args.msg:
            print('Ошибка: Необходимо указать идентификатор (--id), заголовок (--title) и тело (--msg) заметки.')
        else:
            edit_note(args.id, args.title, args.msg)
    elif args.command == 'delete':
        if not args.id:
            print('Ошибка: Необходимо указать идентификатор (--id) заметки для удаления.')
        else:
            delete_note(args.id)
    else:
        print('Ошибка: Неизвестная команда.')

if __name__ == "__main__":
    main()