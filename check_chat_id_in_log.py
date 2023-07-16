chat_ids = set()

with open("log.log") as file_log:
    for line in file_log:
        log_sting = line.split(":")
        if log_sting[3] == "INFO" and log_sting[4] != "":
            chat_ids.add(log_sting[4].split()[2])

print("List of chat ids:")
for i in chat_ids:
    print(i)