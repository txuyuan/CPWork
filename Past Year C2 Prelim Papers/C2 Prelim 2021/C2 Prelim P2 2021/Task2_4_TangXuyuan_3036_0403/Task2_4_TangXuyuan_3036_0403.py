from flask import Flask, render_template
import sqlite3

class ServiceRecord():
    def __init__(self, Sender=None, AccessDate=None, Status=None, AppType=None):
        self._Sender = Sender
        self._AccessDate = AccessDate
        self._Status = Status
        self._AppType = AppType

    def get_Sender(self):
        return self._Sender
    def set_Sender(self, Sender):
        self._Sender = Sender
    def get_AccessDate(self):
        return self._AccessDate
    def set_AccessDate(self, AccessDate):
        self._AccessDate = AccessDate
    def get_Status(self):
        return self._Status
    def set_Status(self, Status):
        self._Status = Status
    def get_AppType(self):
        return self._AppType
    def set_AppType(self, AppType):
        self._AppType = AppType

    def isSuccess(self):
        return self._Status == 200
    def getAppType(self):
        return self._AppType

    def getSuccess(self):
        return "SUCCESS" if self.isSuccess() else "FAILED"

    def __str__(self):
        return f"[{self._Sender}, {self._AccessDate}, {self._Status}]"


class AppServiceRecord(ServiceRecord):
    def getAppType(self):
        match self._AppType:
            case "WA":
                return "WHATSAPP"
            case "FB":
                return "FACEBOOK MESSENGER"

class SmsServiceRecord(ServiceRecord):
    def getAppType(self):
        return "SHORT MESSAGE SERVICE"

def get_all_logs():
    # Fetch logs from database
    con = sqlite3.connect("../ServiceLog.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("""
        SELECT * FROM Log
    """)
    results = cur.fetchall()
    log_records = [dict(x) for x in results]

    cur.close()
    con.close()

    # Cast logs to objects
    logs = []
    for log in log_records:
        if log["AppType"] is not None:
            log = AppServiceRecord(log["Sender"], log["AccessDate"], log["Status"], log["AppType"])
        else:
            log = SmsServiceRecord(log["Sender"], log["AccessDate"], log["Status"])
        logs += [[log.get_Sender(), log.get_AccessDate(), log.getAppType(), log.getSuccess()]]

    return logs

app = Flask(__name__)

@app.route("/")
def index():
    logs = get_all_logs()
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run()
