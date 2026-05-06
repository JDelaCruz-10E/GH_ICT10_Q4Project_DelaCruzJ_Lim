from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt
from js import document
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)


# removing the font cache message
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

days = np.array(['Mon', 'Tue', 'Wed', 'Thurs', 'Fri'])
absences = np.zeros(5, dtype=int)


def add_absence(e):
    document.getElementById('plot').innerHTML =  '    '
    day_index = int(document.getElementById("day").value)
    num_absences = int(document.getElementById("absences").value)

    absences[day_index] += num_absences

    plt.figure(figsize=(6,4))
    plt.plot(days, absences, marker="o", linestyle="-", color="palegoldenrod")
    plt.title("10-Emerald\'s Attendance Sheet")
    plt.xlabel("Days")
    plt.ylabel("Absences")

    display(plt.gcf(), target="plot")
    plt.close()

class classmate:
    def __init__(self, name, section, fav):
        self.name = name
        self.section = section
        self.fav = fav

    def introduce(self):
        return f"Hello I\'m {self.name} from {self.section}, I like to learn {self.fav}!"


classmates = [
    classmate("Joseph", "Emerald", "English"),
    classmate("Erin", "Emerald", "Philosophy"),
    classmate("Caitlyn", "Emerald", "English"),
    classmate("Kyla", "Emerald", "English"),
    classmate("Oscar", "Emerald", "TLE"),
    classmate("Casal", "Emerald", "TLE"),
    classmate("Coeli", "Emerald", "TLE"),
    classmate("David", "Emerald", "TLE"),
    classmate("De Mata", "Emerald", "Philosophy"),
    classmate("Dela Cruz F.", "Emerald", "Science"),
    classmate("Dela Cruz J.", "Emerald", "TLE"),
    classmate("Dellejero", "Emerald", "Philosophy"),
    classmate("Fukuda", "Emerald", "TLE"),
    classmate("Gozum", "Emerald", "TLE"),
    classmate("Lim", "Emerald", "Music"),
    classmate("Ibay", "Emerald", "TLE"),
    classmate("Lozano", "Emerald", "Filipino"),
    classmate("Mamauag", "Emerald", "Philosophy"),
    classmate("Navarro", "Emerald", "TLE"),
    classmate("Precones", "Emerald", "TLE"),
    classmate("Ramos", "Emerald", "TLE"),
    classmate("Sidhu", "Emerald", "Math"),
    classmate("Tiu", "Emerald", "TLE"),
    classmate("Villamayor", "Emerald", "TLE"),
    classmate("Zaragoza", "Emerald", "TLE")
]

def add(e):
    name = document.getElementById("classmate1").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    new_student = classmate(name, section, subject)
    classmates.append(new_student)

    display(f"{name} added successfully!", append=True, target='output')

def show(e):
    document.getElementById('output').innerHTML = " "

    for student in classmates:
        intro = student.introduce()
        display(intro, target='output')