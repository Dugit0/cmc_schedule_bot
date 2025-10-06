from schedule_source import schedules

import os


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


def format(schedule_name, subjects, times):
    char_in_str = 21
    f_out = open(os.path.join('schedules', schedule_name + '.txt'), "w", encoding="utf-8")
    names_of_days = {0: 'Пн', 1: 'Вт', 2: 'Ср', 3: 'Чт', 4: 'Пт', 5: 'Сб', 6: 'Вс'}
    for day in range(7):
        print("#", file=f_out)
        flag_separator = False
        print(f"*{names_of_days[day]} | {schedule_name}*", file=f_out)
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

for key in schedules:
    format(key, schedules[key][0], schedules[key][1])
