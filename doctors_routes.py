from flask import Blueprint, render_template
from sqlalchemy import insert, select
from .database import db
from .models import Doctors

# HTML FILES
DOCTORS_HTML = 'doctors.html'

doctors_records_bp = Blueprint('doctors', __name__)

@doctors_records_bp.route("/doctors")
def doctors():
    stmt_doctors_records = select(Doctors)
    result = db.session.execute(stmt_doctors_records).scalars().all()

    db_doctors = [
        {
            "DoctorID": doctor_record.DoctorID,
            "FirstName": doctor_record.FirstName,
            "LastName": doctor_record.LastName,
            "Specialization": doctor_record.Specialization,
            "ContactNumber": doctor_record.ContactNumber,
        }
        for doctor_record in result
    ]

    return render_template(
        DOCTORS_HTML,
        doctors=db_doctors
    )
