#!/usr/bin/python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") == True else "upper" if islower("a") == False else islower("a")))
print("H is {}".format("lower" if islower("H") == True else "upper" if islower("H") == False else islower("H")))
print("A is {}".format("lower" if islower("A") == True else "upper" if islower("A") == False else islower("A")))
print("3 is {}".format("lower" if islower("3") == True else "upper" if islower("3") == False else islower("3")))
print("g is {}".format("lower" if islower("g") == True else "upper" if islower("g") == False else islower("g")))
