# CounterStrike Game State Analysis

## Welcome to the CounterStrike Game State Analysis project! This project provides a Python class, ProcessGameState, that is capable of processing and analyzing CounterStrike game state data stored in a Parquet file.

## Background and Objective
Our objective is to provide actionable insights to our CounterStrike coaching staff regarding player strategies and behaviors in relation to a specific chokepoint or area of interest on the game map. We have developed a solution that is flexible, easy-to-use, and efficient, capable of handling similar requests for different sets of coordinates and games.

## Solution Overview
### We have designed a Python class, ProcessGameState, to address our objectives. This class:
Handles file ingestion and Extract, Transform, Load (ETL) of the data.
Determines whether each row (representing a player's game state per frame) falls within a provided boundary.
Extracts the weapon classes from the inventory JSON column.

## Design Considerations
We wanted the solution to be as efficient as possible in terms of runtime and to minimize dependencies outside of standard Python libraries. The only third-party libraries used are pandas for data manipulation, seaborn and matplotlib for data visualization, and shapely for geometric operations.

## Methodology
We utilized the data of player positions, weapon inventory, and other game state data to extract meaningful insights. Polygon-based geometric analysis was performed to determine if a player's position is within a specified boundary. We used this to analyze the strategy of the opponent team in terms of their movement and weapon choices.

## Usage

Clone this repository to your local machine.
Navigate to the repository's directory.
Run the analyze_data.py script to start the analysis.

This will:

Analyze whether entering via the specified boundary is a common strategy for Team2 on the Terrorist side.
Calculate the average timer that Team2 on the Terrorist side enters “BombsiteB” with at least 2 rifles or SMGs.
Create a heatmap showing where you suspect Team2 to be waiting inside “BombsiteB” on the Counter-Terrorist side.
The code can also be adapted to analyze different games, players, teams, or boundary conditions as needed.

To address the challenge of enabling non-technical stakeholders, such as the CS:GO coaching staff, to access and utilize the tool without requiring them to run code, we propose the implementation of a user-friendly web-based interface. This solution would empower the coaching staff to easily request and acquire the desired output themselves, enhancing their ability to analyze and strategize effectively.
The web-based interface would provide a simple and intuitive graphical user interface (GUI) where the coaching staff can input the necessary parameters and view the results in a visually appealing manner. By abstracting the underlying code and complexities, the interface allows users to interact with the tool seamlessly, without the need for technical knowledge or coding skills.

This solution can be implemented within a timeframe of less than one week. Leveraging modern web development frameworks and libraries, such as Flask, Django, or Streamlit, it is possible to rapidly create an interactive interface that connects to the existing codebase and presents the required functionalities to the coaching staff. Additionally, deploying the web application on a hosting platform, such as Heroku or AWS, ensures accessibility from any device with an internet connection.

By adopting this approach, the coaching staff can conveniently input their queries, select the desired parameters, and receive the output in a user-friendly format. This empowers them to make informed decisions and derive valuable insights from the CounterStrike data without relying on technical personnel for assistance, thereby streamlining their workflow and enhancing productivity.
