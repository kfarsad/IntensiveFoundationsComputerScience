import os

LEADERBOARD_FILE = "leaderboard.txt"

class LeaderboardData:
    @staticmethod
    def load_leaderboard():
        """Load the leaderboard from a file."""
        if not os.path.exists(LEADERBOARD_FILE):
            return []
        with open(LEADERBOARD_FILE, "r") as file:
            try:
                entries = [line.strip().split(": ") for line in file]
                return sorted([(int(score), name) for score, name in entries], key=lambda x: x[0])
            except Exception as e:
                print(f"Error loading leaderboard: {e}")
                return []

    @staticmethod
    def save_leaderboard(entries):
        """Save the leaderboard to a file."""
        with open(LEADERBOARD_FILE, "w") as file:
            for score, name in entries:
                file.write(f"{score}: {name}\n")

    @staticmethod
    def update_leaderboard(name, score):
        """Add or update a player's score in the leaderboard."""
        entries = LeaderboardData.load_leaderboard()
        updated = False

        for i, (existing_score, existing_name) in enumerate(entries):
            if existing_name == name:
                if score < existing_score:
                    entries[i] = (score, name)
                updated = True
                break

        if not updated:
            entries.append((score, name))

        return sorted(entries, key=lambda x: x[0])
