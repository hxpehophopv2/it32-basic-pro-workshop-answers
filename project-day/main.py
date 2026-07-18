# =====================================================
#  main.py — ศูนย์กลางของระบบ (ไฟล์นี้เขียนให้แล้ว ห้ามแก้!)
#  หน้าที่ของทีมคือเขียนฟังก์ชันในไฟล์ของตัวเองให้เมนูทุกอันใช้งานได้จริง
#  ถ้าเมนูไหนขึ้น "ยังไม่ถูกเขียน" แปลว่าไฟล์นั้นยังทำไม่เสร็จ
# =====================================================
from data import weapons_catalog
from personnel.add_member import add_member
from personnel.show_members import show_members
from personnel.search_member import search_member
from personnel.remove_member import remove_member
from weapon_shop.show_catalog import show_catalog
from weapon_shop.equip_item import equip_item
from missions.send_mission import send_mission

def main():
    while True:
        print("\n=== MAFIA MANAGEMENT SYSTEM ===")
        print("1. รับลูกน้องใหม่")
        print("2. ดูรายชื่อแก๊ง")
        print("3. ค้นหาประวัติ")
        print("4. สั่งเก็บลูกน้อง")
        print("5. คลังอาวุธ")
        print("6. ส่งไปทำภารกิจ")
        print("7. ออกจากระบบ")

        choice = input("เลือกคำสั่ง (1-7): ")

        if choice == '1':
            print("\n--- เพิ่มลูกน้องใหม่ ---")
            name = input("ชื่อ: ")
            age = int(input("อายุ: "))
            power = int(input("ความโหด (1-10): "))
            money = float(input("เงินส่วย: "))

            new_member = add_member(name, age, power, money)

            if new_member is None:
                print("!! add_member ยังไม่ถูกเขียน (ไปเขียนใน personnel/add_member.py)")
            else:
                print(f"เพิ่ม {new_member['name']} ในตำแหน่ง {new_member['role']} เรียบร้อยแล้ว")

        elif choice == '2':
            print("\n--- รายชื่อลูกน้องทั้งหมด ---")
            show_members()

        elif choice == '3':
            print("\n--- ค้นหาประวัติ ---")
            target = input("ชื่อที่ต้องการค้นหา: ")
            person_data = search_member(target)

            if person_data is not None:
                print(f"พบข้อมูล: ชื่อ {person_data['name']}, ตำแหน่ง {person_data['role']}, เงิน {person_data['money']}, อาวุธ {person_data['equipment']}")
            else:
                print("ไม่พบชื่อในระบบ")

        elif choice == '4':
            print("\n--- สั่งเก็บลูกน้อง ---")
            target = input("ชื่อคนที่ต้องการลบ: ")
            is_success = remove_member(target)

            if is_success:
                print(f"สั่งเก็บ {target} เรียบร้อยแล้ว")
            else:
                print("ไม่พบชื่อในระบบ")

        elif choice == '5':
            print("\n=== คลังอาวุธ ===")
            show_catalog()

            weapon_choice = input("เลือกรหัสอาวุธ (1-3): ")
            selected_weapon = weapons_catalog.get(weapon_choice)

            if selected_weapon is None:
                print("ไม่มีสินค้านี้ในระบบ")
            else:
                target_name = input("ระบุชื่อลูกน้องที่จะสวมใส่: ")
                person_data = search_member(target_name)

                if person_data is None:
                    print("ไม่พบรายชื่อลูกน้องคนนี้")
                else:
                    result = equip_item(person_data, selected_weapon)

                    if result is None:
                        print("!! equip_item ยังไม่ถูกเขียน (ไปเขียนใน weapon_shop/equip_item.py)")
                    else:
                        print(result["message"])
                        if result["status"]:
                            print(f"พลังของ {person_data['name']} อัปเดตเป็น {person_data['power']}")

        elif choice == '6':
            print("\n--- ส่งไปทำภารกิจ ---")
            target_name = input("ระบุชื่อลูกน้องที่ต้องการส่งไปเสี่ยงตาย: ")
            person_data = search_member(target_name)

            if person_data is None:
                print("ไม่พบรายชื่อลูกน้องคนนี้ในระบบ")
            else:
                result = send_mission(person_data)

                if result is None:
                    print("!! send_mission ยังไม่ถูกเขียน (โจทย์ OPTIONAL ใน missions/send_mission.py)")
                elif result["status"]:
                    print(f"ภารกิจสำเร็จ! {person_data['name']} รอดชีวิตและนำเงินกลับมาได้ {result['reward']} บาท")
                    print(f"ยอดเงินปัจจุบันของ {person_data['name']} คือ {person_data['money']} บาท")
                else:
                    remove_member(person_data["name"])
                    print(f"ภารกิจล้มเหลว! {person_data['name']} พลาดท่าเสียชีวิต...")
                    print("รายชื่อถูกลบออกจากประวัติของแฟมิลี่แล้ว")

        elif choice == '7':
            print("ปิดระบบ...")
            break

        else:
            print("คำสั่งไม่ถูกต้อง")

if __name__ == "__main__":
    main()
