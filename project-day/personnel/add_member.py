from data import family_members

def add_member(name, age, power, money):
    if power >= 8:
        role = "Hitman"
    elif money >= 1000000:
        role = "Sponsor"
    else:
        role = "Slave"
    new_member = {"name": name, "age": age, "role": role, "power": power, "money": money, "equipment": "ไม่มี"}
    family_members.append(new_member)
    return new_member
