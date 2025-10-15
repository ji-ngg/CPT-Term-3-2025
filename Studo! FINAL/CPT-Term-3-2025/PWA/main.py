import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from database_manager import init_db, find_user_by_email, create_user, update_user_settings, record_timer, get_conn


init_db()

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = os.environ.get("FLASK_SECRET", "devsecretkey")

RECAPTCHA_SECRET = os.environ.get("RECAPTCHA_SECRET", "6Le4p-grAAAAALZLq0MZ9PmTGQlolEx0qMkmqCfl")
RECAPTCHA_SITE_KEY = os.environ.get("RECAPTCHA_SITE_KEY", "6Le4p-grAAAAAPzBNMRuLIzfy3dcQXYNsVPN5GWX")


def verify_recaptcha(token):
    if not RECAPTCHA_SECRET:
        return True
    try:
        resp = requests.post("https://www.google.com/recaptcha/api/siteverify",
                             data={"secret": RECAPTCHA_SECRET, "response": token})
        data = resp.json()
        return data.get("success", False)
    except Exception:
        return False


@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("clock"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET","POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email","").strip().lower()
        password = request.form.get("password","")
        token = request.form.get("g-recaptcha-response","")
        if not verify_recaptcha(token):
            error = "recaptcha failed"
            return render_template("index.html", error=error, site_key=RECAPTCHA_SITE_KEY)
        user = find_user_by_email(email)
        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            session["first_name"] = user["first_name"]
            return redirect(url_for("clock"))
        else:
            error = "invalid credentials"
    return render_template("index.html", error=error, site_key=RECAPTCHA_SITE_KEY)

@app.route("/signup", methods=["GET","POST"])
def signup():
    error = None
    if request.method == "POST":
        fname = request.form.get("first_name","").strip()
        email = request.form.get("email","").strip().lower()
        password = request.form.get("password","")
        token = request.form.get("g-recaptcha-response","")
        if not verify_recaptcha(token):
            error = "recaptcha failed"
            return render_template("signup.html", error=error, site_key=RECAPTCHA_SITE_KEY)
        if not fname or not email or not password:
            error = "fill all fields"
            return render_template("signup.html", error=error, site_key=RECAPTCHA_SITE_KEY)
        from werkzeug.security import generate_password_hash
        pw_hash = generate_password_hash(password)
        try:
            user_id = create_user(fname, email, pw_hash)
            session["user_id"] = user_id
            session["first_name"] = fname
            return redirect(url_for("clock"))
        except Exception as e:
            error = "email already used"
    return render_template("signup.html", error=error, site_key=RECAPTCHA_SITE_KEY)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/clock")
def clock():
    if "user_id" not in session:
        return redirect(url_for("login"))
    uid = session["user_id"]

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT chosen_bg FROM users WHERE id = ?", (uid,))
    row = cur.fetchone()
    conn.close()
    chosen_bg = row["chosen_bg"] if row else "#edf2f4"
    return render_template("clock.html", first_name=session.get("first_name","friend"), chosen_bg=chosen_bg)

@app.route("/pomodoro")
def pomodoro():
    if "user_id" not in session:
        return redirect(url_for("login"))
    uid = session["user_id"]
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT chosen_alarm, chosen_bgm, chosen_bg FROM users WHERE id = ?", (uid,))
    row = cur.fetchone()
    conn.close()
    chosen_alarm = row["chosen_alarm"] if row else "alarm_duck.mp3"
    chosen_bgm = row["chosen_bgm"] if row else "bg_cafe.mp3"
    chosen_bg = row["chosen_bg"] if row else "#edf2f4"
    return render_template("pomodoro.html", first_name=session.get("first_name","friend"), chosen_alarm=chosen_alarm, chosen_bgm=chosen_bgm, chosen_bg=chosen_bg)

@app.route("/timer")
def timer():
    if "user_id" not in session:
        return redirect(url_for("login"))
    uid = session["user_id"]
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT chosen_alarm, chosen_bgm, chosen_bg FROM users WHERE id = ?", (uid,))
    row = cur.fetchone()
    conn.close()
    chosen_alarm = row["chosen_alarm"] if row else "alarm_duck.mp3"
    chosen_bgm = row["chosen_bgm"] if row else "bg_cafe.mp3"
    chosen_bg = row["chosen_bg"] if row else "#edf2f4"
    return render_template("timer.html", chosen_alarm=chosen_alarm, chosen_bgm=chosen_bgm, chosen_bg=chosen_bg)

@app.route("/options")
def options():
    backgrounds = [
        {"id":"#edf2f4","label":"light off white"},
        {"id":"#c0cfd8","label":"soft grey blue"},
        {"id":"#f8f0ff","label":"lavender"},
        {"id":"#fff1e6","label":"peach"}
    ]
    alarms = [
        {"id":"alarm_duck.mp3","label":"duck quack"},
        {"id":"alarm_siren.mp3","label":"siren"}
    ]
    bgm = [
        {"id":"bg_cafe.mp3","label":"cafe murmur"},
        {"id":"bg_rain.mp3","label":"rainforest"},
    ]
    return jsonify({"backgrounds":backgrounds,"alarms":alarms,"bgm":bgm})

@app.route("/save_settings", methods=["POST"])
def save_settings():
    if "user_id" not in session:
        return jsonify({"ok": False, "error":"not logged in"}), 401
    data = request.json or {}
    bg = data.get("chosen_bg")
    alarm = data.get("chosen_alarm")
    bgm = data.get("chosen_bgm")
    update_user_settings(session["user_id"], chosen_bg=bg, chosen_alarm=alarm, chosen_bgm=bgm)
    return jsonify({"ok": True})

@app.route("/record_timer", methods=["POST"])
def api_record_timer():
    if "user_id" not in session:
        return jsonify({"ok": False}), 401
    data = request.json or {}
    mode = data.get("mode","timer")
    duration = int(data.get("duration",0))
    record_timer(session["user_id"], mode, duration)
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True)
