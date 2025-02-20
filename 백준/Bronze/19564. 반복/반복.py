alphabet = list("abcdefghijklmnopqrstuvwxyz")
text = input()
index = -1
count = 1

for t in text:
    current_index = alphabet.index(t)

    if index < current_index:
        index = current_index
    else:
        index = current_index
        count += 1

print(count)