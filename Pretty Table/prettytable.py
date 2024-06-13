# from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()

table.add_column('Pokemon Name', ['Pikachu', 'Squitle', '20comer100saber'])
table.add_column('Pokemon Type', ['Electric', 'Water', 'Sexo'])

table.align = 'l'

print(table)
