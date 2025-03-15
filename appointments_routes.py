from flask import Blueprint, render_template
from sqlalchemy import insert, select
from .database import db
from .models import Appointments

# HTML FILES
APPOINTMENT_HTML = 'appointments.html'

appointment_records_bp = Blueprint('appointments', __name__)

@appointment_records_bp.route("/appointments")
def appointments():
    stmt_patient_appointments = select(Appointments)
    result = db.session.execute(stmt_patient_appointments).scalars().all()
    
    db_appointment_records = [
        {
            "AppointmentID": appointment_record.AppointmentID,
            "PatientID": appointment_record.PatientID,
            "DoctorID": appointment_record.DoctorID,
            "AppointmentDate": appointment_record.AppointmentDate,
            "Status": appointment_record.Status,
        }
        for appointment_record in result
    ]
    
    return render_template(
        APPOINTMENT_HTML,
        appointments=db_appointment_records
    )