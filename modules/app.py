from utils.math_utils import max_average
from classes.student import Student

agoni = Student("Agon", "Cecelia", "agonn.c@gmail.com", "127488", 7.89)
bislimi = Student("Bislim", "Bislimi", "bislimi.b@gmail.com", "127388", 6.78)
ahmeti = Student("Ahmet", "Ahmeti", "a.ahmeti@gmail.com", "127332", 7.12)

lista = []
lista.append(agoni)
lista.append(bislimi)
lista.append(ahmeti)

max_avg_student = max_average(lista)

print("{} {} me mesataren: {}".format(max_avg_student.first_name, max_avg_student.last_name, max_avg_student.average))