import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image

DANCE_MOVES = [
    "whip",
    "nae nae",
    "dougie"
]

class TangoMaker:
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix

    def get_next_move(self, current_move):
        return np.random.choice(
            DANCE_MOVES,
            p=[self.transition_matrix[current_move][next_move] for next_move in DANCE_MOVES]
            )
    
    def dance_sequence(self, current_move="dougie", dance_length=5):
        sequence = []
        while len(sequence) < dance_length:
            next_move = self.get_next_move(current_move)
            sequence.append(next_move)
            current_move = next_move

        return sequence
    
def main ():
    tango_maker = TangoMaker({
        "whip" : {"whip" : 0.5, "nae nae" : 0.2, "dougie" : 0.3},
        "nae nae" : {"whip" : 0.1, "nae nae" : 0.1, "dougie" : 0.8},
        "dougie" : {"whip" : 0.3, "nae nae" : 0.6, "dougie" : 0.1}
    })

    new_dance = tango_maker.dance_sequence()
    print(new_dance)

    whip = Image.open("whip.jpg")

    fig, ax = plt.subplots()
    x_values = np.arange(len(new_dance))

    for i, move in enumerate(new_dance):
        if move == "whip":
            ax.imshow(whip, extent=[i - 0.3, i + 0.3, -0.5, 0.5])
        elif move == "nae nae":
            ax.imshow(whip, extent=[i - 0.3, i + 0.3, -0.5, 0.5])
        else:
            ax.imshow(whip, extent=[i - 0.3, i + 0.3, -0.5, 0.5])

    ax.set_xlim(-0.5, len(new_dance) - 0.5)
    ax.set_ylim(-1, 1)
    ax.set_xticks(x_values)
    ax.set_xticklabels(new_dance)
    ax.set_yticks([])
    ax.set_title("James & Emre's Choreographed Dance")

    plt.show()

if __name__ == "__main__":
    main()

