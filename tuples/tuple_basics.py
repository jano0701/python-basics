person = ("Alice", 30, "Engineer")

# Zugriff auf einzelne Elemente
print("Name:", person[0])
print("Alter:", person[1])
print("Beruf:", person[2])

# Tuple unpacking
name, age, job = person
print(f"{name} ist {age} Jahre alt und arbeitet als {job}.")

# Tuple ist unveränderlich – das hier würde einen Fehler verursachen:
# person[1] = 31