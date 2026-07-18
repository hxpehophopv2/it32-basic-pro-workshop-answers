from data import family_members

def remove_member(target_name):
    for person in family_members:
        if person["name"].lower() == target_name.lower():
            family_members.remove(person)
            return True
    return False
