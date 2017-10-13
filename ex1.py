print "hi"
print "hey"
print "whats up"
print "hello"
print "this is weird"
print "My name is jeff" #I suck
print 25 + 30 - 2

cars = 125
drivers = 30
passengers = 50
print "We have", cars, "cars available"
print "There are", drivers, "drivers today"
print "there is", passengers, "passengers"

my_name = 'Max'
my_age = 17
my_weight = 170
my_height = 74

print "my name is %s." % my_name
print "I am %s years old." % my_age
print "I weigh %s pounds." % my_weight
print " I am %s inches tall." % my_height

x = 'My name'
y = 'is jeff'
z = 'this meme is dead'
print "I said: %s" % x
print "%s" % y
print "I also said: %s" % z

def print_two (*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
dudes = 20
trucks = 23
if dudes > trucks:
    print "we should take the trucks"
if trucks > dudes:
    print "Let's not go to school"

people = 30
cars = 40
trucks = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."
if trucks > cars:
    print "There are too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."
if people > trucks:
    print "Alright let's just take the trucks."
else:
    print "Fine, we'll just stay home then."

True and True
False and True
1 == 1 and 2 == 1
"test" == "test"
1 == 1 or 2 != 1
True and 1 == 1
False and 0 != 0
True or 1 == 1
"test" == "testing"
1 != 0 and 2 == 1
"test" != "testing"
"test" == 1
not (True and False)
not (1 == 1 and 0 != 1)
not (10 == 1 or 1000 == 1000)
not (1 != 10 or 3 ==4)
not ("testing" == "testing" and "Zed" == "Cool Guy")
"chunky" == "bacon" and (not (3 == 4 or 3 == 3))
3 == 3 and (not("testing" == "testing" or "Python" == "Fun"))

print "You enter a dark room with two doors. Do you enter door #1 or door #2?"

door = raw_input(">")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do."
    print "1. Take the cake."
    print "2. Scream at the bear."

if bear == "1":
     print "The bear eats your face off. Good job!"
elif bear == "2":
    print "The bear eats your legs off.  Good job!"

if insanity == "1" or insanity == "2":
    print "Your body survives power by a mind of jello. Good job!"
else:
    print "The insanity rots your eyes into a pool of muck. Good job!"
    print "You stumble around and fall on a knife and die. Good job!"

the_count = [1, 2, 3, 4, 5]
fruits = ['apples,' 'oranges,' 'pears,''apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

for i in change:
    print "I got %r" % i

elements = []


for i in range(0, 6):
    print "Adding %d to the list." % i
elements.append(i)

for i in elements:
    print "Element was: %d" % i

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num

states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

cities = {
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
    }

cities['NY'] = 'New York'
cities['OR'] = 'Oregon'

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" %(abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
    states, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city

class Song(object):

    def _init_(self, lyrics):
        self.lyrics = lyrics

def sing_me_a_song(self):
    for line in self.lyrics:
        print line

happy_bday = Song(["Happy birthday to you",
            "I don't want to get sued",
            "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

sum = 0
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        sum += i
print sum
