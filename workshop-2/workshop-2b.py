name = input("Your name: "))
age = int(input("Your age: "))
height = float(input("Your height: "))
power = int(input("Your power (1-10): "))
money = float(input("Your balance (Starter Pack Dollar): "))

print("\n--- ผลการพิจารณา ---")
if age < 18:
    print(f"ไอ้หนู {name} แกยังเด็กเกินไป กลับไปกินนมตั้งใจเรียนซะ! ")
elif power >= 8:
    print(f"ยินดีต้อนรับ {name} ตำแหน่งของแกคือ: มือปืน (Hitman) ")
elif money >= 1000000:
    print(f"ยินดีต้อนรับ {name} ตำแหน่งของแกคือ: นายทุน (Sponsor) ")
else:
    print(f"ยินดีต้อนรับ {name} ตำแหน่งของแกคือ: ภารโรงล้างจานในคาสิโน ")
