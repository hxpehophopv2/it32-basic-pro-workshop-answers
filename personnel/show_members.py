from data import family_members

def show_members():
    for person in family_members:
        print(f"ชื่อ: {person['name']} | ตำแหน่ง: {person['role']} | ความโหด: {person['power']} | อาวุธ: {person['equipment']}")
