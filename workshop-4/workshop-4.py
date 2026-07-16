# WORKSHOP 4 - ระบบบันทึกข้อมูลลูกน้องคนใหม่

def add_member(name, age, money):
    new_member = {
        "name": name,
        "age": age,
        "money": money
    }
    gang_members.append(new_member)
    return new_member

gang_members = []

while True:
    name_input = input()
    if name_input == "q":
        print("Quitting...")
        break
    
    age_input = int(input())
    money_input = float(input())

    add_member(name_input, age_input, money_input)
    print("Add member successfully!")

print("GANG MEMBERS:")
print(gang_members)
