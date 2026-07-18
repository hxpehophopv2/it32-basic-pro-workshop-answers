def send_mission(person):
    if person["power"] >= 7:
        reward = 300000
        person["money"] += reward
        return {"status": True, "reward": reward}
    return {"status": False, "reward": 0}
