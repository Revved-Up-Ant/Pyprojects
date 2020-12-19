# Odd-Even game for APS DK guys in isolation
import random

compnum = 0
j = 1
teamcs = 0
teamfs = 0
f = 1
name = input('enter name:')
wickets = int(input('Number of Wickets Per team:'))
print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
1.)You have to chose a number between 1-6 for toss then computer will chose a number
2.)You will then have to chose odd or even respectivley
3.)if the sum of your numbers is odd or even and you chose that option you win the toss 
4.)You Have to chose batting or bowling if you won the toss if you lose the toss computer will chose it
5.)The computer (from it's alogorithm) and you will chose a number on each ball 
6.)If you are bowling then the numbers which computer choses will be added to thier total runs and if your number are same then a wicket will fall
7.)If you are batting the numbers you chose will be added to the tally and computer choses a number , if your numbers match a wicket falls
8.)Falling of all wickets of team batting first would mark end of thier innings and score at that point will be taken up for chase
9.)If the Second batting team Reaches the Score without getting Bowled out they win
10.)If the second batting team reaches the score and do not get bowled out they will still keep on playing till all thier wickets fall allowing second batting team to win by a very big margin 
''')
input('Press Enter to Go Forward:')

def team_chose():
    global teamc
    global teamf
    print('\n\n\n\n\n\n\n\nwhich team you want to fight')
    teams = ['0', 'Chennai Super Kings', 'Delhi Capitals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad',
             'Rajashtan Royals', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Mumbai Indians']
    for i in range(1, len(teams)):
        print(i, ':', teams[i])
    c = 1
    while c == 1:
        teamfn = int(input('chose team (1-8):'))
        if (teamfn >= 1) and (teamfn <= 8):
            teamf = teams[teamfn]
            teams.pop(teamfn)
            c = 2
        else:
            print('wrong Input going back')
            c = 1
    print('\n\n\n\n\n\n\n\n\nTeam chosen to fight=', teamf)
    print('which team you want to Chose')
    for f in range(1, len(teams)):
        print(f, ':', teams[f])
    d = 1
    while d == 1:
        teamcn = int(input('chose team (1-8):'))
        if (teamcn >= 1) and (teamcn <= 8):
            teamc = teams[teamcn]
            teams.pop(teamcn)
            d = 2
        else:
            print('wrong Input going back')
            d = 1
    print('Team chosen=', teamc)


def toss():
    global teamc
    global teamf
    global tossw
    global chose
    b = 1
    while b == 1:
        utoss = int(input('Enter Number for Toss(1-6):'))
        if utoss > 6:
            print('wrong input enter Number again:')
            b = 1
        elif utoss <= 0:
            print('wrong input enter number again')
            b = 1
        else:
            b = 2
    ctoss = random.randint(1, 6)
    print('computer has chosen a number')
    a = 1
    while a == 1:
        oe = input('Choose Odd or even (o/e):')
        if (oe == 'e') or (oe == 'E') or (oe == 'o') or (oe == 'O'):
            a = 2
        else:
            print('Wrong input')
            a = 1
    if (((utoss + ctoss) % 2) == 0):
        if (oe == "e") or (oe == "E"):
            print('Its Even')
            print(teamc, ' Won the Toss,', teamf, ' chose the Number ', ctoss, 'and ', teamc, ' chose ', utoss)
            tossw = 1
        else:
            print('Its Even')
            print(teamf, ' Won the Toss,', teamf, ' chose the Number ', ctoss, 'and ', teamc, ' chose ', utoss)
            tossw = 2
    else:
        if (oe == 'o') or (oe == 'O'):
            print('Its Odd')
            print(teamc, ' Won the Toss,', teamf, ' chose the Number ', ctoss, ' and ', teamc, ' chose ', utoss)
            tossw = 1
        else:
            print('Its odd')
            print(teamf, ' Won the Toss,', teamf, ' chose the Number ', ctoss, ' and ', teamc, ' chose ', utoss)
            tossw = 2
    if tossw == 1:
        f = 1
        while f == 1:
            chose = input('Choose Batting or Bowling(ba,bo)')
            if chose == 'ba':
                confirm = input('you chose batting do you want to confirm(y/n)')
                if (confirm == 'y') or (confirm == 'Y'):
                    print(teamc, ' Chose to Bat first')
                    f = 2
                elif (confirm == 'n') or (confirm == 'N'):
                    f = 2
                else:
                    print('Wrong Input')
                    f = 1
            elif chose == 'bo':
                confirm = input('you chose Bowling do you want to confirm(y/n)')
                if (confirm == 'y') or (confirm == 'Y'):
                    print(teamc, ' Chose to bowl first')
                    f = 2
                elif (confirm == 'n') or (confirm == 'N'):
                    f = 1
                else:
                    print('Wrong Input')
                    f = 1
    else:
        comptoss = random.randint(1, 2)
        if comptoss == 1:
            chose = 'bo'
            print(teamf, ' Chose to Bat first')
        else:
            chose = 'ba'
            print(teamf, ' Chose to Bowl first')


def num_choose():
    global un
    global cn
    global chose
    e = 1
    while e == 1:
        un = int(input('Enter your number (1-6):'))
        cn = random.randint(1, 6)
        if un >= 1 and un <= 6:
            print(teamc, " Chose ", un, " and ", teamf, " chose ", cn)
            e = 2
        else:
            print('Wrong input')
            e = 1


def bat():
    print(teamc, 'is now batting')
    global teamcs
    global f
    g = 1
    while g == 1:
        num_choose()
        if un != cn:
            while f == 1:
                teamcs = un
                f = 2
            teamcs = teamcs + un
            g = 1
        elif un == cn:
            print('Wicket!\n\n\n\n')
            teamcs = teamcs
            g = 2
    print(teamc, ' Made ', teamcs, ' Runs')


def bowl():
    print(teamf, 'is now batting')
    global j
    global teamfs
    h = 1
    while h == 1:
        num_choose()
        if un != cn:
            while j == 1:
                teamfs = cn
                j = 2
            teamfs = teamfs + cn
            h = 1
        elif un == cn:
            print('Wicket!\n\n\n\n')
            teamfs = teamfs
            h = 2
    print(teamf, ' Made ', teamfs, ' Runs')


def game():
    global teamcs
    global teamfs
    team_chose()
    toss()
    if chose == 'ba':
        for z in range(1, wickets + 1):
            bat()
        for y in range(1, wickets + 1):
            bowl()
        l = 1
        if teamcs > teamfs:
            print(teamc, ' Wins against ', teamf, ' with ', teamcs - teamfs, ' runs')
        elif teamfs > teamcs:
            print(teamf, ' Wins against ', teamc, ' with ', teamfs - teamcs, ' runs')
        else:
            print('Tie')
    elif chose == 'bo':
        for x in range(1, wickets + 1):
            bowl()
        for w in range(1, wickets + 1):
            bat()
        if teamfs > teamcs:
            print(teamf, ' Wins against ', teamc, ' with ', teamfs - teamcs, ' runs')
        elif teamcs > teamfs:
            print(teamc, ' Wins against ', teamf, ' with ', teamcs - teamfs, ' runs')
        else:
            print('Tie!')


game()




