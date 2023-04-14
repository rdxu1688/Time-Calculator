def add_time(start, duration, week_day = ""):
    s = start.split(" ")[0].split(":")
    d = duration.split(":")
    M = start.split(" ")[1]
    n_days = 0
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if M != 'AM' and M != 'PM':
        return "Error: time of day needs to be AM or PM"

    hour = int(s[0])
    minute = int(s[1])
    hour_change = int(d[0])
    minutes_change = int(d[1])

    hour += hour_change
    minute += minutes_change

    while minute > 60:
        minute -= 60
        hour += 1

    while hour > 11:
        hour -= 12
        if M == "PM":
            M = "AM"
            n_days += 1
        else:
            M = "PM"
    
    if minute < 10:
        minute_format = "0" + str(minute)
    else:
        minute_format = str(minute)
    
    if n_days == 0:
        days_later = ""
    elif n_days == 1:
        days_later = " (next day)"
    else:
        days_later = f" ({n_days} days later)"

    index = n_days%7
    i = 0
    hit = False
    for day in week:
        if week_day.lower() == day.lower():
            index += i
            hit = True
            break
        i += 1

    while index > 6:
        index -= 7
    
    if hit:
        week_day = ", " + week[index]

    if hour == 0:
        hour += 12

    new_time = str(hour) + ":" + minute_format + " " + M + week_day + days_later
    return new_time