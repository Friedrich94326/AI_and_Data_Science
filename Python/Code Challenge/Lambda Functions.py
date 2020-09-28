# syntax: lambda my_input: <my_input modified somehow>
contains_a = lambda word: "a" in word

print contains_a("banana")
print contains_a("apple")
print contains_a("cherry")


long_string = lambda str: len(str) > 12
print long_string("short")
print long_string("photosynthesis")



ends_in_a = lambda word: word[-1] == "a"
print ends_in_a("data")
print ends_in_a("aardvark")


double_or_zero = lambda num: 2*num if num > 10 else 0
print double_or_zero(15)
print double_or_zero(5)


even_or_odd = lambda num: "even" if num % 2 == 0 else "odd"
print even_or_odd(10)
print even_or_odd(5)

multiple_of_three = lambda num: "multiple of three" if num % 3 == 0 else "not a multiple"
print multiple_of_three(9)
print multiple_of_three(10)


rate_movie = lambda rating: "I liked this movie." if rating > 8.5 else "This movie was not very good."
print rate_movie(9.2)
print rate_movie(7.2)


ones_place = lambda num: num % 10
print ones_place(123)
print ones_place(4)


double_square = lambda num: 2*(num**2)
print double_square(5)
print double_square(3)


# random.randint(a,b) returns an integer between a and b (inclusive)
import random
#Write your lambda function here
add_random = lambda num: num + random.randint(1, 10)
print add_random(5)
print add_random(100)


