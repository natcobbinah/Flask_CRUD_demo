from flask import Blueprint, render_template
from sqlalchemy import insert, select
from .database import db
from .models import MedicalRecords

# HTML FILES
MEDICAL_RECORDS_HTML = 'medical_records.html'

medical_records_bp = Blueprint('medical_records', __name__)

@medical_records_bp.route("/medical_records")
def medical_records():
    stmt_medical_records = select(MedicalRecords)
    result = db.session.execute(stmt_medical_records).scalars().all()

    db_medical_records = [
        {
            "RecordID": medical_record.RecordID,
            "PatientID": medical_record.PatientID,
            "Diagnosis": medical_record.Diagnosis,
            "Treatment": medical_record.Treatment,
            "Prescription": medical_record.Prescription,
            "DateRecorded": medical_record.DateRecorded,
        }
        for medical_record in result
    ]

    return render_template(
        MEDICAL_RECORDS_HTML,
        medical_records=db_medical_records,
    )