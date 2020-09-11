my_age = 19
my_name = "Akanksha"
print("my_age")
print("Hello" + my_name +"!")
print("Hello {} you are {} years old".format(my_name,my_age))


your_name = "Jamie"
def say_hello(name):
    print("hey there, {}".format(name))

say_hello(your_name)
say_hello("Sam")

your_name = "Jamie"
your_age = 20
def say_hello(name,age):
    print("hey there, {} your age is {}".format(name,age))

say_hello(your_name,your_age)
say_hello("Sam","19")

for num in range(10):
    print ("Day {}".format(num))
    
planets = ["Mercury","Venus", "Earth", "Mars"]
planets.append("Jupiter")
planets.append("Saturn")

print(planets[1])
