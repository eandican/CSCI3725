"""
Name: Emre Andican
Class: CSCI 3725
Project Name: TripAdvisor
Description: This is a system that randomly selects one of two seasons (Winter or Summer), then chooses a destination 
based on the probaility of me visiting (given financial and time constraints), and then chooses an activity to focus on
during a trip to this place (probailties are decided on the most common activities within this spot). I utilize
Matplotlib and Pillow to help visualize this to statisfy the visual arts component of this task :).
"""
import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image

TRIP_SEASON = [
    "Winter",
    "Summer"
]

WINTER_DESTINATION = [
    "Japan",
    "Zermatt",
    "Whistler"
]

SUMMER_DESTINATION = [
    "Maui",
    "Turks & Caicos",
    "Lake Como"
]

ACTIVITIES = [
    "Skiing",
    "Surfing",
    "Hiking",
    "Dining",
    "Sightseeing",
    "Beaching"
]

class TripAdvisor:
    def __init__(self, destination_matrix, activity_matrix):
        self.destination_matrix = destination_matrix
        self.activity_matrix = activity_matrix

    def get_season(self):
        """
          Decides whether my yearly trip will be a winter or summer vacation 

          Return: 1 of 2 seasons within TRIP_SEASON (Winter or Summer)

        """
        return np.random.choice(TRIP_SEASON)
    
    def get_destination(self, current_season):
        """
          Decides where I will go on vacation based on the season

          Args: current_season (str) - the season of the vacation

          Return: a destination which is ultimately decided based on probabilites of my ability to visit
          through a transition matrix

        """
        if current_season == "Winter":
            return np.random.choice(
                WINTER_DESTINATION,
                p=[self.destination_matrix[current_season][destination] for destination in WINTER_DESTINATION]
            )
        
        elif current_season == "Summer":
            return np.random.choice(
                SUMMER_DESTINATION,
                p=[self.destination_matrix[current_season][destination] for destination in SUMMER_DESTINATION]
            )
        
    def get_activities(self, destination):
        """
          Decides what I will do based on the location of my planned vacation

          Args: destination (str) - where I will be going

          Return: an activity which is ultimately decided based on the popularity of activities within this location/
          accessbility of these activites through a transition matrix

        """
        return np.random.choice(
            ACTIVITIES,
            p=[self.activity_matrix[destination][next_activity] for next_activity in ACTIVITIES]
        )
    
    def plan_trip(self):
        """ 
        Calls all of the above functions, starting with trip season, and creating a list that contains
        the season, location, and main activity of this trip

        Return: our trip in list form.
         
        """

        trip = []
    
        season = self.get_season()
        trip.append(season)
        
        destination = self.get_destination(season)
        trip.append(destination)

        activities = self.get_activities(destination)
        trip.append(activities)

        return trip
    
def main():
    trip_adivsor = TripAdvisor({
        "Winter" : {"Japan" : 0.1, "Zermatt": 0.3, "Whistler": 0.6},
        "Summer" : {"Maui" : 0.3, "Turks & Caicos" : 0.4, "Lake Como" : 0.3}
    },
    { 
        "Japan" : {"Skiing" : 0.4, "Surfing" : 0.0, "Hiking": 0.2, "Dining" : 0.2, "Sightseeing" : 0.2, "Beaching" : 0.0},
        "Zermatt" : {"Skiing" : 0.6, "Surfing" : 0.0, "Hiking": 0.2, "Dining" : 0.1, "Sightseeing" : 0.1, "Beaching" : 0.0},
        "Whistler" : {"Skiing" : 0.6, "Surfing" : 0.0, "Hiking": 0.3, "Dining" : 0.1, "Sightseeing" : 0.0, "Beaching" : 0.0},
        "Maui" : {"Skiing" : 0.0, "Surfing" : 0.4, "Hiking": 0.2, "Dining" : 0.0, "Sightseeing" : 0.1, "Beaching" : 0.3},
        "Turks & Caicos" : {"Skiing" : 0.0, "Surfing" : 0.3, "Hiking": 0.0, "Dining" : 0.2, "Sightseeing" : 0.1, "Beaching" : 0.4},
        "Lake Como" : {"Skiing" : 0.0, "Surfing" : 0.0, "Hiking": 0.0, "Dining" : 0.5, "Sightseeing" : 0.3, "Beaching" : 0.2}
    })

    upcoming_trip = trip_adivsor.plan_trip()
    print(upcoming_trip)

    # Variables for our images

    winter_season = Image.open("Assets/winter.jpg")
    summer_season = Image.open("Assets/summer.jpg")

    japan_flag = Image.open("Assets/japan.jpg")
    swiss_flag = Image.open("Assets/swiss.jpg")
    canada_flag = Image.open("Assets/canada.jpg")
    hawaii_flag = Image.open("Assets/hawaii.jpg")
    turks_flag = Image.open("Assets/turks.jpg")
    italy_flag = Image.open("Assets/italy.jpg")

    skiing = Image.open("Assets/skiing.jpg")
    surfing = Image.open("Assets/surfing.jpg")
    hiking = Image.open("Assets/hiking.jpg")
    dining = Image.open("Assets/dining.jpg")
    sightseeing = Image.open("Assets/sightseeing.jpg")
    beaching = Image.open("Assets/beaching.jpg")

    fig, ax = plt.subplots()
    x_values = np.arange(len(upcoming_trip))

    # Decides what image to present based on the value

    for i, x in enumerate(upcoming_trip):
        if x == "Winter":
            ax.imshow(winter_season, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Summer":
            ax.imshow(summer_season, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Japan":
            ax.imshow(japan_flag, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Zermatt":
            ax.imshow(swiss_flag, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Whistler":
            ax.imshow(canada_flag, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Maui":
            ax.imshow(hawaii_flag, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Turks & Caicos":
            ax.imshow(turks_flag, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Lake Como":
            ax.imshow(italy_flag, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Skiing":
            ax.imshow(skiing, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Surfing":
            ax.imshow(surfing, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Hiking":
            ax.imshow(hiking, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Dining":
            ax.imshow(dining, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Sightseeing":
            ax.imshow(sightseeing, extent=[i - 0.5, i + 0.5, -0.5, 0.5])
        elif x == "Beaching":
            ax.imshow(beaching, extent=[i - 0.5, i + 0.5, -0.5, 0.5])

    # Creates plot space / graph
            
    ax.set_xlim(-0.5, len(upcoming_trip) - 0.5)
    ax.set_ylim(-1, 1)
    ax.set_xticks(x_values)
    ax.set_xticklabels(upcoming_trip)
    ax.set_yticks([])
    ax.set_title("Emre's Next Trip")

    # Helps remove gridlines

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.show()

if __name__ == "__main__":
    main()
