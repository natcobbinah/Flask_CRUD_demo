from flask import Blueprint, render_template, redirect, request, url_for, flash
from sqlalchemy import insert, select, delete, update
from maurs_hospital.database import db
from maurs_hospital.models import Patients
from maurs_hospital.forms import PatientForm
from werkzeug.datastructures import MultiDict

# HTML FILES
PATIENTS_HTML = "patients.html"

patient_bp = Blueprint("patients", __name__)


@patient_bp.route("/patients", methods=["GET", "POST"])
def patients():
    patients_form = PatientForm()

    stmt_patient_records = select(Patients)
    result = db.session.execute(stmt_patient_records).scalars().all()

    db_patients = [
        {
            "PatientID": patient_record.PatientID,
            "FirstName": patient_record.FirstName,
            "LastName": patient_record.LastName,
            "DOB": patient_record.DOB,
            "Gender": patient_record.Gender,
            "ContactNumber": patient_record.ContactNumber,
            "Address": patient_record.Address,
        }
        for patient_record in result
    ]

    # create/edit record
    if patients_form.validate_on_submit():
        form_data = request.form
        user_id_to_edit = request.args.get("user_id")

        create_new_patient_or_update_record(form_data, user_id_to_edit)

        return redirect(url_for("patients.patients"))

    # prepopulated edit record forms
    if request.args.get("edit") == "yes":
        user_id_to_edit = request.args.get("user_id")

        edit_form = prepopulate_form_fields(user_id_to_edit)
        return render_template(PATIENTS_HTML, patients=db_patients, form=edit_form)

    return render_template(PATIENTS_HTML, patients=db_patients, form=patients_form)


@patient_bp.route("/patients/<int:patientId>")
def delete_patients_record(patientId):
    patient_id_toDelete = int(patientId)

    stmt = delete(Patients).where(Patients.PatientID == patient_id_toDelete)
    db.session.execute(stmt)
    db.session.commit()

    flash('Patient record was deleted successfully')
    return redirect(url_for("patients.patients"))


def prepopulate_form_fields(user_id_to_edit:int) -> PatientForm :
    stmt_patient_records = select(Patients).where(Patients.PatientID == user_id_to_edit)
    result = db.session.execute(stmt_patient_records).scalars().all()

    db_patients = [
        {
            "PatientID": patient_record.PatientID,
            "FirstName": patient_record.FirstName,
            "LastName": patient_record.LastName,
            "DOB": patient_record.DOB,
            "Gender": patient_record.Gender,
            "ContactNumber": patient_record.ContactNumber,
            "Address": patient_record.Address,
        }
        for patient_record in result
    ]

    patients_form = PatientForm(
        formdata=MultiDict(
            [
                ("PatientID", db_patients[0]["PatientID"]),
                ("FirstName", db_patients[0]["FirstName"]),
                ("LastName", db_patients[0]["LastName"]),
                ("DOB", db_patients[0]["DOB"]),
                ("Gender", "Male" if db_patients[0]["Gender"] == "M" else "Female"),
                ("ContactNumber", db_patients[0]["ContactNumber"]),
                ("Address", db_patients[0]["Address"]),
            ]
        )
    )

    return patients_form


def create_new_patient_or_update_record(form_data: MultiDict, user_id_to_edit: int) -> None:
    current_patient_table_index = db.session.query(Patients).count()

    if user_id_to_edit is not None:
        stmt_patient_records = select(Patients).where(
            Patients.PatientID == user_id_to_edit
        )

        if db.session.execute(stmt_patient_records).first() is not None:
            stmt = (
                update(Patients)
                .where(Patients.PatientID == user_id_to_edit)
                .values(
                    (
                        user_id_to_edit,
                        form_data["FirstName"],
                        form_data["LastName"],
                        form_data["DOB"],
                        form_data["Gender"],
                        form_data["ContactNumber"],
                        form_data["Address"],
                    )
                )
            )
            db.session.execute(stmt)
            db.session.commit()

            flash('Patient record was updated successfully')
    else:

        insert_current_record_to_patient_table = insert(Patients).values(
            (
                current_patient_table_index + 1,
                form_data["FirstName"],
                form_data["LastName"],
                form_data["DOB"],
                form_data["Gender"],
                form_data["ContactNumber"],
                form_data["Address"],
            )
        )
        db.session.execute(insert_current_record_to_patient_table)
        db.session.commit()

        flash('Patient record was created successfully')
