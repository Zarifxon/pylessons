class DOOR_STATUS:
    opening = 1 
    closing = -1 
    stopped = 0 


def controller(events):
    time = len(events)
    for second in range(time): 
        event = events[second]
        status = DOOR_STATUS.stopped
        height = 0

        if(event == "."): continue
        if(event = "P"):
            if(height == 0):
                

