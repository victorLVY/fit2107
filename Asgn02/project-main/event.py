
from datetime import date

# variables: may wanna change location. 
event_rec = []
cancel_event = []


class EventType:
    OFFICIAL = "official"
    ONLINE = "online"
    PHYSICAL = "physical"

class Event():
    def __init__(self,
                event_id,
                name,
                location,
                attendees,
                date):
               # reminders,
               # creator=None,
               # organizer=None):
        #raise NotImplementedError
        self.event_id = event_id
        self.name = name
        self.location = location
        self.attendees = attendees
        self.date = date

    def del_event(event):
        today = date.today()
        event_date = event.date
        flag = False
        if (event_date < today):
            # allow delettion
            # i think we need to store it somewhere, need to decide and ask them later. 
            #del(event)
            event_rec.remove(event)
            flag = True
        return flag
    def cancel_event(event):
        #del(event)
        # check if event exists first
        flag = False
        temp_event = event if (event in event_rec) else None
        if (temp_event != None):
            # delete from event record
            event_rec.remove(temp_event)
            cancel_event.append(temp_event)
            flag = True
        #event_rec.remove(temp_event), cancel_event.append(temp_event)
        return flag
    
    # extra not sure need or not, from cancel_event. 
    def restore_event(event):
        flag = False

        return flag

    # event location is abit special and needs to be check during init.

        
        