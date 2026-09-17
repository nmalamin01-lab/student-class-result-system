def parcentage(n1, n2):
    return (n1 / n2)

def addition(n1, n2):
    return n1 + n2
symbols = {
      "+" : addition,
      "|" : parcentage
      }
grade = {
    "A" : "Excelent",
    "B" : "Very Good",
    "C" : "Good",
    "D" : "Fair",
    "E" : "Pass",
    "F" : "Fail"
    }
function = "|"
students = []

number_of_students = int(input("Enter Number of total student result to be recorded: "))
def studentresultcompiller():
    for c in range(number_of_students):
        score = []
        subject = []
        
        student = input("ADD STUDENT \nenter student name: \n")
        subNo = int(input("how many subject does the student offer?  "))
        a = range(subNo)
        for number in range(subNo):
            courses = input("Enter subject offer by the student: \n")
            subject.append(courses)

        for s in subject:
            sc = int(input("Enter Score for " + (s) + ":"))
            score.append(sc)
            done = False

            
        n_m = sum(score)
        average = symbols[function](n_m, subNo)
        print("#################STUDENT RESULT################## \n")
        print(f"Name: {student} \n")
        for i in range(subNo):
            mark = score[i]
            if mark >= 70:
                res_grade = "A"
            elif mark >= 60:
                res_grade = "B"
            elif mark >= 50:
                res_grade = "C"
            elif mark >= 45:
                res_grade = "D"
            elif mark >= 40:
                res_grade = "E"
            else:
                res_grade = "F"
                
            print(f"{subject[i]} : {mark} - {res_grade} - {grade[res_grade]}")
        print(f"\naverage: {average:.2f}")

        students.append({
            "student" : student,
            "average" : average
            })
    top_student = max(students, key=lambda x: x["average"])
    print("\nBest Student In Class:", top_student["student"])
    print("Average:", top_student["average"])
studentresultcompiller()
