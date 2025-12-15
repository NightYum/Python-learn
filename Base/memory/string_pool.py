string1 = "some string"
string2 = "some string"

print(f"string1: {string1}")
print(f"string2: {string2}")
print(f"string1 is string2? {string1 is string2}")

print()

string3 = "some " + "string"
print(f"string3 = some + string")
print(f"string1 is string2? {string1 is string2}")

print()

input_string = input("Enter a string: ")
print(f"input_string is string1? {input_string is string1}")