from process_game_state import ProcessGameState
import seaborn as sns
import matplotlib.pyplot as plt

# Instantiate the class with parquet file and boundary coordinates
process = ProcessGameState('game_state_frame_data.parquet', [(-1735, 250), (-2024, 398), (-2806, 742), (-2472, 1233), (-1565, 580)])

# Try to execute the data processing methods
try:
    process.filter_rows_in_boundary()  # This method checks whether each row falls within a provided boundary
    process.extract_weapon_classes()  # This method extracts the weapon classes from the inventory json column
except ValueError as e:  # Catch and print possible errors during data processing
    print(f"Error during data processing: {str(e)}")
    exit(1)  # Exit the script with an error status

# Check if entering via the boundary is a common strategy for Team2 on T side
common_strategy = process.team_strategy('Team2', 'T')  # This method checks the average strategy for the team
# Check if the returned result is a string, meaning there's no data available
if isinstance(common_strategy, str):
    print(common_strategy)
else:  # If not, it means we have a valid data
    print(f"Entering via the boundary is a common strategy for Team2 on T side: {common_strategy > 0.5}")

# Calculate the average timer for Team2 on T side to enter BombsiteB with at least 2 rifles or SMGs
average_timer = process.average_timer_with_weapons('Team2', 'T', 2, ['rifle', 'smg'])
# Check if the returned result is a string, meaning there's no data available
if isinstance(average_timer, str):
    print(average_timer)
else:  # If not, it means we have a valid data
    print(f"Average timer for Team2 on T side to enter BombsiteB with at least 2 rifles or SMGs: {average_timer}")

# Generate a heatmap for Team2 on CT side
heatmap_data = process.heatmap_coordinates('Team2', 'CT')
# Check if the returned result is a string, meaning there's no data available
if isinstance(heatmap_data, str):
    print(heatmap_data)
else:  # If not, it means we have a valid data
    sns.heatmap(heatmap_data, cmap='YlGnBu')  # Generate the heatmap using seaborn
    plt.title('Heatmap for Team2 on CT side')  # Add a title to the heatmap
    plt.show()  # Display the heatmap
