# CounterStrike Game State Analysis

Welcome to the CounterStrike Game State Analysis project! This project provides a Python class, ProcessGameState, that is capable of processing and analyzing CounterStrike game state data stored in a Parquet file.

Background and Objective
Our objective was to provide actionable insights to our CounterStrike coaching staff regarding player strategies and behaviors in relation to a specific chokepoint or area of interest on the game map. We developed a solution that is flexible, easy-to-use, and efficient, capable of handling similar requests for different sets of coordinates and games.

Solution Overview
We have designed a Python class, ProcessGameState, to address our objectives. This class:

Handles file ingestion and Extract, Transform, Load (ETL) of the data.
Determines whether each row (representing a player's game state per frame) falls within a provided boundary.
Extracts the weapon classes from the inventory JSON column.
Design Considerations
We wanted the solution to be as efficient as possible in terms of runtime and to minimize dependencies outside of standard Python libraries. The only third-party libraries used are pandas for data manipulation and shapely for geometric operations.

Methodology
We utilized the data of player positions, weapon inventory, and other game state data to extract meaningful insights. Polygon-based geometric analysis was performed to determine if a player's position is within a specified boundary. We used this to analyze the strategy of the opponent team in terms of their movement and weapon choices.
