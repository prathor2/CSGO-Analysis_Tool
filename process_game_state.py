import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from shapely.geometry import Polygon, Point

class ProcessGameState:
    def __init__(self, parquet_file, boundary_vertices):
        # Loading data from parquet file
        self.data = pd.read_parquet(parquet_file)

        # Creating a polygon from boundary vertices
        self.polygon = Polygon(boundary_vertices)

    def filter_rows_in_boundary(self):
        """Assigns True or False to each row depending on whether the point is within the boundary"""
        xy_coords = list(zip(self.data['x'], self.data['y']))
        self.data['in_boundary'] = [self.polygon.contains(Point(point)) for point in xy_coords]

    def extract_weapon_classes(self):
        """Extracts weapon classes from the inventory column and adds it as a new column"""
        # Check if 'inventory' column is in DataFrame
        if 'inventory' not in self.data.columns:
            raise ValueError("Missing 'inventory' column in DataFrame")

        def extract_classes(inventory_json):
            """Extracts classes from inventory json"""
            try:
                return [item['class'] for item in json.loads(inventory_json).values()]
            except (json.JSONDecodeError, KeyError):
                return []

        self.data['weapon_classes'] = self.data['inventory'].apply(extract_classes)

    def team_strategy(self, team, side):
        """Calculates the mean of in_boundary values for the given team and side"""
        team_data = self.data[(self.data['team'] == team) & (self.data['side'] == side)]

        # Check if DataFrame is empty
        if team_data.empty:
            return "No data available for the given team and side"

        return team_data['in_boundary'].mean()

    def average_timer_with_weapons(self, team, side, min_weapons, weapon_types):
        """Calculates the average timer for the given team and side with at least min_weapons of weapon_types"""
        team_data = self.data[(self.data['team'] == team) & (self.data['side'] == side)]
        team_data['weapon_count'] = team_data['weapon_classes'].apply(lambda x: sum([weapon in x for weapon in weapon_types]))
        filtered_data = team_data[team_data['weapon_count'] >= min_weapons]

        # Check if DataFrame is empty
        if filtered_data.empty:
            return "No data available for the given conditions"

        return filtered_data['seconds'].mean()

    def heatmap_coordinates(self, team, side):
        """Generates a heatmap of coordinates for the given team and side"""
        team_data = self.data[(self.data['team'] == team) & (self.data['side'] == side) & (self.data['in_boundary'])]
        
        # Check if DataFrame is empty
        if team_data.empty:
            return "No data available for the given team and side"

        bins = 10  
        heatmap_data = team_data.groupby([pd.cut(team_data["x"], bins), pd.cut(team_data["y"], bins)]).size().unstack()
        return heatmap_data
