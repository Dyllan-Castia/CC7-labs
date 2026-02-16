message = input("Enter message: ")

found = False

if "LOL" in message:
    message = message.replace("LOL", "laughing out loud")
    found = True
if "BFN" in message:
    message = message.replace("BFN", "bye for now")
    found = True
if "FTW" in message:
    message = message.replace("FTW", "for the win")
    found = True
if "IRL" in message:
    message = message.replace("IRL", "in real life")
    found = True

if not found:
    print("Sorry, don't see any abbreviations")
else:
    print(message)
    
