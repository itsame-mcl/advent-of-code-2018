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
mins_report = list()
for guard in guards_set:
    subset = [record for record in parsed_data if record[61] == guard]
    for i in range(0,60):
        current_min = [0] * 3
        current_min[0] = guard
        current_min[1] = i
        for record in subset:
            if record[i] == "#":
                current_min[2] += 1
        mins_report.append(current_min)

mins_report.sort(key=itemgetter(2))
print(mins_report[-1][0]*mins_report[-1][1])