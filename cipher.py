
with open("originaltext.txt", "r", encoding="utf-8") as file:
    for line in file.readlines()[::-1]:
        with open("encrypted.txt", "a", encoding="utf-8") as efile:
            efile.write(line[::-1])