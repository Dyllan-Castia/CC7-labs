highway_number = int(input())

if highway_number < 1 or highway_number > 999:
    print(f"{highway_number} is not a valid interstate highway number.")

elif 1 <= highway_number <= 99:
    if highway_number % 2 == 0:
        print(f"I-{highway_number} is primary, going east/west.")
    else:
        print(f"I-{highway_number} is primary, going north/south.")

else:
    primary = highway_number % 100

    if primary == 0:
        print(f"{highway_number} is not a valid interstate highway number.")
    else:
        if primary % 2 == 0:
            print(f"I-{highway_number} is auxiliary, serving I-{primary}, going east/west.")
        else:
            print(f"I-{highway_number} is auxiliary, serving I-{primary}, going north/south.")
