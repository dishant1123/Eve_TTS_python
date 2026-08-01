from http.server import BaseHTTPRequestHandler, HTTPServer
import json
students = [
    {
        "id": 1,
        "name": "Dishant",
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Rahul",
        "course": "Data Science"
    }
]

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/students":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(students).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Page Not Found")
    def do_POST(self):
        if self.path == "/students":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)

            students.append(data)
            self.send_response(201)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "message": "Student Added Successfully",
                "students": students
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()
    def do_PUT(self):
        if self.path.startswith("/students/"):
            student_id = int(self.path.split("/")[-1])
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)
            found = False
            for student in students:
                if student["id"] == student_id:
                    student["name"] = data["name"]
                    student["course"] = data["course"]
                    found = True
                    break
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            if found:
                response = {
                    "message": "Student Updated",
                    "students": students
                }
            else:
                response = {
                    "message": "Student Not Found"
                }
            self.wfile.write(json.dumps(response).encode())
        else:

            self.send_response(404)
            self.end_headers()
    def do_DELETE(self):

        if self.path.startswith("/students/"):
            student_id = int(self.path.split("/")[-1])
            found = False
            for student in students:
                if student["id"] == student_id:
                    students.remove(student)
                    found = True
                    break
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            if found:
                response = {
                    "message": "Student Deleted",
                    "students": students
                }
            else:
                response = {
                    "message": "Student Not Found"
                }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()
# Run Server
server = HTTPServer(("localhost", 8000), MyServer)
print("Server Started")
print("http://localhost:8000/students")

server.serve_forever()



