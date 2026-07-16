# WORKSHOP 4 - ระบบบันทึกข้อมูลลูกน้องคนใหม่

def add_member(name, age, gang):
    new_member = {
        "name": name,
        "age": age,
        "gang": gang
    }
    gang_members.append(new_member)
    return new_member

gang_members = []

while True:
    choice = input("1 for Add member | 2 for Show member | [Any key] Quit: ")
    if choice == "1":
        name_input = input("Enter you name: ")
        age_input = int(input("Enter your age: "))
        gang_input = input("Enter your gang: ")

        add_member(name_input, age_input, gang_input)
        print("Add member successfully!")
    elif choice == "2":
        print("GANG MEMBERS:")
        print(gang_members)
    else:
        print("Quitting...")
        break
        
