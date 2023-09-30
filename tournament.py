# Simulate a sports tournament

from collections import defaultdict
import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # Read teams into memory from file
    with open(sys.argv[1], newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # print(row["team"], row["rating"])
            teams.append(row)

    # Convert ratings to ints
    for i in teams:
        i["rating"] = int(i["rating"])

    """TESTING"""
    # print(f"Teams:\n{teams}")

    counts = defaultdict(int)

    # Simulate N tournaments and keep track of win counts
    for _ in range(0, N):
        winner = simulate_tournament(teams)
        counts[winner] += 1

    """TESTING"""
    # print(f"Counts:\n{counts}")

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    round_num = 0
    winners = None
    champion = None

    while True:
        if round_num == 0:
            winners = simulate_round(teams)
            round_num += 1
        else:
            if len(winners) != 1:
                winners = simulate_round(winners)
                round_num += 1
            else:
                champion = winners[0]["team"]
                break

    return champion


if __name__ == "__main__":
    main()
