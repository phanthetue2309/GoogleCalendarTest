from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def main():
   # creates one hour event tomorrow 10 AM IST
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, 9)+timedelta(days=2)
   # params = 10 is at 10 o'clock
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=2)).isoformat()
   # timedelta(hours=1) will be 10h + 1h 

   event_result = service.events().insert(calendarId='primary',
       body={
            "summary": 'Team Core Meeting ',
            "description": 'This is a meeting of team core',
            "start": {"dateTime": start, "timeZone": 'Asia/Ho_Chi_Minh'},
            "end": {"dateTime": end, "timeZone": 'Asia/Ho_Chi_Minh'},
        }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
   main()