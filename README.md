# CounterStrike Game State Analysis
## Welcome to the CounterStrike Game State Analysis project!
This project provides a Python class, ProcessGameState, that is capable of processing and analyzing CounterStrike game state data stored in a Parquet file. With a few lines of code, I can extract meaningful insights into player strategies, helping our coaching staff to optimize their approach to the game.

## Background and Objective
Our objective is to provide actionable insights to our CounterStrike coaching staff regarding player strategies and behaviors in relation to specific areas of interest on the game map. I designed a solution that is flexible, easy-to-use, and efficient, capable of handling similar requests for different sets of coordinates and games.

## Solution Overview
### The Python class, ProcessGameState, serves as the main component of our solution. This class:

Handles file ingestion and performs Extract, Transform, Load (ETL) operations on the data.
Determines whether each row (representing a player's game state per frame) falls within a provided boundary.
Extracts the weapon classes from the inventory JSON column.
Design Considerations
I aimed to design a solution with optimal runtime efficiency and minimal dependencies on non-standard Python libraries. We used pandas for data manipulation, seaborn and matplotlib for data visualization, and shapely for geometric operations.

## Methodology
I used the game data, including player positions, weapon inventory, and other state data, to gain insights into players' strategies. Using polygon-based geometric analysis, I determined whether a player's position is within a specified boundary. We then analyzed the strategy of the opponent team based on their movement patterns and weapon choices.

# Usage and Results
To use this solution:

Clone this repository to your local machine.
Navigate to the repository's directory.
Run the analyze_data.py script to start the analysis.
This script will:

## Analyze whether entering via the specified boundary is a common strategy for Team2 on the Terrorist side.

From my analysis, entering via the boundary is not a common strategy for Team2 on the Terrorist side. 

## Calculate the average timer that Team2 on the Terrorist side enters “BombsiteB” with at least 2 rifles or SMGs.

According to my analysis, the average time taken for Team2, when playing on the Terrorist side, to enter "BombsiteB" with at least 2 rifles or SMGs is approximately 40.20 seconds. 

## Create a heatmap showing where you suspect Team2 to be waiting inside “BombsiteB” on the Counter-Terrorist side.

The generated heatmap shows a dark blue spot at x (356.3) and y (-1763.3,-1715.2), indicating the location where Team2 is most likely waiting.

This code can be adapted to analyze different games, players, teams, or boundary conditions as needed.

![Figure_1 (1)](https://github.com/prathor2/Intern-Assesment-EG/assets/123683540/6d7c164f-91da-40f7-a958-c189d11205a0)
<img width="852" alt="Screen Shot 2023-05-29 at 11 31 10 PM" src="https://github.com/prathor2/Intern-Assesment-EG/assets/123683540/e5b0c655-0c80-4b0d-be87-e7ff49b7114d">


## Proposed Solution for Non-Tech Stakeholders
I understand that non-technical stakeholders, such as our CS:GO coaching staff, may find it challenging to run the code. To make this solution more accessible, I propose developing a user-friendly web-based interface. This interface would allow our coaching staff to easily upload the game state data and specify the boundary coordinates.

After processing the data, the interface would present the findings in an easy-to-understand format. This includes a statement of whether entering via the boundary is a common strategy, the average timer for entering a location with specified weapons, and a heatmap indicating suspected player positions.

We estimate that this interface could be developed in less than one week, utilizing modern web development frameworks like Flask or Django for the back-end, and Bootstrap or React for the front-end. This solution would empower our coaching staff to gain insights from the game state data directly, enhancing their ability to make informed decisions and strategic plans.
