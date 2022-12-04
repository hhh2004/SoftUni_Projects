spell = input()
while True:
    command = input()
    if command == 'Abracadabra':
        break
    else:
        command = command.split(' ')
    if command[0] == 'Abjuration':
        spell = spell.upper()
        print(spell)
    elif command[0] == 'Necromancy':
        spell = spell.lower()
        print(spell)
    elif command[0] == 'Illusion':
        if -len(spell) <= int(command[1]) < len(spell):
            bob_the_builder = list(spell)
            bob_the_builder[int(command[1])] = command[2]
            spell = ''.join(bob_the_builder)
            print('Done!')
        else:
            print('The spell was too weak.')
    elif command[0] == 'Divination':
        spell = spell.replace(command[1], command[2])
        print(spell)
    elif command[0] == 'Alteration':
        spell = spell.replace(command[1], '')
        print(spell)
    else:
        print('The spell did not work!')

