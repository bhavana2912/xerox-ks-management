from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from firebase_config import db
import os

app = Flask(__name__)

# ==========================================
# UPLOAD FOLDER
# ==========================================

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==========================================
# CUSTOMER ROUTES
# ==========================================

@app.route("/")
def home():
    return render_template("customer/home.html")


@app.route("/services")
def services():
    return render_template("customer/services.html")


@app.route("/pricing")
def pricing():
    return render_template("customer/pricing.html")


@app.route("/service-request")
def service_request():
    return render_template("customer/service_request.html")


@app.route("/xerox-order")
def xerox_order():
    return render_template("customer/xerox_order.html")


@app.route("/mobile-repair")
def mobile_repair():
    return render_template("customer/mobile_repair.html")


@app.route("/online-service")
def online_service():
    return render_template("customer/online_service.html")


@app.route("/contact")
def contact():
    return render_template("customer/contact.html")


@app.route("/success")
def success():
    return render_template("customer/success.html")

    # ==========================================
# SUBMIT XEROX ORDER
# ==========================================

@app.route("/submit-xerox-order", methods=["POST"])
def submit_xerox_order():

    customer_name = request.form.get("customer_name")
    mobile = request.form.get("mobile")
    paper_size = request.form.get("paper_size")
    print_type = request.form.get("print_type")
    print_side = request.form.get("print_side")
    copies = request.form.get("copies")
    instructions = request.form.get("instructions")

    document = request.files.get("document")

    filename = ""

    if document and document.filename != "":
        filename = secure_filename(document.filename)
        document.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    db.collection("xerox_orders").add({
        "customer_name": customer_name,
        "mobile": mobile,
        "paper_size": paper_size,
        "print_type": print_type,
        "print_side": print_side,
        "copies": copies,
        "instructions": instructions,
        "document": filename,
        "status": "Pending"
    })

    return redirect(url_for("success"))


# ==========================================
# SUBMIT MOBILE REPAIR
# ==========================================

@app.route("/submit-mobile-repair", methods=["POST"])
def submit_mobile_repair():

    customer_name = request.form.get("customer_name")
    mobile = request.form.get("mobile")
    brand = request.form.get("brand")
    model = request.form.get("model")
    repair_type = request.form.get("repair_type")
    problem = request.form.get("problem")
    visit_date = request.form.get("visit_date")

    photo = request.files.get("photo")

    filename = ""

    if photo and photo.filename != "":
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    db.collection("mobile_orders").add({
        "customer_name": customer_name,
        "mobile": mobile,
        "brand": brand,
        "model": model,
        "repair_type": repair_type,
        "problem": problem,
        "visit_date": visit_date,
        "photo": filename,
        "status": "Pending"
    })

    return redirect(url_for("success"))


# ==========================================
# SUBMIT ONLINE SERVICE
# ==========================================

@app.route("/submit-online-service", methods=["POST"])
def submit_online_service():

    customer_name = request.form.get("customer_name")
    mobile = request.form.get("mobile")
    service = request.form.get("service")
    notes = request.form.get("notes")

    document = request.files.get("document")

    filename = ""

    if document and document.filename != "":
        filename = secure_filename(document.filename)
        document.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    db.collection("online_orders").add({
        "customer_name": customer_name,
        "mobile": mobile,
        "service": service,
        "notes": notes,
        "document": filename,
        "status": "Pending"
    })

    return redirect(url_for("success"))

    # ==========================================
# SUBMIT XEROX ORDER
# ==========================================

@app.route("/submit-xerox-order", methods=["POST"])
def submit_xerox_order():

    customer_name = request.form.get("customer_name")
    mobile = request.form.get("mobile")
    paper_size = request.form.get("paper_size")
    print_type = request.form.get("print_type")
    print_side = request.form.get("print_side")
    copies = request.form.get("copies")
    instructions = request.form.get("instructions")

    document = request.files.get("document")

    filename = ""

    if document and document.filename != "":
        filename = secure_filename(document.filename)
        document.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    db.collection("xerox_orders").add({
        "customer_name": customer_name,
        "mobile": mobile,
        "paper_size": paper_size,
        "print_type": print_type,
        "print_side": print_side,
        "copies": copies,
        "instructions": instructions,
        "document": filename,
        "status": "Pending"
    })

    return redirect(url_for("success"))


