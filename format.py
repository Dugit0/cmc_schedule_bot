schedule_name = 'Geo308'
from schedule_source import subjects_Geo308 as subjects
from schedule_source import times_Geo308 as times



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


char_in_str = 21
f_out = open(os.path.join('schedules', schedule_name + '.txt'), "w", encoding="utf-8")
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
