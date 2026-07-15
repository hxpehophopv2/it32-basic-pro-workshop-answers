# WORKSHOP 3B - ปฏิบัติการเก็บค่าคุ้มครอง (While Loop)

target_money = float(input("เราจะเก็บเงินให้ถึงกี่บาทดี?: "))
total_money = 0  # ตัวแปรเก็บยอดรวม
num_shops = 0 # จำนวนร้านที่เก็บไปแล้ว

# ลูปจะทำงาน "ตราบใดที่" ยอดเงินยังน้อยกว่า 50000
while total_money < 50000:
    print(f"-> ยอดปัจจุบันมีแค่ {total_money} บาท (ยังไม่ถึงเป้า!)")
    money = float(input(f"เก็บร้านที่ {num_shops + 1} กี่บาทดี?: "))
    total_money += money
    num_shops += 1

print(f"\n[รายงาน] บอสครับ! ตอนนี้ได้เงิน {total_money} บาท ทะลุเป้า {target_money} บาทแล้ว กลับฐานได้!")
