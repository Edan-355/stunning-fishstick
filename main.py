# @author = Edan
# @class = AP CSP "Learning API with Python!"
# March Madness Bracket Simulator (FINAL VERSION)

import sys
import json
import random
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError


def get_teams():
    """
    Backup data (acts like API response to avoid errors)
    """
    return {
        "data": [
            {"full_name": "Alabama"},
            {"full_name": "Michigan"},
            {"full_name": "Texas"},
            {"full_name": "Prude"},
            {"full_name": "Duke"},
            {"full_name": "St.Johns"},
            {"full_name": "Arizona"},
            {"full_name": "Arkansas"}
        ]
    }


def assign_seeds(teams):
    """
    Assign seeds 1–8
    """
    selected = teams[:8]
    seeds = {}

    for i, team in enumerate(selected):
        seeds[i + 1] = team["full_name"]

    return seeds


def simulate_game(seed1, team1, seed2, team2):
    """
    Simulate a game with upset logic
    """
    score1 = random.randint(60, 100) + (9 - seed1)
    score2 = random.randint(60, 100) + (9 - seed2)

    if score1 > score2:
        winner = (seed1, team1)
    else:
        winner = (seed2, team2)

    print(f"{seed1}. {team1} ({score1}) vs {seed2}. {team2} ({score2}) -> Winner: {winner[1]}")
    return winner


def simulate_round(matchups, round_name):
    """
    Simulate a round of games
    """
    print(f"\n🏀 {round_name} 🏀\n")
    winners = []

    for seed1, team1, seed2, team2 in matchups:
        winner = simulate_game(seed1, team1, seed2, team2)
        winners.append(winner)

    return winners


def create_matchups(seeds):
    """
    Create real March Madness matchups
    """
    return [
        (1, seeds[1], 8, seeds[8]),
        (4, seeds[4], 5, seeds[5]),
        (2, seeds[2], 7, seeds[7]),
        (3, seeds[3], 6, seeds[6]),
    ]


def main():
    print("🏀 March Madness Simulator (Final)")
    print(f"Python version: {sys.version.split()[0]}")

    try:
        data = get_teams()
        teams_data = data.get("data", [])

        seeds = assign_seeds(teams_data)

        print("\n🎯 TOURNAMENT SEEDS:")
        for seed, team in seeds.items():
            print(f"{seed}. {team}")

        # ROUND 1
        matchups = create_matchups(seeds)
        winners = simulate_round(matchups, "Quarterfinals")

        # FINAL FOUR
        matchups2 = [
            (winners[0][0], winners[0][1], winners[1][0], winners[1][1]),
            (winners[2][0], winners[2][1], winners[3][0], winners[3][1]),
        ]
        winners2 = simulate_round(matchups2, "Final Four")

        # CHAMPIONSHIP
        final_match = [
            (winners2[0][0], winners2[0][1], winners2[1][0], winners2[1][1])
        ]
        champion = simulate_round(final_match, "Championship")

        print(f"\n🏆 NATIONAL CHAMPION: {champion[0][1]} 🏆")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
