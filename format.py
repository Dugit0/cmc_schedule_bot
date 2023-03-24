# ------------- Фил -------------
subjects = [
    [
        [''], 
        ['Французский Сем 1028'], 
        [''], 
        ['Языки мира Лек П11'], 
        ['История Лек 1060'], 
        ['Латинский Сем 1028']
    ],
    [
        [''], 
        ['Синтаксис Лек П11'], 
        ['Синтаксис Сем П11'], 
        ['Семантика Лек П11'], 
        ['Семантика Сем П11'], 
        ['']
    ],
    [
        [''], 
        ['Фонетика Лек/Сем П11'], 
        ['Физическая культура'], 
        ['Межфакультетские курсы']
    ],
    [
        [''], 
        [''], 
        ['Линал и мат анализ Лек 844'], 
        ['Линал и мат анализ Сем 844'], 
        ['Древнерусский Лек/Сем 844'], 
        ['']
    ],
    [
        [''], 
        ['Психология Лек 951'], 
        ['Физическая культура'], 
        ['Французский Сем 1028'], 
        ['Французский Сем 1028'], 
        ['Латинский Сем 1028']
    ],
    [
         ['-'], 
         ['-'], 
         ['-']
    ],
    [
         ['-'], 
         ['-'], 
         ['-']
    ]
]

times = [
    [['09:00', '10:30'], ['10:45', '12:15'], ['13:00', '14:30'], ['14:40', '16:10'], ['16:20', '17:50'], ['18:00', '19:30']],
    [['09:00', '10:30'], ['10:45', '12:15'], ['13:00', '14:30'], ['14:40', '16:10'], ['16:20', '17:50'], ['18:00', '19:30']],
    [['09:00', '10:30'], ['10:45', '12:15'], ['13:00', '14:30'], ['14:40', '17:50']],
    [['09:00', '10:30'], ['10:45', '12:15'], ['13:00', '14:30'], ['14:40', '16:10'], ['16:20', '17:50'], ['18:00', '19:30']],
    [['09:00', '10:30'], ['10:45', '12:15'], ['13:00', '14:30'], ['14:40', '16:10'], ['16:20', '17:50'], ['18:00', '19:30']],
    [['-'], ['-'], ['-']],
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















