from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dictionary of students with names as keys and marks as values
students = {
    student['name']: student['marks']
    for student in [
        {"name": "0", "marks": 45}, {"name": "i1", "marks": 34}, {"name": "XpnuGx", "marks": 54},
        {"name": "yr58", "marks": 72}, {"name": "jVeR1q", "marks": 93}, {"name": "FDWMOGH", "marks": 2},
        {"name": "sPYJR", "marks": 90}, {"name": "N", "marks": 60}, {"name": "g", "marks": 81},
        {"name": "IsvFkhW1wW", "marks": 54}, {"name": "Sn6", "marks": 92}, {"name": "rI", "marks": 33},
        {"name": "i", "marks": 47}, {"name": "89fPECdQr", "marks": 64}, {"name": "fvZ4iMFG", "marks": 77},
        {"name": "GNdj4ytZ", "marks": 13}, {"name": "vv6fLc0QW", "marks": 33}, {"name": "4IT50Vm8", "marks": 52},
        {"name": "66VfQO", "marks": 52}, {"name": "hzQ", "marks": 63}, {"name": "f0mqqC", "marks": 82},
        {"name": "mwUQuTm", "marks": 31}, {"name": "ploi8pQL0B", "marks": 81}, {"name": "jd8X6EpJn", "marks": 1},
        {"name": "GVOp", "marks": 57}, {"name": "DY5f4sm", "marks": 24}, {"name": "capF0S7n", "marks": 8},
        {"name": "XaRYyfy", "marks": 41}, {"name": "BUBcH", "marks": 54}, {"name": "ePiR9", "marks": 59},
        {"name": "I2zkg", "marks": 11}, {"name": "p14HZ8", "marks": 92}, {"name": "fxm6cp2", "marks": 44},
        {"name": "gkSupzH", "marks": 72}, {"name": "WzGqr1z", "marks": 40}, {"name": "k", "marks": 89},
        {"name": "1upz", "marks": 68}, {"name": "AZ286", "marks": 9}, {"name": "j1HAP", "marks": 89},
        {"name": "9lC9", "marks": 90}, {"name": "e0SRdCPeEj", "marks": 62}, {"name": "yvOY8", "marks": 25},
        {"name": "eIKDKP31s", "marks": 83}, {"name": "cml0Evv", "marks": 70}, {"name": "FIyEB", "marks": 57},
        {"name": "yRiRgFsb", "marks": 28}, {"name": "sW8nQJrm", "marks": 87}, {"name": "mNj8iD", "marks": 87},
        {"name": "tookvVp", "marks": 47}, {"name": "aAZ", "marks": 43}, {"name": "7fisUQ2", "marks": 43},
        {"name": "bHG", "marks": 22}, {"name": "Ws4", "marks": 23}, {"name": "ZeHGRru3Vi", "marks": 42},
        {"name": "rqOIo7a", "marks": 71}, {"name": "4bWd", "marks": 33}, {"name": "LF", "marks": 74},
        {"name": "7VsPlBwz", "marks": 28}, {"name": "jnfLWfE8D9", "marks": 20}, {"name": "03h", "marks": 50},
        {"name": "0xjsrxHOH", "marks": 69}, {"name": "WHy4uC", "marks": 29}, {"name": "sD", "marks": 92},
        {"name": "m89hD2kQXy", "marks": 88}, {"name": "z631Q1KSB", "marks": 15}, {"name": "77V", "marks": 81},
        {"name": "SJ", "marks": 15}, {"name": "vuxcKpOUR", "marks": 13}, {"name": "YLns", "marks": 27},
        {"name": "W", "marks": 9}, {"name": "WE", "marks": 47}, {"name": "hcLD", "marks": 87},
        {"name": "3ukT2HS", "marks": 4}, {"name": "MnbXHAyAQp", "marks": 4}, {"name": "rZc", "marks": 87},
        {"name": "Eh9", "marks": 8}, {"name": "tBaNSRsx", "marks": 46}, {"name": "uL7prt", "marks": 94},
        {"name": "zq", "marks": 13}, {"name": "PFv0bWi", "marks": 89}, {"name": "nZv0gsVR", "marks": 19},
        {"name": "VQyDp", "marks": 19}, {"name": "MyAV", "marks": 76}, {"name": "8xo0GJB", "marks": 65},
        {"name": "KxITK5X1z", "marks": 78}, {"name": "Raonhc", "marks": 97}, {"name": "8sbDfy0", "marks": 6},
        {"name": "r2", "marks": 95}, {"name": "6J2H4k1E", "marks": 81}, {"name": "Y2aTV0ur", "marks": 30},
        {"name": "H", "marks": 61}, {"name": "jr", "marks": 73}, {"name": "4", "marks": 33},
        {"name": "dyo", "marks": 58}, {"name": "vI", "marks": 93}, {"name": "c2juJZu6R", "marks": 80},
        {"name": "wnP", "marks": 89}, {"name": "y", "marks": 83}, {"name": "RXDIqxxiwh", "marks": 81},
        {"name": "M6ZF", "marks": 15}
    ]
}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get names from query parameters
    marks = {name: students.get(name, "not found") for name in names}  # Return "not found" if missing
    return jsonify(marks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Make it accessible on network
