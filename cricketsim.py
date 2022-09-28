import random
print( "Cricket Simulator","Allowed Inputs : 1 , 2, 3, 4, 6")
runs=0
wickets = int(input(" How many wickets would you like? : "))
while True:
    ball = input("Enter result of ball : ")
    bowler = int(random.randint( 1 ,6 ))
    if bowler == 5:
        bowler = 6
    print("Bowler picks ",bowler)
    bowler = str(bowler)
    if ball == bowler:
        wickets -= 1
        print("Wicket! and total wickets is ",wickets)
        ball = ("x")
    if wickets == 0:
            print("Game Over, total runs is ", runs)
            break
    allowed = ('1','2','3','4','6','w','n','0')
    if ball in allowed:
        if ball == '1':
            runs += 1
            print("1 run and total runs is ", runs)
        elif ball == '2':
            runs += 2
            print("2 runs and total runs is ", runs)
        elif ball == '3':
            runs += 3
            print(" 3 runs and total runs is ", runs)
        elif ball == '4':
            runs += 4
            print("A superb boundary!! and total runs is ", runs)
        elif ball == '6':
            runs += 6
            print("Wow, a a stunner of a six!!! and total runs is ", runs)
        elif ball == '0':
            print("No runs on this ball")
        elif ball == 'n':
            print ("No ball")
    elif ball == "x":
        pass
    else:
        print("Invalid Input, Try Again ")
    
