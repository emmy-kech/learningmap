skills = {}
while True:
    k = input("add skills:")
    val = input("have you done this skill?")
    skills[k] = val
    skills.update({k:val})
    print(k)