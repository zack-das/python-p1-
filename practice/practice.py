
print("Coding")
for i in range (10):
    current = i
    previous = i - 1 if  i > 0  else  0
    total = current + previous

    print(f"current:{current}, previous:{previous} and total {total}")
