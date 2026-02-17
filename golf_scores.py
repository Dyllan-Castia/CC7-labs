strokes = int(input())
par = int(input())
score = ""

if par < 3 or par > 5:
    score = "Error"
else:
    if par == strokes:
        score = "Par"
    elif strokes == par + 1:
        score = "Bogey"
    elif strokes == par - 1:
        score = "Birdie"
    elif strokes == par - 2:
        score = "Eagle"
    else:
        score = "Error"

print(f"Par {par} in {strokes} strokes is {score}")
