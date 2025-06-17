# NBA Historical Games Explorer

This project fetches and analyzes random historical NBA games using the Ball Don't Lie API. It provides insights into past NBA games, their scores, and outcomes.

## Features

- Fetches random historical NBA games from the 2023-2024 season
- Provides detailed game summaries including:
  - Teams playing
  - Final scores
  - Game status
  - Winner information
  - Game time and period details
- Saves game data in JSON format for further analysis

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sports_insights.git
cd sports_insights
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script to fetch a random historical NBA game:
```bash
python src/fetch_nba_data.py
```

The script will:
1. Select a random date from the 2023-2024 NBA season
2. Fetch game data for that date
3. Display a summary of the games played
4. Save the data to `data/nba/game_summaries.json`

## Data Structure

The saved JSON file contains:
- Date of the games
- List of games played on that date
- For each game:
  - Teams involved
  - Final scores
  - Game status
  - Season information
  - Game time and period details

## Dependencies

- Python 3.8+
  
## License

MIT License
