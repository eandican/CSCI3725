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
        return np.random.choice(TRIP_SEASON)
    
    def get_destination(self, current_season):
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
        return np.random.choice(
            ACTIVITIES,
            p=[self.activity_matrix[destination][next_activity] for next_activity in ACTIVITIES]
        )
    
    def plan_trip(self):
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

    winter_season = Image.open("winter.jpg")
    summer_season = Image.open("summer.jpg")

    japan_flag = Image.open("japan.jpg")
    swiss_flag = Image.open("swiss.jpg")
    canada_flag = Image.open("canada.jpg")
    hawaii_flag = Image.open("hawaii.jpg")
    turks_flag = Image.open("turks.jpg")
    italy_flag = Image.open("italy.jpg")

    skiing = Image.open("skiing.jpg")
    surfing = Image.open("surfing.jpg")
    hiking = Image.open("hiking.jpg")
    dining = Image.open("dining.jpg")
    sightseeing = Image.open("sightseeing.jpg")
    beaching = Image.open("beaching.jpg")

    fig, ax = plt.subplots()
    x_values = np.arange(len(upcoming_trip))

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

    ax.set_xlim(-0.5, len(upcoming_trip) - 0.5)
    ax.set_ylim(-1, 1)
    ax.set_xticks(x_values)
    ax.set_xticklabels(upcoming_trip)
    ax.set_yticks([])
    ax.set_title("Emre's Next Trip")

    plt.show()

if __name__ == "__main__":
    main()


        
    