# ==========================================
# SUBMIT MOBILE REPAIR
# ==========================================

@app.route("/submit-mobile-repair", methods=["POST"])
def submit_mobile_repair():

    customer_name = request.form.get("customer_name")
    mobile = request.form.get("mobile")
    brand = request.form.get("brand")
    model = request.form.get("model")
    repair_type = request.form.get("repair_type")
    problem = request.form.get("problem")
    visit_date = request.form.get("visit_date")

    photo = request.files.get("photo")

    filename = ""

    if photo and photo.filename != "":
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    db.collection("mobile_orders").add({
        "customer_name": customer_name,
        "mobile": mobile,
        "brand": brand,
        "model": model,
        "repair_type": repair_type,
        "problem": problem,
        "visit_date": visit_date,
        "photo": filename,
        "status": "Pending"
    })

    return redirect(url_for("success"))


# ==========================================
# SUBMIT ONLINE SERVICE
# ==========================================

@app.route("/submit-online-service", methods=["POST"])
def submit_online_service():

    customer_name = request.form.get("customer_name")
    mobile = request.form.get("mobile")
    service = request.form.get("service")
    notes = request.form.get("notes")

    document = request.files.get("document")

    filename = ""

    if document and document.filename != "":
        filename = secure_filename(document.filename)
        document.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    db.collection("online_orders").add({
        "customer_name": customer_name,
        "mobile": mobile,
        "service": service,
        "notes": notes,
        "document": filename,
        "status": "Pending"
    })

    return redirect(url_for("success"))

    # ==========================================
# ADMIN XEROX ORDERS
# ==========================================

@app.route("/admin/xerox-orders")
def xerox_orders():

    docs = db.collection("xerox_orders").stream()

    orders = []

    for doc in docs:
        order = doc.to_dict()
        order["id"] = doc.id
        orders.append(order)

    return render_template(
        "admin/xerox_orders.html",
        orders=orders
    )


# ==========================================
# ADMIN MOBILE ORDERS
# ==========================================

@app.route("/admin/mobile-orders")
def mobile_orders():

    docs = db.collection("mobile_orders").stream()

    orders = []

    for doc in docs:
        order = doc.to_dict()
        order["id"] = doc.id
        orders.append(order)

    return render_template(
        "admin/mobile_orders.html",
        orders=orders
    )


# ==========================================
# ADMIN ONLINE ORDERS
# ==========================================

@app.route("/admin/online-orders")
def admin_online_orders():

    docs = db.collection("online_orders").stream()

    orders = []

    for doc in docs:
        order = doc.to_dict()
        order["id"] = doc.id
        orders.append(order)

    return render_template(
        "admin/online_orders.html",
        orders=orders
    )


# ==========================================
# VIEW XEROX ORDER
# ==========================================

@app.route("/admin/xerox-order/<order_id>")
def view_xerox_order(order_id):

    doc = db.collection("xerox_orders").document(order_id).get()

    if not doc.exists:
        return "Order Not Found"

    order = doc.to_dict()
    order["id"] = doc.id

    return render_template(
        "admin/view_xerox_order.html",
        order=order
    )


# ==========================================
# UPDATE STATUS
# ==========================================

@app.route("/update-status/<order_id>/<status>")
def update_status(order_id, status):

    db.collection("xerox_orders").document(order_id).update({
        "status": status
    })

    return redirect(url_for("xerox_orders"))


# ==========================================
# LOGOUT
# ==========================================

@app.route("/logout")
def logout():
    return redirect(url_for("admin"))


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)