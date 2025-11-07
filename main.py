from js import document
from pyscript import display

def getting_info(e):
    name = document.getElementById('input1').value
    section = document.getElementById('input2').value

    document.getElementById('info').innerHTML = ""

    display(f'{name} from {section}', target='info')

def calculating_grades(e):
    eng = float(document.getElementById("subj1").value)
    math = float(document.getElementById("subj2").value)
    sci = float(document.getElementById("subj3").value)
    fili = float(document.getElementById("subj4").value)
    pe = float(document.getElementById("subj5").value)
    ss = float(document.getElementById("subj6").value)
    mus = float(document.getElementById("subj7").value)
    ict = float(document.getElementById("subj8").value)
    tle = float(document.getElementById("subj9").value)
    ve = float(document.getElementById("subj10").value)

    name = document.getElementById('input1').value
    
    subjects = [eng, math, sci, fili, pe, ss, mus, ict, tle, ve]

    total = sum(subjects)
    average = total / len(subjects)

    document.getElementById('output').innerHTML = ""   
    
    display(f'{name}s Grades:', target='output')
    display(f' English: {eng}', target='output')
    display(f' Mathematics: {math}', target='output')
    display(f' Science: {sci}', target='output')
    display(f' Filipino: {fili}', target='output')
    display(f' Physical Education: {pe}', target='output')
    display(f' Social Studies: {ss}', target='output')
    display(f' Music: {mus}', target='output')
    display(f' ICT: {ict}', target='output')
    display(f' TLE: {tle}', target='output')
    display(f' Values Education: {ve}', target='output')


    display(subjects, target='output')
    display(f'Your final grade is {average:.2f}', target='output')
