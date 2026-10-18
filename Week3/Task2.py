students = [
    {"name": "Sara", "score": 75},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 80}
]

def validate_score(score):
    if 0 <= score <= 100:
        return True
    else:
        return False
    
# calculate grade
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# calculate average score
def ave_score(students):
    sum = 0
    for score in students:
        sum += score["score"]
    ave = sum / len(students)
    return ave
    
# print(ave_score(students))

#find highest and lowest score
def highesLowest_score(students):
    lowest = students[0]["score"]
    highest = students[0]["score"]
    for i in range(len(students)):
        if students[i]["score"] < lowest:
            lowest = students[i]["score"]
        if students[i]["score"] > highest:
            highest = students[i]["score"]
    return highest, lowest

# print(highesLowest_score(students))

# count pass and fail student
def passAndFailCount(students):
    pas = 0
    fail = 0
    for i in range(len(students)):
        if students[i]["score"] >=50:
            pas += 1
        else:
            fail += 1
    return pas, fail
print(passAndFailCount(students))

# above average
def above_ave(students):
    ave = ave_score(students)
    above_ave = []
    for student in students:
        if student["score"] > ave:
            above_ave.append(student["name"])
    return above_ave

# report 
def generate_report(students):
    #check validation
    for student in students:
        if not validate_score(student["score"]):
            print(f"invalid score for {student["name"]}: {student["score"]}")
            return

    print("========== STUDENT REPORT==========")

    for student in students:
        name = student["name"]
        score = student["score"]
        grade = calculate_grade(score)

        print(f"Name: {name}, Score: {score} Grade: {grade}")

    average = ave_score(students)
    highest, lowest = highesLowest_score(students)
    passed, fail = passAndFailCount(students)
    above_average = above_ave(students)

    print(f"\naverage: {average:.2f}")
    print(f"highest score: {highest}")
    print(f"lowest score: {lowest}")
    print(f"passed student: {passed}")
    print(f"failed student: {fail}")
    print(f"above average: {above_average}")
    

generate_report(students)




