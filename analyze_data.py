from process_game_state import ProcessGameState
import seaborn as sns
import matplotlib.pyplot as plt

# Instantiate class with parquet file and boundary coordinates
process = ProcessGameState('game_state_frame_data.parquet', [(-1735, 250), (-2024, 398), (-2806, 742), (-2472, 1233), (-1565, 580)])

# Handle file ingestion and ETL
process.filter_rows_in_boundary()
process.extract_weapon_classes()

# Check if entering via the boundary is a common strategy for Team2 on T side
common_strategy = process.team_strategy('Team2', 'T') > 0.5
print(f"Entering via the boundary is a common strategy for Team2 on T side: {common_strategy}")

# Get the average timer for Team2 on T side to enter BombsiteB with at least 2 rifles or SMGs
average_timer = process.average_timer_with_weapons('Team2', 'T', 2, ['rifle', 'smg'])
print(f"Average timer for Team2 on T side to enter BombsiteB with at least 2 rifles or SMGs: {average_timer}")

# Create a heatmap for Team2 on CT side
heatmap_data = process.heatmap_coordinates('Team2', 'CT')
sns.heatmap(heatmap_data, cmap='YlGnBu')
plt.title('Heatmap for Team2 on CT side')
plt.show()
