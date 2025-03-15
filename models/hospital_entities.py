from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from maurs_hospital.database import db
from sqlalchemy import DateTime
import datetime
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Patients(db.Model):
    __tablename__ = "Patients_041"

    PatientID: Mapped[int] = mapped_column(primary_key=True)
    FirstName: Mapped[str]
    LastName: Mapped[str]
    DOB: Mapped[str]
    Gender: Mapped[str]
    ContactNumber: Mapped[str]
    Address: Mapped[str]


class Doctors(db.Model):
    __tablename__ = "Doctors_041"

    DoctorID: Mapped[int] = mapped_column(primary_key=True)
    FirstName: Mapped[str]
    LastName: Mapped[str]
    Specialization: Mapped[str]
    ContactNumber: Mapped[str]


class Appointments(db.Model):
    __tablename__ = "Appointments_041"

    AppointmentID: Mapped[int] = mapped_column(primary_key=True)
    PatientID: Mapped[int] = mapped_column(ForeignKey("Patients_041.PatientID"))
    DoctorID: Mapped[int] = mapped_column(ForeignKey("Doctors_041.DoctorID"))
    AppointmentDate: Mapped[str]
    Status: Mapped[str]
    # FOREIGN KEY (PatientID) REFERENCES Patients_041(PatientID),
    # FOREIGN KEY (DoctorID) REFERENCES Doctors_041(DoctorID)


class MedicalRecords(db.Model):
    __tablename__ = "MedicalRecords_041"

    RecordID: Mapped[int] = mapped_column(primary_key=True)
    PatientID: Mapped[int] = mapped_column(ForeignKey("Patients_041.PatientID"))
    Diagnosis: Mapped[str]
    Treatment: Mapped[str]
    Prescription: Mapped[str]
    DateRecorded: Mapped[str]
    # PatientID: Mapped[int] = mapped_column(ForeignKey("Patients_041.PatientID"))
    # FOREIGN KEY (PatientID) REFERENCES Patients_041(PatientID)


class Billing(db.Model):
    __tablename__ = "Billing_041"

    BillID: Mapped[int] = mapped_column(primary_key=True)
    PatientID: Mapped[int] = mapped_column(ForeignKey("Patients_041.PatientID"))
    Amount: Mapped[float]
    PaymentStatus: Mapped[str]
    # FOREIGN KEY (PatientID) REFERENCES Patients_041(PatientID)
