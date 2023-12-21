import datetime
import sched
import time
class PillReminder:
    def __init__(self):
        self.medication_schedule = {}
    def add_medication(self, medication_name, dosage, frequency):
        if medication_name not in self.medication_schedule:
            self.medication_schedule[medication_name] = {'dosage': dosage,         'frequency': frequency}
        else:
            print(f"{medication_name} is already in the schedule.")

    def set_reminder(self, medication_name, start_time):
        if medication_name in self.medication_schedule:
            frequency = self.medication_schedule[medication_name]['frequency']
            s = sched.scheduler(time.time, time.sleep)
            
            def remind():
                print(f"Time to take {medication_name}. Dosage: {self.medication_schedule[medication_name]['dosage']}")

            while True:
                s.enterabs(start_time, 1, remind, ())
                start_time += frequency * 60  # Frequency in minutes
                s.run()

if __name__ == "__main__":
    reminder_app = PillReminder()

    # Adding medications to the schedule
    reminder_app.add_medication("Aspirin", "1 tablet", 6)  # Example: every 6 minutes for testing purposes
    reminder_app.add_medication("Ibuprofen", "1 capsule", 10)  # Example: every 10 minutes for testing purposes
    # Setting reminder
    reminder_app.set_reminder("Aspirin", time.time())
    reminder_app.set_reminder("Ibuprofen", time.time())


class Doctor:
    def _init_(self, name, speciality):
        self.name = name
        self.speciality = speciality
        self.patient_records = {}

    def upload_details(self, patient_name, details):
        if patient_name not in self.patient_records:
            self.patient_records[patient_name] = details
            print(f"Details uploaded for {patient_name} by Dr. {self.name}")
        else:
            print(f"Details for {patient_name} already exist.")

    def view_patient_details(self, patient_name):
        if patient_name in self.patient_records:
            return self.patient_records[patient_name]
        else:
            return f"No details found for {patient_name}"

class Patient:
    def _init_(self, name):
        self.name = name
    def follow_doctor(self, doctor, details):
        doctor.upload_details(self.name, details)
    def view_details(self, doctor):
        return doctor.view_patient_details(self.name)
if __name__ == "_main_":
    # Creating a doctor
    doctor1 = Doctor("Smith", "Cardiologist")
    # Creating a patient
    patient1 = Patient("Alice")
    # Patient follows the doctor and uploads details
    patient1.follow_doctor(doctor1, "Heart condition, medication prescribed.")
    # Patient views details
    details = patient1.view_details(doctor1)
    print(f"Patient {patient1.name} details: {details}")
