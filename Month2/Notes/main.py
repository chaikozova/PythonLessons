import ast

command = None
all_notes = None


def all_notes_update():
    with open('data.txt', 'r') as file:
        all_notes = ast.literal_eval(file.read())
    return all_notes


def time_input(current_day_notes, date, add=False):
    time = input('Input time: ')
    if add:
        if current_day_notes:
            if time in current_day_notes.keys():
                print(f'{date} in {time} you already have note {current_day_notes.get(time)}')
                return time_input(current_day_notes, date, add=True)
        return time
    if current_day_notes:
        if time not in current_day_notes.keys():
            print(f'{date} at {time} you dont have notes')
            return time_input(current_day_notes, date)
        print(f'{date} at {time} you have {current_day_notes.get(time)}')
    return time


def date_input(all_notes, add=False):
    date = input('Input date: ')
    current_day_notes = all_notes.get(date)
    if add:
        if current_day_notes:
            print(f'{date} => {current_day_notes}')
        return date
    if current_day_notes:
        print(f'on {date} => {current_day_notes}')
        return date
    else:
        print('You dont have notes on this day')
        print(f'Choose another day {all_notes.keys}')
        return date_input(all_notes, date)


def add_note():
    all_notes = all_notes_update()
    date = date_input(all_notes, add=True)
    current_day_notes = all_notes.get(date)
    time = time_input(current_day_notes, date, add=True)
    comment = input('Input comment: ')
    note = {time: comment} if current_day_notes else {date: {time: comment}}
    if current_day_notes:
        current_day_notes.update(note)
    else:
        all_notes.update(note)
    with open('data.txt', 'w') as file:
        file.writelines(str(all_notes))


def edit_note():
    all_notes = all_notes_update()
    date_old = date_input(all_notes)
    current_day_notes = all_notes.get(date_old)
    time_old = time_input(current_day_notes, date_old)
    q = input('If you want to change only comment - press 1\nIf you want to change the whole note - press 2\n')
    if q == '1':
        comment = input('Input comment: ')
        current_day_notes[time_old] = comment
        all_notes[date_old] = current_day_notes
        with open('data.txt', 'w') as file:
            file.writelines(str(all_notes))
    if q == '2':
        date = date_input(all_notes, add=True)
        time = time_input(all_notes.get(date), date, add=True)
        comment = input('Input comment: ')
        note = {time: comment} if all_notes.get(date) else {date: {time: comment}}
        if all_notes.get(date):
            all_notes.get(date).update(note)
        else:
            all_notes.update(note)
        with open('data.txt', 'w') as file:
            file.writelines(str(all_notes))
        current_day_notes.pop(time_old)
        all_notes[date_old] = current_day_notes
        with open('data.txt', 'w') as file:
            file.writelines(str(all_notes))


def delete_note():
    all_notes = all_notes_update()
    date = date_input(all_notes)
    current_day_notes = all_notes.get(date)
    time = time_input(current_day_notes, date)
    print('Now this note has been deleted')
    current_day_notes.pop(time)
    if not current_day_notes:
        all_notes.pop(date)
    else:
        all_notes[date] = current_day_notes
    with open('data.txt', 'w') as file:
        file.writelines(str(all_notes))


def show_all_notes():
    with open('data.txt', 'r') as file:
        all_notes = ast.literal_eval(file.read())
    for key in all_notes.keys():
        print('**********')
        print(f'{key}:')
        print('**********')
        for k in all_notes.get(key).keys():
            print(f'{k}: {all_notes.get(key).get(k)}')


def show_one_day_notes():
    all_notes = all_notes_update()
    date = date_input(all_notes)
    with open('data.txt', 'r') as file:
        all_notes = ast.literal_eval(file.read())
    if all_notes.get(date):
        for key in all_notes.get(date).keys():
            print(f'{key}: {all_notes.get(date).get(key)}')


def print_menu():
    print('------------------------')
    print('1. Add new Note')
    print('2. Edit Note')
    print('3. Delete Notes')
    print('4. Show All Notes')
    print('5. Show Notes in 1 day')
    print('6. Exit')
    print('------------------------')


while command != '6':
    print_menu()
    command = input('Choose one command: ')
    if command == '1':
        add_note()

    elif command == '2':
        edit_note()

    elif command == '3':
        delete_note()

    elif command == '4':
        show_all_notes()

    elif command == '5':
        show_one_day_notes()
    elif command == '6':
        print('Bye bye 👋🏻')
    else:
        print('Wrong command')

