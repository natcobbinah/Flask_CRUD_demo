from flask import Flask, render_template, request, redirect, url_for, jsonify
from .database import db
from flask_font_awesome import FontAwesome
from .db_data import (
    prepopulate_records_into_patient_table,
    prepopulate_records_into_doctors_table,
    prepopulate_records_into_appointments_table,
    prepopulate_records_into_medical_records_table,
    prepopulate_records_into_billing_records_table,
)
from .models import Patients, Doctors, MedicalRecords, Appointments, Billing
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap5
from sqlalchemy import insert, select
from .routes import (
    appointment_records_bp,
    billing_records_bp,
    doctors_records_bp,
    medical_records_bp,
    patient_bp,
    homepage_bp,
)


app = Flask(__name__)
app.config.from_object("maurs_hospital.settings")

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)
font_awesome = FontAwesome(app)


# init database
db.init_app(app)

# database connection
with app.app_context():
    db.drop_all()
    db.create_all()

    prepopulate_records_into_patient_table()
    prepopulate_records_into_doctors_table()
    prepopulate_records_into_appointments_table()
    prepopulate_records_into_medical_records_table()
    prepopulate_records_into_billing_records_table()

# register routes
app.register_blueprint(homepage_bp)
app.register_blueprint(billing_records_bp)
app.register_blueprint(doctors_records_bp)
app.register_blueprint(medical_records_bp)
app.register_blueprint(patient_bp)
app.register_blueprint(appointment_records_bp)

if __name__ == "__main__":
    app.run()
