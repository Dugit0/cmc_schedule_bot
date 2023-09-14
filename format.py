# ------------- CMC321 -------------
subjects = [
    [
        [''], 
        ['Уравнения мат физики П-13'], 
        ['Прикладная алгебра П-8а'], 
        ['Уравнения мат физики 607'], 
        ['Язык Python П-5'], 
        ['']
    ],
    [
        ['Экономика П-8а'], 
        ['Экономика 658'], 
        ['Практикум МЗ-4', '(с 19-го МЗ-2)'], 
        ['ИМИРИС 582'], 
        ['ИМИРИС 582'], 
        ['']
    ],
    [
        ['Введение в сети ЭВМ П-14'], 
        ['Введение в сети ЭВМ П-14'], 
        ['Методы машинного обучения П-6'], 
        ['Межфакультетские курсы'], 
        [''], 
        ['']
    ],
    [
        ['--- / СКиПОД П-8а'], 
        ['СКиПОД П-8а'], 
        ['Базы данных П-14'], 
        ['Базы данных П-14'], 
        [''], 
        ['']
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
    ],
    [
        ['-'], 
        ['-'], 
        ['-']
    ]
]

times = [
    [['08:45', '10:20'], ['10:30', '12:05'], ['12:50', '14:25'], ['14:35', '16:10'], ['16:20', '17:55'], ['18:00', '19:30']],
    [['08:45', '10:20'], ['10:30', '12:05'], ['12:50', '14:25'], ['14:35', '16:10'], ['16:20', '17:55']],
    [['08:45', '10:20'], ['10:30', '12:05'], ['12:50', '14:25'], ['15:10', '18:30']],
    [['08:45', '10:20'], ['10:30', '12:05'], ['12:50', '14:25'], ['14:35', '16:10'], ['16:20', '17:55']],
    [['08:45', '10:20'], ['10:30', '12:05'], ['12:50', '14:25'], ['14:35', '16:10'], ['16:20', '17:55']],
    [['08:45', '10:20'], ['10:30', '12:05'], ['12:50', '14:25'], ['14:35', '16:10']],
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















