from melodia.core import Track
from melodia.music import chord
from melodia.io import midi
import melodia

#melodia.io.midi.dump()
track = Track(signature=(4, 4))

track.add(melodia.core.note.Note('A4', (1, 1), 0.6))

with open('chords.mid', 'wb') as f:
    midi.dump(track, f)


def genmelody(name, scale, length, usepatterns, ):
     print('Starting generation')

if __name__ == '__main__':
    print('Use standart parameters?')
    t = input()
    if t != 'Yes' and t != 'yes':
        print('Enter parameters:')
        print('Name is: ')
        name = input()
        print('Scale is: ')
        scale = input()
        print('Length is: ')
        length = input()
        print('Use patterns or not: ')
        usepatterns = input()
    else:
        name = 'New melody by EugeneBee MelodyGenerator'
        scale = 'Am'
        length = 8
        usepatterns = 'Yes'

    genmelody(name, scale, length, usepatterns)
    print('Melody is generated!')
