def add_time(start, duration, weekday=None):
    week_dict = {
        1: 'monday',
        2: 'tuesday',
        3: 'wednesday',
        4: 'thursday',
        5: 'friday',
        6: 'saturday',
        7: 'sunday'
    }
    day_counter = 0
    start_time_elements = start.split()
    period = start_time_elements[1]
    start_time = start_time_elements[0].split(':')
    start_time_hour = int(start_time[0])
    start_time_minutes = int(start_time[1])
    duration_elements = duration.split(':')
    duration_hour = int(duration_elements[0])
    duration_minutes = int(duration_elements[1])
    if period == 'PM':
        start_time_hour = start_time_hour + 12
    if duration_hour > 24:
        day_counter = duration_hour // 24
        duration_hour = duration_hour % 24
    new_hour = start_time_hour + duration_hour
    new_minutes = start_time_minutes + duration_minutes
    if new_minutes > 60:
        temp_count = new_minutes // 60
        new_minutes = new_minutes % 60
        new_hour = new_hour + temp_count
    if new_hour > 24:
        temp_count = new_hour // 24
        new_hour = new_hour % 24
        day_counter = day_counter + temp_count
    if new_hour > 11:
        new_hour = new_hour - 12
        period = 'PM'
    else:
        period = 'AM'
    if weekday is not None:
        weekday = weekday.lower()
        for number, day in week_dict.items():
            if weekday == day:
                current_day_number = number
                print(current_day_number)
        if day_counter > 7:
            temp_count = day_counter % 7
            desired_day_number = current_day_number + temp_count
            if desired_day_number > 7:
                desired_day_number = desired_day_number % 7

        else:
            desired_day_number = current_day_number + day_counter
        weekday = week_dict[desired_day_number]
    if new_hour == 0:
        new_hour = 12
    new_hour = str(new_hour)
    new_minutes = str(new_minutes)
    if int(new_minutes) < 10:
        new_minutes = '0' + new_minutes
    if day_counter == 0:
        day_counter = ""
    elif day_counter == 1:
        day_counter = " (next day)"
    else:
        day_counter = " (" + str(day_counter) + " days later)"
    if weekday is None:
        new_time = new_hour + ':' + new_minutes + ' ' + period + day_counter
    else:
        weekday = weekday.capitalize()
        weekday = ", " + weekday
        new_time = new_hour + ':' + new_minutes + ' ' + period + weekday + day_counter
    return new_time


print(add_time("11:06 PM", "2:02"))
print(add_time("8:16 PM", "466:02", "tuesday"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("11:40 AM", "0:25"))
print(add_time("8:16 PM", "466:02", "tuesday"))
