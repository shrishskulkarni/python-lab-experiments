## Experiment Title

Experiment 2

## Aim

To write a program to implement control flow statements and looping statements in Python.

## Algorithm

1. Read `n`, the number of players from the user.
2. Initialize a loop counter `i = 0`.
3. Repeat while `i < n`:
   - Increment `i` by 1.
   - Read `rscored`, `bfaced`, `fours`, `sixes`, `wickets`, `rcon`, `ob`, and `ct` from the user.
   - Compute batting strike rate `sr = (rscored / bfaced) * 100` and print it.
   - Compute bowling economy rate `er = rcon / ob` and print it.
   - Based on `rscored` and `sr`, classify the player as "Excellent Batter", "Good Batter", "Average Batter", or "Poor Batter" and store the result in `batter`.
   - Based on `wickets` and `er`, classify the player as "Excellent Bowler", "Good Bowler", "Average Bowler", or "Poor Bowler" and store the result in `bowler`.
   - Based on `ct`, classify fielding as "Outstanding Fielder", "Active Fielder", or "Needs Improvement".
   - Using the `batter` and `bowler` labels, classify the overall all‑round performance as "Star All-Rounder", "Strong All-Rounder", "Supporting All-Rounder", or "Needs Improvement".
4. End the loop after processing all `n` players.

## Output

Sample run:

```text
Enter Number of players: 1
enter runs scored: 65
enter balls faced: 50
enter fours: 8
enter sixes: 2
enter wickets taken: 3
enter runs conceded: 24
enter overs bowled: 4
enter catches taken: 2
130.0
6.0
Excellent Batter
Excellent Bowler
Outstanding Fielder
Star All-Rounder
```
