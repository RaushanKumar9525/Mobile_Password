def student_grade_management():
    students = []  
    #take user name and id.
    while True:
        name = input("Enter Student Name :-->") 
        student_id = input("Enter Student Id No:-->")
        total_score = 0
        scores = []
#take five subject marks and calculate total marks.
        for i in range(1, 6):
            score = float(input(f"Enter the Marks of Subject {i} :-->"))
            scores.append(score)
            total_score =total_score + score 

        grade = calculate_grade(total_score)

        students.append({
            'Name': name,
            'ID': student_id,
            'Scores': scores,
            'Total Score': total_score,
            'Grade': grade
        })
#it used to add new student then pres yes and user wansts to not store new student then press no. 
        if input("Add another student? (yes/no):-->").lower() != 'yes':
            break

    display_students(students)
#calculate average and assign the grade aaccording to average value.
def calculate_grade(total_score):
    average_score = total_score / 5  # store average value.
    if average_score >= 95:     
        return 'A'
    elif average_score >= 90:
        return 'B'
    elif average_score >= 80:
        return 'C'
    elif average_score >= 75:
        return 'D'
    elif average_score >= 70:
        return 'E'
    else:
        return 'F'
# Display the student name, id and total score and last is grade in table formate.
def display_students(students):
    print("\n Student Details :")
    print("ID\t Name \t Total.s.\t Grade")
    for student in students:
        print(f"{student['ID']}\t {student['Name']}\t {student['Total Score']}\t \t \t{student['Grade']}")

# Start the program
student_grade_management()
