from models import db, TimeSlot, ModuleSession
import random
from datetime import datetime, timedelta
from sqlalchemy import and_

# Lower and upper limits for start and end times
lower_limit = datetime.strptime("08:00:00", "%H:%M:%S")
upper_limit = datetime.strptime("17:00:00", "%H:%M:%S")
days_of_week = list(range(5))

def run(all_modules):
    for module in all_modules:
        for _ in range(3):
            random_day = random.choice(days_of_week)
            # Generate a random start time
            random_hour = random.randint(lower_limit.hour, upper_limit.hour)
            random_start_time = lower_limit.replace(hour=random_hour, minute=0)
            # Generate a random duration (1 or 2 hours)
            duration_hours = random.choice([1, 2])
            # Calculate the end time
            random_end_time = random_start_time + timedelta(hours=duration_hours)

            date = random_start_time + timedelta(days=random_day)
            # Format the times as strings
            day = date.strftime("%A")
            start_time = random_start_time.time()
            end_time = random_end_time.time()

            if not db.session.query(TimeSlot).filter(and_(TimeSlot.day == day, TimeSlot.module_id == module.id)).first():
                new_timeslot = TimeSlot(day=day, start_time=start_time, end_time=end_time, module_id=module.id)
                db.session.add(new_timeslot)

    db.session.commit()
