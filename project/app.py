from student import *

students_list = []
user_input = ""
while user_input != 'q':
    user_input = input("Give command (press h for help, q to exit): ")
    if user_input == 'a':    
        name = input("Student name: ")
        lastname = input("Student lastname: ")
        id = input("Student id: ")
        std = Student(name, lastname, id, {}, [])
        students_list.append(std)
    elif user_input == 'h':
        print("Press a to add new student. ")
        print("Press q to exit the program. ")
        print("Press l to list students. ")
        print("Write attendance for attendance. ")
        print("Press g for grades. ")
    elif user_input == 'l':
        for x in students_list:
            print(x.get_name())
            print(x.get_courses())
            print(x.get_attendance())
    elif user_input == 'attendance':
        inp = input("C to check attendance, A to add attendance: ")
        if inp == 'A':
            for x in students_list:
                inp = input("{} for here write H for missing write M: ".format(x.get_name()))
                if inp == 'H':
                    x.get_attendance().append(True)
                elif inp == "M":
                    x.get_attendance().append(False)
        elif inp == 'C':
            for x in students_list:
                print(x.get_name(), x.get_attendance())
    elif user_input == 'g':
        id_input = input("Please provide user id: ")
        for x in students_list:
            if id_input == x.get_id():
                course_input = input(x.get_name() + " found, provide course name: ")
                x.get_courses()[course_input] = []
                for i in range(1, 4):
                    grade_input = input("Write grade " + str(i) + " for " + course_input + " ")
                    x.get_courses()[course_input].append(int(grade_input))
        


