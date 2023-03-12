# ------------- Мех212 -------------
subjects = [
    [
        ['Действительный анализ П4'], 
        ['Дифференциальная геометрия П4'], 
        ['Мат анализ 447'], 
        ['Английский 449']
    ],
    [
        ['Дифференциальная геометрия 405'], 
        ['Мат анализ П4'], 
        ['Физическая культура'], 
        ['Английский 449'],
        ['Практикум 1610 / ---']

    ],
    [
        ['Диффуры П4'], 
        ['--- / Практикум 1305'], 
        ['Теорвер П4'], 
        ['Межфакультетские курсы']
    ],
    [

        ['-'], 
        ['-'], 
        ['-'], 
        ['-']

    ],
    [
        ['Работа на ЭВМ П4'], 
        ['Мат анализ П4'], 
        ['Физическая культура'], 
        ['Мат анализ 1415']
    ],
    [
        ['Теорвер 404'], 
        ['Диффуры 404'], 
        ['Практикум на ЭВМ 445'], 
        ['Действительный анализ 406']
    ],
    [
         ['-'], 
         ['-'], 
         ['-']
    ]
]

times = [
    [['09:00', '10:35'], ['10:45', '12:20'], ['13:15', '14:50'], ['15:00', '16:35']],
    [['09:00', '10:35'], ['10:45', '12:20'], ['13:15', '14:50'], ['15:00', '16:35'], ['16:40', '18:15']],
    [['09:00', '10:35'], ['10:45', '12:20'], ['13:15', '14:50'], ['15:00', '16:35']],
    [['09:00', '10:35'], ['10:45', '12:20'], ['13:15', '14:50'], ['15:00', '16:35']],
    [['09:00', '10:35'], ['10:45', '12:20'], ['13:15', '14:50'], ['15:00', '16:35']],
    [['09:00', '10:35'], ['10:45', '12:20'], ['13:15', '14:50'], ['15:00', '16:35']],
    [['-'], ['-'], ['-']]
    ]






def add_str(arr, max_len, template_str):
    for i in range(len(arr), max_len):
        arr.append(template_str)
    return arr

def split(s, max_len):
    l = s.split()
    res = []
    buf = ""
    for i in l:
        if len(buf) == 0:
            buf = i
        elif len(buf) + 1 + len(i) < max_len:
            buf += " " + i
        else:
            res.append(buf)
            buf = i
    if len(buf) > 0:
        res.append(buf)
    return res


char_in_str = 21
f_out = open("schedule.txt", "w", encoding="utf-8")
for day in range(7):
    # print(f"-------------- day {day + 1} --------------")
    # print(f"/set {day + 1}")
    print("#", file=f_out)
    flag_separator = False
    print("```", file=f_out)
    for time, subj in zip(times[day], subjects[day]):
        if flag_separator:
            print("-------------", file=f_out)
        flag_separator = True
        new_subj = []
        for i in range(len(subj)):
            new_subj.extend(split(subj[i], char_in_str))
        subj = new_subj
        max_len = max(len(time), len(subj))
        add_str(time, max_len, "     ")
        add_str(subj, max_len, "")
        for i, j in zip(time, subj):
            print(f"{i} | {j}", file=f_out)
    print("```", file=f_out)
print("#", file=f_out)
f_out.close()















