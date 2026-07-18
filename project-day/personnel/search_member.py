from data import family_members

def search_member(target_name):
    for person in family_members:
        if person["name"].lower() == target_name.lower():
            return person
    return None
