import requests
import json
from datetime import datetime, timedelta
import os
import random

# API configuration
API_KEY = "bb7663e6-e4bc-4efa-8193-95c21f3e2569"
HEADERS = {
    "Authorization": API_KEY,
    "Accept": "application/json"
}

def get_random_date():
    """Get a random date from the 2023-2024 NBA season."""
    # NBA 2023-2024 season dates
    season_start = datetime(2023, 10, 24)  # Regular season start
    season_end = datetime(2024, 4, 14)     # Regular season end
    
    # Calculate total days in season
    total_days = (season_end - season_start).days
    
    # Get random number of days to add to start date
    random_days = random.randint(0, total_days)
    
    # Calculate random date
    random_date = season_start + timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d')

def fetch_nba_games(date):
    """Fetch NBA games for a specific date."""
    url = "https://api.balldontlie.io/v1/games"
    params = {
        "dates[]": date,
        "seasons[]": "2023"  # Current season
    }
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def get_game_summaries(games_data):
    """Extract game summaries from games data."""
    game_summaries = []
    
    for game in games_data['data']:
        summary = {
            'game_id': game['id'],
            'date': game['date'],
            'home_team': {
                'name': game['home_team']['full_name'],
                'score': game['home_team_score']
            },
            'visitor_team': {
                'name': game['visitor_team']['full_name'],
                'score': game['visitor_team_score']
            },
            'status': game['status'],
            'season': game['season'],
            'period': game['period'],
            'time': game['time']
        }
        game_summaries.append(summary)
    
    return game_summaries

def save_to_json(data, filename):
    """Save data to a JSON file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    # Get a random date from the season
    random_date = get_random_date()
    print(f"Fetching games for date: {random_date}")
    
    try:
        # Fetch games for the random date
        games_data = fetch_nba_games(random_date)
        
        if not games_data['data']:
            print(f"No games found for {random_date}")
            print("Trying another random date...")
            return main()  # Recursively try another date
        
        # Get game summaries
        game_summaries = get_game_summaries(games_data)
        
        # Prepare output data
        output_data = {
            'date': random_date,
            'games': game_summaries,
            'execution_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Save to JSON file
        output_file = 'data/nba/game_summaries.json'
        save_to_json(output_data, output_file)
        print(f"Successfully saved game summaries to {output_file}")
        
        # Print game summaries
        print("\nGame Summaries:")
        for game in game_summaries:
            print(f"\n{game['home_team']['name']} vs {game['visitor_team']['name']}")
            print(f"Score: {game['home_team']['score']} - {game['visitor_team']['score']}")
            print(f"Status: {game['status']}")
            if game['status'] == 'Final':
                winner = game['home_team']['name'] if game['home_team']['score'] > game['visitor_team']['score'] else game['visitor_team']['name']
                print(f"Winner: {winner}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 