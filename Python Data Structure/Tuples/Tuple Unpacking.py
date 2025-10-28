# Demonstrates unpacking tuples.

person = ("Alice", 25, "Researcher")

name, age, profession = person

if __name__=='__main__':
    print(f"Name: {name} Age: {age}, Profession: {profession}")