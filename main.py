#!/bin/python3


from turtle import*
from random import*

def randomcolour():
  red= randint(0,255)
  green= randint(0,255)
  blue = randint(0,255)
  color(red,green,blue)

def ramdomplace():
  penup()
  x = randint(-100,100)
  y = randint(-100,100)
  goto(x,y)
  pendown()
  

shape("turtle")
for i in range(9000):
  randomcolour()
  ramdomplace()
  stamp()
