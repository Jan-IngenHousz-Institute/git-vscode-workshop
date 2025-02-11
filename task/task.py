import sys

def welcome_message(user_team: str) -> str:
    """
    Returns a welcome message customized based on the team.

    Each team must replace the placeholder block below with an if condition
    that appends a team-specific greeting if user_team matches your team.
    """
    # Base message
    message = "Welcome to JII! From... "

    # >>>>>>>> TEAM GREETING BLOCK - REPLACE THE NEXT LINES WITH YOUR IF CONDITION <<<<<<<<<<
    message += " DEFAULT GREETING!" 
    # <<<<<<<<<< END TEAM GREETING BLOCK >>>>>>>>>>

    return message

if __name__ == "__main__":
    import sys
    team = sys.argv[1] if len(sys.argv) > 1 else ""
    print(welcome_message(team))

def main():
    # Example usage: python main.py Alpha
    user_team = sys.argv[1] if len(sys.argv) > 1 else ""
    print(welcome_message(user_team))

if __name__ == "__main__":
    main()
