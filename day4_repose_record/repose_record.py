import os
import datetime
from operator import itemgetter

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
        line_splitted = line.replace('[',"").replace(']',"").replace('\n',"").split(" ", 2)
        date_splitted = line_splitted[0].split("-")
        hour_splitted = line_splitted[1].split(":")
        line_timestamp = datetime.datetime(int(date_splitted[0]), int(date_splitted[1]), int(date_splitted[2]), int(hour_splitted[0]), int(hour_splitted[1]))
        data.append([line_timestamp, line_splitted[2]])

data.sort(key=itemgetter(0))

parsed_data = list()
current_parsed = [0] * 62
last_minute = 0
last_state = "."
for record in data:
    words = record[1].split(" ")
    if words[0] == "Guard":
        if current_parsed[61] != 0:
            for i in range(last_minute,60):
                current_parsed[i] = last_state
            parsed_data.append(current_parsed)
        current_parsed = [0] * 62
        if record[0].hour == 0:
            parse_date = datetime.date(record[0].year, record[0].month, record[0].day)
            current_parsed[60] = parse_date
        else:
            parse_date = datetime.date(record[0].year, record[0].month, record[0].day) + datetime.timedelta(days = 1)
            current_parsed[60] = parse_date
        current_parsed[61] = int(words[1].replace("#",""))
        last_minute = 0
    elif words[0] == "falls":
        change_minute = record[0].minute
        for i in range(last_minute, change_minute):
            current_parsed[i] = "."
        last_minute = change_minute
        last_state = "#"
    elif words[0] == "wakes":
        change_minute = record[0].minute
        for i in range(last_minute, change_minute):
            current_parsed[i] = "#"
        last_minute = change_minute
        last_state = "."

guards_set = set([item[61] for item in parsed_data])

guard_report = list()
for guard in guards_set:
    current_guard = [0] * 3
    current_guard[0] = guard
    subset = [record for record in parsed_data if record[61] == guard]
    total_sleep = 0
    top_min = -1
    sleep_top_min = 0
    for i in range(0,60):
        sleep_min = 0
        for record in subset:
            if record[i] == "#":
                total_sleep += 1
                sleep_min += 1
        if sleep_min > sleep_top_min:
            top_min = i
            sleep_top_min = sleep_min
    current_guard[1] = total_sleep
    current_guard[2] = top_min
    guard_report.append(current_guard)

guard_report.sort(key=itemgetter(1))
print(guard_report[-1][0]*guard_report[-1][2])