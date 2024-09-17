"""
Learning Objectives:
- Let's remmeber Python!
- What would a Markov chain look like in code?

Dependencies: numpy, scipy

To install (example): python -m pip install --user numpy scipy
"""

import numpy as np
from scipy.io.wavfile import write

SAMPLE_RATE = 44100

NOTE_FREQUENCIES = {
    'A' : 440.01,
    'B' : 493.89,
    'C' : 261.63
}

class MarkovMusician:

    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.notes = list(transition_matrix.keys())



    def get_next_note(self, current_note):
        """
          Decides which note to play next based on the current note.

          Args: current_note (str) - the current note that is being played.

        """
        return np.random.choice(
            self.notes,
            p=[self.transition_matrix[current_note][next_note] for next_note in self.notes]
          )

        """ 
          Example!
          np.random.choice(5, p=[0.1, 0, 0.3, 0.6, 0])

              5 => aray([0, 1, 2, 3, 4])
              p => probabilities of each of the elements in the array

        """



    def compose_melody(self, current_note="A", song_length=3):
        """
          Generate a sequence of notes!
        """
        melody = []
        
        while len(melody) < song_length: 
            next_note = self.get_next_note(current_note)
            melody.append(next_note)
            current_note = next_note

        return melody



    def get_wave(self, frequency=440, duration=0.3, max_amplitude=4096):
        time = np.linspace(0, duration, int(SAMPLE_RATE * duration))
        sound_wave = max_amplitude * np.sin(2 * np.pi * frequency * time)
        return sound_wave

    
    
    def get_sound_wave(self, melody):
        """ Transform the String melody into a list of sound waves """

        song = []

        for current_note in melody:
            sound_wave = self.get_wave(NOTE_FREQUENCIES[current_note])
            song.append(sound_wave)
        
        song = np.concatenate(song)

        print("Song is now: ", song)

        return song



    def write_sound_file(self, melody):
        """ Write out a collection of sound waves (a song!) to a file.
        """
        data = song.get_sound_wave_data(melody)
        write("new-hit-song.wav", SAMPLE_RATE, data.astype(np.int16))



def main():
    song_maker = MarkovMusician({
        'A' : {"A": 0.3, "B": 0.4, "C": 0.3},
        'B' : {"A": 0.7, "B": 0.2, "C": 0.1},
        'C' : {"A": 0.1, "B": 0.7, "C": 0.2}  
    })

    # print(song_maker.transition_matrix)
    # print(song_maker.notes)

    # print(song_maker.get_next_note("A"))

    # print(song_maker.compose_melody())

    new_song = song_maker.compose_melody(current_note = "c", song_length=10)
    print(new_song)

    song_maker.write_sound_file(new_song)

if __name__ == "__main__":
    main()