def get_most_common_letter(text):
    counter = {}
    print("counter is initialised as an empty dictionary {}")
    for char in text:
        if char != " ":
            print(f"for {char} in {text}")
            counter[char] = counter.get(char, 0) + 1
            print(counter[char])
    letter = sorted(counter.items(), key=lambda item: item[1], reverse = True)[0][0]
    print(sorted(counter.items()))
    print(letter)
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
