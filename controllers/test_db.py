def getAllModules():
    return [{'id':'SEN301','name' : 'Software Engineering', 'code' : 'SFEN301', 'type':'module', "sessions": []}, 
            {'id':'PRJB301','name' : 'Project B', 'code' : 'PRJB301', 'type':'module', "sessions": []}, 
            {'id':'MCHI301','name' : 'Machine Intelligence', 'code' : 'MCHI301', 'type':'module', "sessions": []}, 
            {'id':'PJMN301','name' : 'Project Management', 'code' : 'PJMN301', 'type':'module', "sessions": []},
            {'id':'PBDV301','name' : 'Platform Based Programming', 'code' : 'PBDV301', 'type':'module', "sessions": []}]

def getAllAttendance():
    return [{"code":"MCHI301","module":"Machine Intelligence III", "date":"30/09/2023","time":" 02:37 PM","status":"Present","student_id":"22175060"},
    {"code":"PJMN301","module":"Project Management III", "date":"30/09/2023","time":" 01:04 PM","status":"Absent","student_id" : "22104775"},
    {"code":"MCHI301","module":"Machine Intelligence III", "date":"30/09/2023","time":" 01:08 PM","status":"Present","student_id": "21710473"},
    {"code":"SFEN301","module":"Software Engineering III", "date":"30/09/2023","time":" 01:00 PM","status":"Present","student_id": "22010661"}]

def getStudentAttendance(student_id):
    return [item for item in getAllAttendance() if item["student_id"]==student_id]

def getAllQR():
    return [{"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
            {"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
            {"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
            {"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
            {"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
            {"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
            {"module":"Software Engineering III","session":"30/09/2023 09:30 AM","expiration":"30/09/2023 12:00 PM","expired":0,"qr_url":"path/to/blob/storage"},
            {"module":"Project B III","session":"28/09/2023 14:00 AM","expiration":"28/09/2023 12:00 PM","expired":1,"qr_url":"path/to/blob/storage"},
            {"module":"Project B III","session":"28/09/2023 14:00 AM","expiration":"28/09/2023 12:00 PM","expired":1,"qr_url":"path/to/blob/storage"},
            {"module":"Project B III","session":"28/09/2023 14:00 AM","expiration":"28/09/2023 12:00 PM","expired":1,"qr_url":"path/to/blob/storage"}]
            
def getAllQualifications():
    return [{'id':'BINCT1', 'name' : 'BACHELOR OF INF & COM TECHNOLOGY', 'code' : 'BINCT1', 'type':'qualification'},
            {'id':'DIIAD1','name':'DIPLOMA IN ICT APPLICATIONS DEVELOPMENT','code' : 'DIIAD1', 'type':'qualification'}]

def getUserTimetable():
    return [{"module":"BSIT301","time":"08:00 AM","status":"Absent"},{"module":"SFEN301","time":"10:00 AM","status":"Present"},{"module":"PRJB301","time":"12:00 PM","status":"Upcoming"}]

