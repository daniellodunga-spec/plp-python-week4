scores = [72, 45, 90, 61, 38]
passes = 0 
fail = 0
for score in scores:
    if score >= 50:
        passes = passes + 1
    else:
        fail = fail + 1
    if score >= 80:
        print("Grade: A")
    elif score >= 70 and score <= 79:
        print("Grade: B")
    elif score >= 50 and score <= 69:
        print("Grade: C")
    elif score <= 50:
        print("Grade: F")
print("passes:", passes)
print("fail:", fail)

average = sum(scores) / len(scores)
average = round(average, 1)
print("Average:", average)
