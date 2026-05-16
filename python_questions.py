#An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house.

#humara code 
points=float(input("enter a no.:"))# how far the house is 
result=points/5 
 
print("no . of steps it would take to reach the house is :",round(result))

#more correct code 
points = int(input("enter a no.: "))
steps = (points + 4) // 5

print("no. of steps it would take to reach the house is:", steps)

#Q2
#A soldier wants to buy w bananas in the shop. He has to pay k dollars for the first banana, 2k dollars for the second one and so on (in other words, he has to pay i·k dollars for the i-th banana).

#He has n dollars. How many dollars does he have to borrow from his friend soldier to buy w bananas?

banas_to_buy=12
each_banana_cost=2
total_banana_cost=0
he_has_rupees=86

 

total_banana_cost = 0

for i in range(1, banas_to_buy + 1):
    cost = i * each_banana_cost
    total_banana_cost += cost
    
he_has_to_borrow=total_banana_cost-he_has_rupees

print(total_banana_cost)
print(he_has_to_borrow)

no=79
no_of_times_subtract=10
 
for i in range(1,no_of_times_subtract+1):
    if str(no[1]) == '0':
        no // 10 
    else:
        no-1


#Q3 

#A. Wrong Subtraction
#time limit per test1 second
#memory limit per test256 megabytes
#Little girl Tanya is learning how to decrease a number by one, but she does it wrong with a number consisting of two or more digits. Tanya subtracts one from a number by the following algorithm:

#if the last digit of the number is non-zero, she decreases the number by one;
#if the last digit of the number is zero, she divides the number by 10 (i.e. removes the last digit).
#You are given an integer number 𝑛
#. Tanya will subtract one from it 𝑘
 #times. Your task is to print the result after all 𝑘
 #subtractions.

#It is guaranteed that the result will be positive integer number.
#this logic was totally correct 
no=79
no_of_times_subtract=10
 
for i in range(1,no_of_times_subtract+1):
    if no % 10 == 0 :
        no = no // 10 
    else:
        no=no -1
        
#Q4 
# #Petya loves football very much. One day, as he was watching a football match, he was writing the players' current positions on a piece of paper. To simplify the situation he depicted it as a string consisting of zeroes and ones. A zero corresponds to players of one team; a one corresponds to players of another team. If there are at least 7 players of some team standing one after another, then the situation is considered dangerous. For example, the situation 00100110111111101 is dangerous and 11110111011101 is not. You are given the current situation. Determine whether it is dangerous or not.

# for me lets make the dengorous no. 4 
#did this question in pure self logic 
string="110011000111"
if "0000" in string or "1111" in  string:
    print("it is dengorous situation")
else:
    print("it is not dengorous situation") 


#Q watermelon 
#One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

#Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.
weight_of_melon=4
if weight_of_melon % 2 == 0 :
    print("they can have the water melon equally")
else:
    print("they cant have it equally")



#Qteams
n = int(input())
count = 0

for i in range(n):
    values = input().split()

    p = int(values[0])
    v = int(values[1])
    t = int(values[2])

    if p + v + t >= 2:
        count += 1

print(count)

# Q bit++ 
n=1
no_of_times_to_enter_input=2
for i in range(no_of_times_to_enter_input):
    if input == "x++":
        n=n+1 
        if input == "--x":
          n=n-1
          if input == "++x":
              n=n
              if input == "x--":
                  n=n
    else:
        print("enter valid input")

print("final value of n is : ",n)

#Q next round 
no_of_participants=4
kth_place=2
scores=[]
count=0
for i in range(no_of_participants):
    inpu=int(input("enter the score of seven participant:"))
    scores.append(inpu)
    print(scores)
    
print(scores[2])
pass_next_round=scores[2]
for j in range(len(scores)):
    if scores[j] > pass_next_round:
        count += 1 
        
print("so no. of people going next round is :",count)
