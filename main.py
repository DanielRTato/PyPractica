import prettytable

from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pikachu","Charmander", "Squiertle"])
table.add_column("Type", ["Electric","Water","Fire"])

print(table)
