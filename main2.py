from js import document

def compute_grade(event):
    event.preventDefault()

    subjects = ["science", "english", "ict", "math", "filipino", "pe"]
    grades = [float(document.getElementById(s).value or 0) for s in subjects]
    average = sum(grades) / len(grades)

    first = document.getElementById("first").value
    last = document.getElementById("last").value

    document.getElementById("show1").innerText = f"{first} {last}'s Average Grade is:"
    document.getElementById("show2").innerText = f"{average:.2f}"


