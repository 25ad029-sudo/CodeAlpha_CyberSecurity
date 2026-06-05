attempts = {}

while True:
    ip = input("Enter IP Address (or exit): ")

    if ip.lower() == "exit":
        break

    if ip in attempts:
        attempts[ip] += 1
    else:
        attempts[ip] = 1

    if attempts[ip] > 3:
        print("ALERT! Suspicious Activity from", ip)
    else:
        print("Access Recorded")