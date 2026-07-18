from data import weapons_catalog

def show_catalog():
    for key, item in weapons_catalog.items():
        print(f"[{key}] {item['name']} | ราคา: {item['price']} | พลัง: +{item['bonus']}")
