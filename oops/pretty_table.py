from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Name" , ["Akhil" , "Yasar" , "Junaid"])
table.add_column("CGPA" , [8.98,9.4,8.7])
table.align = "l"
print(table)