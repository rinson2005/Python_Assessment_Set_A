n = int(input("Enter the number of students: "))
passed = 0
failed = 0

highest = 0
topper = ""

for i in range(n):
  student = input("Enter student name and marks: ").split()
  name = student[0]
  python = int(student[1])
  database = int(student[2])
  aptitude = int(student[3])
  total = python + database + aptitude
  average = total / 3

  if python >= 40 and database >= 40 and aptitude >= 40 and average >= 50:
    passed += 1
    if average >= 80:
      grade = "A"
    elif average >= 70:
      grade = "B"
    elif average >= 60:
      grade = "C"
    else:
      grade = "D"
    print(f"{name.title()} - Average: {average:.2f} - Passed - Grade: {grade}")
  else:
    failed += 1
    print(f"{name} - Average: {average:.2f} - Failed")

  if average > highest:
    highest = average
    topper = name

print("-" * 30)
print(f"Passed: {passed}")
print(f"Failed: {failed}")
if topper:
  print(f"Top Performer: {topper.title()}")