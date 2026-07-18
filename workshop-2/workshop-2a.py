# WORKSHOP 2A - ระบบคำนวณกำไรค้าอาวุธเถื่อน

quantity = int(input("รับมากี่กระบอก?: "))
cost_per_gun = float(input("รับมากระบอกละกี่บาท?: "))
sell_price_per_gun = float(input("จะนำไปขายกระบอกละกี่บาท?: "))
team_members = int(input("มีลูกน้องออกไปทำปฏิบัติการนี้กี่คน?: "))

total_cost = quantity * cost_per_gun
revenue = quantity * sell_price_per_gun
profit = revenue - total_cost
boss_money = profit * 0.2
each_member_money = profit * 0.8 / team_members

print(f"ต้นทุนราคา {total_cost} บาท")
print(f"มีรายได้รวม {revenue} บาท")
print(f"ได้รับกำไร {profit} บาท")
print(f"เป็นเงินของบอส {boss_money} บาท")
print(f"มีลูกน้องเข้าร่วมปฏิบัติการนี้ {team_members} คน และจะได้รับคนละ {each_member_money} บาท")
