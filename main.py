# imports

from melodia.core import Track
from melodia.core import Tone
#from melodia.music import chord
from melodia.io import midi
import melodia
import random as r


# melodia

# melodia.io.midi.dump()
track = Track(signature=(4, 4))

#track.add(melodia.core.note.Note('A4', (1, 1), 0.6))

#with open('chords.mid', 'wb') as f:
#    midi.dump(track, f)


# variables

cleanscales = ['Cj', 'Am', 0]  # Clean C major and A minor
# Cj means C major
# Am means A minor
# Small b means flat
# # means sharp

# 0 is flat
# 1 is nothing
# 2 is sharp

scales = [['Cj',  'Am',  1, 1, 1, 1, 1, 1, 1],  # Scales
          ['Gj',  'Em',  1, 1, 1, 2, 1, 1, 1],  # Sharp scales
          ['Dj',  'Bm',  2, 1, 1, 2, 1, 1, 1],
          ['Aj',  'F#m', 2, 1, 1, 2, 2, 1, 1],
          ['Ej',  'C#m', 2, 2, 1, 2, 2, 1, 1],
          ['Bj',  'G#m', 2, 2, 1, 2, 2, 2, 1],
          ['F#j', 'D#m', 2, 2, 2, 2, 2, 2, 1],
          ['C#j', 'A#m', 2, 2, 2, 2, 2, 2, 2],
          ['Fj',  'Dm',  1, 1, 1, 1, 1, 1, 0],  # Flat scales
          ['Bbj', 'Gm',  1, 1, 0, 1, 1, 1, 0],
          ['Ebj', 'Cm',  1, 1, 0, 1, 1, 0, 0],
          ['Abj', 'Fm',  1, 0, 0, 1, 1, 0, 0],
          ['Dbj', 'Bbm', 1, 0, 0, 1, 0, 0, 0],
          ['Gbj', 'Ebm', 0, 0, 0, 1, 0, 0, 0],
          ['Cbj', 'Abm', 0, 0, 0, 0, 0, 0, 0]]

# до ре ми фа соль ля си
keys = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
keysstr = 'CDEFGAB'


# functions

def genmelody(scale, length, usepatterns):
    print('Starting generation')
    key = Tone.from_notation(scale[:-1] + '3').pitch
    workingscale = scales[0]
    for i in range(15):
        if scale == scales[i][0] or scale == scales[i][1]:
            workingscale = scales[i]
    if (usepatterns == 'Yes' or usepatterns == 'yes') and length % 8 != 0:
        print('Error! Length should be divisible by 8 if you want to use patterns.')
        return 0

    elif usepatterns == 'Yes' or usepatterns == 'yes':
        print("patterns")
        track.add(melodia.core.note.Note(key, (1, 4)))
        track.add(melodia.core.note.Note(key-4, (1, 4)))
        track.add(melodia.core.note.Note(key, (1, 4)))
        track.add(melodia.core.note.Note(key-4, (1, 4)))
        for i in range(int(length/8) - 1):
            workingscale = scales[0]
            ns = ''
            for j in range(4):
                n = r.randint(0, 6)
                if workingscale[2 + n] == 0:
                    ns = chr(n + ord('A')) + 'b' + str(3)
                elif workingscale[2 + n] == 1:
                    ns = chr(n + ord('A')) + str(3)
                else:
                    ns = chr(n + ord('A')) + '#' + str(3)
                track.add(melodia.core.note.Note(ns, (1, 4)))
            track.add(melodia.core.note.Note(Tone.from_notation(ns).pitch-4, (1, 4)))
            track.add(melodia.core.note.Note(Tone.from_notation(ns).pitch, (1, 4)))
            track.add(melodia.core.note.Note(Tone.from_notation(ns).pitch-4, (1, 4)))
            track.add(melodia.core.note.Note(Tone.from_notation(ns).pitch, (1, 4)))
        for j in range(4):
            n = r.randint(0, 6)
            o = r.randint(0, 1)  # Notes could be generated between 2 octaves so that the melody will sound better
            if workingscale[2 + n] == 0:
                ns = chr(n + ord('A')) + 'b' + str(3 + o)
            elif workingscale[2 + n] == 1:
                ns = chr(n + ord('A')) + str(3 + o)
            else:
                ns = chr(n + ord('A')) + '#' + str(3 + o)
            track.add(melodia.core.note.Note(ns, (1, 4)))

    else:
        track.add(melodia.core.note.Note(key, (1, 4)))
        for i in range(length-1):
            n = r.randint(0, 6)
            o = r.randint(0, 1)  # Notes could be generated between 2 octaves so that the melody will sound better
            if workingscale[2 + n] == 0:
                ns = chr(n+ord('A')) + 'b' + str(3+o)
            elif workingscale[2 + n] == 1:
                ns = chr(n+ord('A')) + str(3+o)
            else:
                ns = chr(n+ord('A')) + '#' + str(3+o)
            track.add(melodia.core.note.Note(ns, (1, 4)))
    print('Melody is generated!')


# main

if __name__ == '__main__':
    print('Use standard parameters?')
    t = input()
    if t != 'Yes' and t != 'yes':
        print('Enter parameters:')
        print('Name is: ')
        name = input()
        print('Scale is: ')  # Major is written as j
        scale = input()
        print('Length is: ')
        length = int(input())  # Amount of notes in the melody
        print('Use patterns or not: ')  # Length should be divisible by 8 if you want to use patterns
        usepatterns = input()
    else:
        name = 'Melody by MelodyGenerator'
        scale = 'Am'
        length = 8
        usepatterns = 'No'

    genmelody(scale, length, usepatterns)

    with open(name + '.mid', 'wb') as f:
        midi.dump(track, f)
