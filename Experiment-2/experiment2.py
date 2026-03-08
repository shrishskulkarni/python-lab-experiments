n = int(input("Enter Number of players: "))
i = 0

while (i < n):
    i = i + 1
    rscored = int(input("enter runs scored: "))
    bfaced = int(input("enter balls faced: "))
    fours = int(input("enter fours: "))
    sixes = int(input("enter sixes: "))
    wickets = int(input("enter wickets taken: "))
    rcon = int(input("enter runs conceded: "))
    ob = int(input("enter overs bowled: "))
    ct = int(input("enter catches taken: "))
    
    sr = (rscored / bfaced) * 100
    print(sr)
    er = rcon / ob
    print(er)
    
    if (rscored >= 50 and sr >= 120):
        print("Excellent Batter")
        batter = "Excellent Batter"
    elif (rscored >= 30 and sr >= 100):
        print("Good Batter")
        batter = "Good Batter"
    elif (rscored >= 20):
        print("Average Batter")
        batter = "Average Batter"
    else:
        print("Poor Batter")
        batter = "Poor Batter"
        
    if (wickets >= 3 and er <= 6):
        print("Excellent Bowler")
        bowler = "Excellent Bowler"
    elif (wickets >= 2 and er <= 8):
        print("Good Bowler")
        bowler = "Good Bowler"
    elif (wickets >= 1):
        print("Average Bowler")
        bowler = "Average Bowler"
    else:
        print("Poor Bowler")
        bowler = "Poor Bowler"
        
    if (ct >= 2):
        print("Outstanding Fielder")
    elif (ct == 1):
        print("Active Fielder")
    else:
        print("Needs Improvement")
        
    if (batter == "Excellent Batter" and bowler == "Excellent Bowler"):
        print("Star All-Rounder")
    elif (batter == "Good Batter" and bowler == "Good Bowler"):
        print("Strong All-Rounder")
    elif (batter == "Good Batter" or bowler == "Good Bowler"):
        print("Supporting All-Rounder")
    else:
        print("Needs Improvement")
