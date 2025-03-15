from .database import db
from sqlalchemy import insert, select
from .models import Patients, Doctors, MedicalRecords, Appointments, Billing


def prepopulate_records_into_patient_table():
    stmt_patient = [
        insert(Patients).values((1, 'Paul', 'Peckem', '1991-05-19',
                                    'M', '004352323', '4 Mail Avenue Nanterre')),
        insert(Patients).values((2, 'Richard', 'Parker', '1994-06-16',
                                    'M', '8967567', '8 PLACE du 8 mai, Mantes')),
        insert(Patients).values((3, 'Ayn', 'Rand', '1997-09-01',
                                    'F', '5875844567', '9 Boulevard avenue coltier')),

        insert(Patients).values((4, 'Peter', 'Griffith', '1998-01-02',
                                    'M', '475483563', 'Rue Etienne Marcel, 78 ')),

        insert(Patients).values((5, 'Yossarian', 'Hamar', '1999-01-20',
                                    'M', '375436546', '10 Avenue du Droit'))
    ]

    for patient in stmt_patient:
        db.session.execute(patient)
        db.session.commit()


def prepopulate_records_into_doctors_table():
    stmt_doctors = [
        insert(Doctors).values(
            (1, 'Hans', 'Niemann', 'Cardiologist', '87657567')),
        insert(Doctors).values(
            (2, 'Elon', 'Musk', 'Neurologist', '567863463')),
        insert(Doctors).values((3, 'Bill', 'Gates', 'Obgyn', '35634674578')),
        insert(Doctors).values(
            (4, 'Peter', 'Thiel', 'Dermatologist', '32564576')),
        insert(Doctors).values(
            (5, 'Alex', 'Goodman', 'Dentist', '4846363564')),
    ]

    for doctor in stmt_doctors:
        db.session.execute(doctor)
        db.session.commit()


def prepopulate_records_into_appointments_table():
    stmt_appointments = [
        insert(Appointments).values(
            (1, 1, 1, '2025-03-15 10:00:00', 'Scheduled')),
        insert(Appointments).values(
            (2, 2, 1, '2025-03-18 10:00:00', 'Scheduled')),
        insert(Appointments).values(
            (3, 1, 2, '2025-03-19 10:00:00', 'Scheduled')),
        insert(Appointments).values(
            (4, 3, 4, '2025-03-20 10:00:00', 'Scheduled')),
        insert(Appointments).values(
            (5, 4, 5, '2025-03-21 10:00:00', 'Scheduled')),
    ]

    for appointment in stmt_appointments:
        db.session.execute(appointment)
        db.session.commit()


def prepopulate_records_into_medical_records_table():
    stmt_medical_records = [
        insert(MedicalRecords).values(
            (1, 1, 'Hypertension', 'Lifestyle changes and medication', 'Lisinopril', '2025-03-19 10:00:00')),
        insert(MedicalRecords).values(
            (2, 2, 'Short breath', 'Lifestyle changes', 'Lisinopril', '2025-03-19 10:00:00')),
        insert(MedicalRecords).values(
            (3, 3, 'Headache', 'Rest and good dieting', 'Doliprane', '2025-03-19 10:00:00')),
        insert(MedicalRecords).values(
            (4, 4, 'Escema', 'Clean and filtered water', 'Medicated Creams', '2025-03-19 10:00:00')),
        insert(MedicalRecords).values(
            (5, 5, 'Asthma', 'Mild excercises and occasional jogging', 'Rhinophil', '2025-03-19 10:00:00')),
    ]

    for medical_records in stmt_medical_records:
        db.session.execute(medical_records)
        db.session.commit()


def prepopulate_records_into_billing_records_table():
    stmt_billing = [
        insert(Billing).values(
            (1, 1, 550.00, 'Pending')),
        insert(Billing).values(
            (2, 2, 50.00, 'Paid')),
        insert(Billing).values(
            (3, 3, 750.00, 'Pending')),
        insert(Billing).values(
            (4, 4, 150.00, 'Paid')),
    ]

    for bill in stmt_billing:
        db.session.execute(bill)
        db.session.commit()
