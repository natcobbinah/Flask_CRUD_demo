from flask import Blueprint, render_template
from sqlalchemy import insert, select
from .database import db
from .models import Billing

# HTML FILES
BILLING_HTML = 'billing.html'

billing_records_bp = Blueprint('billing_records', __name__)

@billing_records_bp.route("/billing")
def billing():
    stmt_billing = select(Billing)
    result = db.session.execute(stmt_billing).scalars().all()

    db_billing_records = [
        {
            "BillID": billing_record.BillID,
            "PatientID": billing_record.PatientID,
            "Amount": billing_record.Amount,
            "PaymentStatus": billing_record.PaymentStatus
        }
        for billing_record in result
    ]


    return render_template(
        BILLING_HTML,
        billing=db_billing_records
    )
