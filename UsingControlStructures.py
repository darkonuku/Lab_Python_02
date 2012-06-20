print'LAB02, PART II'
print''
print 'Question 5'
print''
theInput = raw_input("Enter an integer: ")
if int(theInput) % 2 == 0:
    print 'the value you entered is','even'
else:
    print'the value you enteed is','odd'
print''
print'-----------------------------------------------------------------------'
print''

print 'Question 6'

#declaring variables
primarySchoolAge = 4
legalVotingAge = 18
presidentAge = 35
retirementAge = 60
personAge = input('Enter an age: ')

if personAge < primarySchoolAge:
    print'Too Young'
if personAge >= legalVotingAge:
    print'Remember to vote'
if (personAge >= legalVotingAge) and (personAge < presidentAge):
    print"You can't be president"
if personAge >= retirementAge:
    print'Too old'
elif personAge >= presidentAge:
    print 'Vote for me'


print''
print'-----------------------------------------------------------------------'
print''

print'Question 7'

print'the multiples of 3 between 40 and 0 in descending order are: '
for i in range(40,-1,-1):
    if i%3 == 0:
        print i

print''
print'-----------------------------------------------------------------------'
print''

print'Question 8'
print'the multiples of 3 between 6 and 30 are: '
for i in range(6,30):
    if (i%2!=0) and (i%3 !=0) and (i % 5 !=0):
        print i
        

print''
print'-----------------------------------------------------------------------'
print''

print'Question 9'
print'the number is: '
i = 0
while (True):
    if (79*i)%97 == 1:
        print i
        break
    i += 1
    

