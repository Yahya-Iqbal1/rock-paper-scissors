import random

print("=" * 45)
print("   ✊ ROCK PAPER SCISSORS GAME ✂️")
print("=" * 45)
print("     Made by M. Yahya Iqbal")
print("=" * 45)

choices = ["rock", "paper", "scissors"]

emojis = {
    "rock": "✊",
    "paper": "📄",
    "scissors": "✂️"
}

player_score = 0
computer_score = 0
ties = 0
player_streak = 0
computer_streak = 0
best_streak = 0
total_games = 0

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

while True:
    print("\n" + "-" * 45)
    print(f"  📊 Score  —  You: {player_score}  |  CPU: {computer_score}  |  Ties: {ties}")
    print(f"  🔥 Your Streak: {player_streak}  |  Best Streak: {best_streak}")
    print("-" * 45)
    print("\n  Choose your move:")
    print("  1 — Rock     ✊")
    print("  2 — Paper    📄")
    print("  3 — Scissors ✂️")
    print("  4 — Stats    📈")
    print("  5 — Quit     🚪")

    choice = input("\n  Enter (1/2/3/4/5): ").strip()

    if choice == "5":
        print("\n" + "=" * 45)
        print("       FINAL RESULTS")
        print("=" * 45)
        print(f"  Total Games  : {total_games}")
        print(f"  You Won      : {player_score}")
        print(f"  CPU Won      : {computer_score}")
        print(f"  Ties         : {ties}")
        print(f"  Best Streak  : {best_streak} 🔥")
        if total_games > 0:
            win_rate = round((player_score / total_games) * 100, 1)
            print(f"  Win Rate     : {win_rate}%")
        print("=" * 45)
        print("  Thanks for playing! — Yahya Iqbal")
        print("=" * 45)
        break

    elif choice == "4":
        print("\n" + "=" * 45)
        print("         📈 YOUR STATS")
        print("=" * 45)
        print(f"  Total Games  : {total_games}")
        print(f"  Wins         : {player_score}")
        print(f"  Losses       : {computer_score}")
        print(f"  Ties         : {ties}")
        print(f"  Best Streak  : {best_streak} 🔥")
        if total_games > 0:
            win_rate = round((player_score / total_games) * 100, 1)
            print(f"  Win Rate     : {win_rate}%")
        print("=" * 45)
        continue

    elif choice in ["1", "2", "3"]:
        player_choice = choices[int(choice) - 1]
        computer_choice = random.choice(choices)
        total_games += 1

        print(f"\n  You chose    : {emojis[player_choice]} {player_choice.upper()}")
        print(f"  CPU chose    : {emojis[computer_choice]} {computer_choice.upper()}")

        result = determine_winner(player_choice, computer_choice)

        if result == "player":
            player_score += 1
            player_streak += 1
            computer_streak = 0
            if player_streak > best_streak:
                best_streak = player_streak
            print(f"\n  🎉 YOU WIN!")
            if player_streak >= 2:
                print(f"  🔥 {player_streak} WIN STREAK!")

        elif result == "computer":
            computer_score += 1
            computer_streak += 1
            player_streak = 0
            print(f"\n  😞 CPU WINS!")
            if computer_streak >= 2:
                print(f"  💀 CPU is on a {computer_streak} streak!")

        else:
            ties += 1
            player_streak = 0
            computer_streak = 0
            print(f"\n  🤝 IT'S A TIE!")

    else:
        print("\n  ❌ Invalid choice! Enter 1, 2, 3, 4 or 5.")
