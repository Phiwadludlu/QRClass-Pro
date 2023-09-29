from flask import render_template

def viewAttendance():
    return render_template('layouts/lecturer/LecturerAttendance.html')

def activeQR():
    qr_data = [{"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
{"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
{"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
{"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
{"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
{"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
{"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
{"module":"Project B III","session":"28/09/2023 14:00 AM","expiration":"28/09/2023 12:00 PM","expired":1,"qr_url":"path/to/blob/storage"},
{"module":"Project B III","session":"28/09/2023 14:00 AM","expiration":"28/09/2023 12:00 PM","expired":1,"qr_url":"path/to/blob/storage"},
{"module":"Project B III","session":"28/09/2023 14:00 AM","expiration":"28/09/2023 12:00 PM","expired":1,"qr_url":"path/to/blob/storage"}]
    return render_template('layouts/lecturer/ActiveQR_layout.html', qr_data=qr_data)