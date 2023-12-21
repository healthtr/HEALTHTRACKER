import datetime
import sched
import time
class PillReminder:
def _init_(self):
  self.medication_schedule ={}
def add_medication(self, medication_name, dosage, frequency): if medication_name not in
self.medication_schedule:
self.medication_schedule [medication_ name] = {'dosage': dosage, 'frequency': frequency}
else:
print(f"{medication_name} is already in the schedule.")
def set_reminder (self,medication_name, start_time): 
if medication_name in
  self.medication_schedule:
frequency =self.medication_schedule[medication_name]['frequency']
S =sched.scheduler(time.time time.sleep) ,
def remind():
print(f"Time to take {medication_name}. Dosage: (self.medication_schedule[medication _name]['dosage']}")
while True:
s.enterabs(start_time, 1, remind, ())
start_time += frequency * 60 # Frequency in minutes
s.run()
if _name_ == "_main_":
reminder_app PillReminder()
# Adding medications to the schedule
reminder_app.add_medication("Aspirin ", "1 tablet", 6) # Example: every 6 minutes for testing purposes
reminder_app.add_medication("Ibuprof en", "1 capsule", 10) # Example: every 10 minutes for testing purposes
# Setting reminders
reminder_app.set_reminder("Aspirin", time.time())
reminder_app.set_reminder("Ibuprofen time.time())
