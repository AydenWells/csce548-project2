import requests

BASE = "http://127.0.0.1:5000"


def main():
    print("1) CREATE student")
    r = requests.post(f"{BASE}/student", json={"name": "Ayden", "email": "ayden@example.com"})
    print("Status:", r.status_code, "Body:", r.json())
    new_id = r.json().get("id")

    print("\n2) GET student")
    r = requests.get(f"{BASE}/student/{new_id}")
    print("Status:", r.status_code, "Body:", r.json())

    print("\n3) UPDATE student")
    r = requests.put(f"{BASE}/student", json={"id": new_id, "name": "Ayden Updated", "email": "ayden2@example.com"})
    print("Status:", r.status_code, "Body:", r.json())

    print("\n4) GET student again (prove update)")
    r = requests.get(f"{BASE}/student/{new_id}")
    print("Status:", r.status_code, "Body:", r.json())

    print("\n5) DELETE student")
    r = requests.delete(f"{BASE}/student/{new_id}")
    print("Status:", r.status_code, "Body:", r.json())

    print("\n6) GET student again (prove delete)")
    r = requests.get(f"{BASE}/student/{new_id}")
    print("Status:", r.status_code, "Body:", r.json())


if __name__ == "__main__":
    main()