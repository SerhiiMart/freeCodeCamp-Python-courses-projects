def add_time(start, durr, week_day = False):
    days_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    durr_tuple = durr.partition(":")
    hours = int(durr_tuple[0])
    minutes = int(durr_tuple[2])
    
    start_tuple = start.partition(":")
    start_minutes_tuple = start_tuple[2].partition(" ")
    start_hours = int(start_tuple[0])
    start_minutes = int(start_minutes_tuple[0])
    am_or_pm = start_minutes_tuple[2]
    am_and_pm_flip = {"AM": "PM", "PM": "AM"}

    amount_of_days = int(hours / 24)
    
    end_minutes = start_minutes + minutes
    if(end_minutes >= 60):
      start_hours += 1
      end_minutes = end_minutes % 60
    amount_of_am_pm_flips = int((start_hours + hours) / 12)
    end_hours = (start_hours + hours) % 12
    end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)
    end_hours = end_hours = 12 if end_hours == 0 else end_hours
    if(am_or_pm == "PM" and start_hours + (hours % 12) >= 12):
      amount_of_days += 1

    am_or_pm = am_and_pm_flip[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm
    
    new_time = str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm 
    if(week_day):
      week_day = week_day.lower()
      index = int((days_index[week_day]) + amount_of_days) % 7
      new_day = week_days[index]
      new_time += ", " + new_day
      
    print("end_hours " + str(end_hours))
    print("end_minutes " + str(end_minutes))
    if(amount_of_days == 1):
      return new_time + " " + "(next day)"
    elif(amount_of_days > 1):
      return new_time + " (" + str(amount_of_days) + " days later)" 

    return new_time