def equip_item(person, weapon):
    if person["money"] < weapon["price"]:
        return {"status": False, "message": "เงินส่วยไม่พอซื้อ"}
    if person["equipment"] != "ไม่มี":
        return {"status": False, "message": "มีอาวุธอยู่แล้ว ไม่สามารถใส่เพิ่มได้"}
    person["money"] -= weapon["price"]
    person["equipment"] = weapon["name"]
    person["power"] += weapon["bonus"]
    return {"status": True, "message": "สวมใส่อาวุธสำเร็จ"}
