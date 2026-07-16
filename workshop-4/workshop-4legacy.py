# WORKSHOP 4 LEGACY

# 1. ประกาศตัวแปร Data Structure
active_list = [
    {"name": "Tony", "bounty": 50000},
    {"name": "Luigi", "bounty": 30000},
    {"name": "Mario", "bounty": 100000}
]
captured_list = []
bank_account = 0.0

# 2. ฟังก์ชันทั้ง 4 ตาม Requirement
def search_target(target_name, current_active, current_captured):
    # ค้นหาใน Active List ก่อน
    for person in current_active:
        if person["name"].lower() == target_name.lower():
            return 1, person  # คืนค่า 1 แปลว่าเจอใน Active
            
    # ค้นหาใน Captured List
    for name in current_captured:
        if name.lower() == target_name.lower():
            return 2, None    # คืนค่า 2 แปลว่าโดนจับไปแล้ว
            
    # ไม่พบเลย
    return 3, None            # คืนค่า 3 แปลว่าไม่พบเป้าหมาย

def add_money(current_bank, bounty_amount):
    return current_bank + bounty_amount

def capture_target(target_name, current_captured):
    current_captured.append(target_name)

def remove_active(person_data, current_active):
    current_active.remove(person_data)

# 3. Main Loop สำหรับการทำงานหลัก
print("=== THE BOUNTY HUNTER SYSTEM ===")

while True:
    # เงื่อนไขจบโปรแกรม: Active List ว่างเปล่า
    if len(active_list) == 0:
        print("\nเป้าหมายถูกจับหมดแล้ว! ปิดระบบ...")
        break
        
    # Output ระหว่างทำงาน
    print("-" * 40)
    print(f"BankAccount ปัจจุบัน: {bank_account} บาท")
    print("คนที่ยังรอดใน Active List:")
    for p in active_list:
        print(f"   - {p['name']} (ค่าหัว: {p['bounty']} บาท)")
        
    # รับ Input
    name_input = input("\nใส่ชื่อคนที่ต้องการล่า (หรือพิมพ์ 'q' เพื่อออก): ")
    
    # เงื่อนไขจบโปรแกรม: ผู้ใช้พิมพ์ q
    if name_input.lower() == 'q':
        print("\nยกเลิกการล่า ปิดระบบ...")
        break
        
    # เรียกใช้ฟังก์ชันค้นหา และรับสถานะกลับมา
    status, target_data = search_target(name_input, active_list, captured_list)
    
    # ตรวจสอบ 3 กรณีตามสไลด์
    if status == 1:
        # กรณีที่ 1: หาชื่อเจอใน Active List -> เรียกใช้ฟังก์ชันอีก 3 ตัวที่เหลือ
        bank_account = add_money(bank_account, target_data["bounty"])
        capture_target(target_data["name"], captured_list)
        remove_active(target_data, active_list)
        print(f"จับกุม {target_data['name']} สำเร็จ! รับเงิน {target_data['bounty']} บาท")
        
    elif status == 2:
        # กรณีที่ 2: หาชื่อเจอ แต่โดนจับไปแล้ว
        print(f"ไอ้หมอนี่โดนจับไปแล้ว!")
        
    else:
        # กรณีที่ 3: หาชื่อไม่เจอเลย
        print("ไม่พบเป้าหมายในระบบ!")

# 4. Output เมื่อจบโปรแกรม
print("\n=== สรุปผลงาน ===")
print(f"สรุปยอดเงินทั้งหมด: {bank_account} บาท")
print(f"รายชื่อใน Captured List: {captured_list}")
