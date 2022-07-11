def add_time(current_time,added_time):
    added_time=added_time.split(":")
    current_time=current_time.split(":")
    if int(current_time[1])>60 or int(added_time[1])>60:
        raise Exception("Minutes is greater than 60")
    hours=int(current_time[0])+int(added_time[0])
    if hours>24:
        h=hours
        while h>24:
            h-=24
        hours=h
        if hours>12:
            hours=hours-12
    elif hours>12:
        hours=hours-12
    minutes=int(current_time[1])+int(added_time[1])
    if minutes>=60:
        hours+=(minutes//60)
        minutes=(minutes%60)
    if hours>12:
        hours=hours-12
    if minutes<10 and hours<10:
        return f"0{hours}:0{minutes}"
    elif minutes<10:
        return f"{hours}:0{minutes}"
    return f"{hours}:{minutes}"      
current_time=input("Enter the Current Time: ")
added_time=input("Enter the added time: ")
print("The Time is",add_time(current_time, added_time))