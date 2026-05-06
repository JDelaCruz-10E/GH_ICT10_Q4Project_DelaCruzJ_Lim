from pyscript import display, document


class classmate:
    def __init__(self, name, section, fav):
        self.name = name
        self.section = section
        self.fav = fav

    def introduce(self):
        return f"Hello I\'m {self.name} from {self.section}, I like to learn {self.fav}!"


classmates = [
    classmate("Joseph", "Emerald", "TLE"),
    classmate("Erin", "Emerald", "Philosophy"),
    classmate("Caitlyn", "Emerald", "TLE"),
    classmate("Kyla", "Emerald", "English"),
    classmate("Oscar", "Emerald", "TLE"),
    classmate("Casal", "Emerald", "TLE"),
    classmate("Coeli", "Emerald", "TLE"),
    classmate("David", "Emerald", "TLE"),
    classmate("De Mata", "Emerald", "TLE"),
    classmate("Dela Cruz F.", "Emerald", "TLE"),
    classmate("Dela Cruz J.", "Emerald", "TLE"),
    classmate("Dellejero", "Emerald", "Philosophy"),
    classmate("Fukuda", "Emerald", "TLE"),
    classmate("Gozum", "Emerald", "TLE"),
    classmate("Lim", "Emerald", "TLE"),
    classmate("Ibay", "Emerald", "TLE"),
    classmate("Lozano", "Emerald", "Filipino"),
    classmate("Mamauag", "Emerald", "Philosophy"),
    classmate("Navarro", "Emerald", "TLE"),
    classmate("Precones", "Emerald", "TLE"),
    classmate("Ramos", "Emerald", "TLE"),
    classmate("Sidhu", "Emerald", "TLE"),
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
