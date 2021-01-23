def add_time(start, duration, sday=" "):
    sday=sday.lower()
    sday=sday.capitalize()
    days = ["","Monday", "Tuesday" , "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    eDayCounter=0

    start = start.split(":")
    bHour = start[0] #string
    bHour = int(bHour)

    MaT = start[1].split(" ")
    bMin = MaT[0] #string
    bMin = int(bMin)

    bT = MaT[1] #string
    if bT=="PM":
        bHour+=12

    duration = duration.split(":")
    dHour = duration[0] #string
    dHour = int(dHour)
    eDayCounter+=dHour//24

    dMin = duration[1] #string
    dMin = int(dMin)

    x = bHour + (dHour%24)
    y = bMin + dMin
    if(y>=60):
        x+=1
    if(x>=24):
        eDayCounter+=1

    aMin = bMin + dMin
    eHour = aMin//60
    aMin = aMin%60 #Final Minute

    aHour = bHour + dHour + eHour
    dDay = aHour//24
    m = aHour%24
    if aHour%24==0:
        aHour=12
    else:
        aHour=aHour%24
    if m>=12:
        aT = "PM"
    else:
        aT = "AM"
    if aHour>12:
        aHour = aHour%12 #Final Hour

    if(len(str(aMin))==1):
        aMin="0"+str(aMin)
    write=str(aHour)+":"+str(aMin)+" "+aT

    if sday!=" ":
        aDay = days.index(sday) + dDay
        if(aDay>7):
            aDay = aDay%7
        aDay = days[aDay] #Final Day
        write+=", {}".format(aDay)
    
    if(eDayCounter>0):
        if(eDayCounter==1):
            write+=" (next day)"
        else:
            write+=" ({} days later)".format(eDayCounter)
    
    return write