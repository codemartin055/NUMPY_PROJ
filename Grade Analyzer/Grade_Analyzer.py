import numpy as np
names=np.array(['Amina','Brian','Cynthia','David','Esther','Felix','Grace','Hassan','Irene','James'])
scores=np.array([72,85,90,64,78,55,93,48,81,67])
print("Average:",scores.mean()) #the average
print("The Median:",np.median(scores)) #the middle value
print("Max score:",scores.max()) #The highest score
print("Min score:",scores.min()) #lowest score
print("Std:",scores.std()) #spread of scores
passed=scores>=60
print("Number of passed:",passed.sum())
print("Passed:", names[passed])
print("Number failed:", (~passed).sum())
print("Failed:",names[~passed])
best_mark=scores.argmax() #argmax looks for the position of max score
print("Top student:",names[best_mark])
conditions = [scores >= 80, scores >= 70, scores >= 60]
letters    = ["A",          "B",          "C"]

grades = np.select(conditions, letters, default="F")
print(grades)
for name, score, grade in zip(names, scores, grades):
    print(f"{name:<10} {score:>3}  {grade}")

print("A:", (grades == "A").sum())
print("B:", (grades == "A").sum())
print("C:", (grades == "C").sum())
print("F:", (grades == "F").sum())
print("Total:", (grades == "A").sum() + (grades == "B").sum() + (grades == "C").sum() + (grades == "F").sum())