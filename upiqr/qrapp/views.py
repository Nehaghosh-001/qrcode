from django.shortcuts import render
import qrcode
import base64
from io import BytesIO
import re


def home(request):
    qr = None
    error_message = ""
    contact = ""
    account_holder_name = ""

    if request.method == "POST":
        contact = (request.POST.get("contact", "") or "").strip()
        pattern = r'^[a-zA-Z0-9._-]{2,}@[a-zA-Z]{2,}$'

        if not re.fullmatch(pattern, contact):
            error_message = "Please enter a valid UPI ID."
        else:
            raw_name = contact.split('@')[0]
            account_holder_name = raw_name.replace('.', ' ').replace('_', ' ').replace('-', ' ').title()
            url = f"upi://pay?pa={contact}&pn={account_holder_name}&cu=INR"
            img = qrcode.make(url)
            img = img.convert("RGB") if hasattr(img, "convert") else img

            buffer = BytesIO()
            img.save(buffer, format="JPEG")
            qr = base64.b64encode(buffer.getvalue()).decode()

    return render(request, "index.html", {
        "qr": qr,
        "error_message": error_message,
        "contact": contact,
        "account_holder_name": account_holder_name,
    })