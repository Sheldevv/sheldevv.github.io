import random
import string

def gen_license_plate():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    return f"{letters}-{numbers}"

# Load existing plates
try:
    with open("data.txt", "r") as f:
        existing = {line.strip() for line in f}
except FileNotFoundError:
    existing = set()

# Keep generating until unique
while True:
    lpn_str = gen_license_plate()
    if lpn_str not in existing:
        break

print(lpn_str)

with open("data.txt", "a") as f:
    f.write(lpn_str + "\n")
