import pandas as pd
import json
from shapely.geometry import Polygon, Point

class ProcessGameState:
    def __init__(self, parquet_file, boundary_vertices):
        self.data = pd.read_parquet(parquet_file)
        self.polygon = Polygon(boundary_vertices)

    def filter_rows_in_boundary(self):
        xy_coords = list(zip(self.data['x'], self.data['y']))
        self.data['in_boundary'] = [self.polygon.contains(Point(p)) for p in xy_coords]

    def extract_weapon_classes(self):
        self.data['weapon_classes'] = self.data['inventory'].apply(lambda x: [i['class'] for i in json.loads(x).values()])

    def team_strategy(self, team, side):
        team_data = self.data[(self.data['team'] == team) & (self.data['side'] == side)]
        return team_data['in_boundary'].mean()

    def average_timer_with_weapons(self, team, side, min_weapons, weapon_types):
        team_data = self.data[(self.data['team'] == team) & (self.data['side'] == side)]
        team_data['weapon_count'] = team_data['weapon_classes'].apply(lambda x: sum([weapon in x for weapon in weapon_types]))
        return team_data[team_data['weapon_count'] >= min_weapons]['seconds'].mean()
