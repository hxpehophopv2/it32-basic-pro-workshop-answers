# WORKSHOP 3C - ปฏิบัติการเก็บค่าคุ้มครอง (While True Loop)

total_money = 0
num_shops = 0 # จำนวนร้านที่เก็บไปแล้ว


# ลูปทำงานไปเรื่อย ๆ ไม่มีวันหยุดจนกว่าจะเจอ break
while True:
    # รับค่าเป็น String ก่อน (ห้ามครอบ float() ตรงนี้เด็ดขาด)
    data = input(f"กรอกยอดเงินส่วยของร้านที่ {num_shops + 1} (หรือพิมพ์ 'police' หากตำรวจมา) : ")
    
    # 1. เช็กก่อนว่าพิมพ์ police ไหม
    if data == "police":
        print(f"ตำรวจมา! ทิ้งเงิน {total_money} บาทแล้ววิ่งหนีเร็ว!!")
        break  # สั่งหยุดลูปทันที
        
    # 2. ถ้าไม่ใช่ police ค่อยแปลงข้อมูลเป็นตัวเลขเพื่อเอาไปบวกเงิน
    money = float(data)
    total_money += money
    print(f">> เก็บเงินเพิ่มได้ ยอดรวมเป็น {total_money} บาท\n")

print(f"เมื่อกี้เก็บไปได้ทั้งหมด {num_shops} ร้านก่อนตำหนวดมา")
