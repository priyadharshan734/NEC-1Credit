@app.route('/')
def home():
    """Welcome message for the API"""
    return jsonify({"message": "Welcome to the ML Model and Personal API!"})

@app.route('/name', methods=['GET'])
def get_name():
    return jsonify({"name": "priyadharshan734"})  # Replace with your actual name

@app.route('/register_number', methods=['GET'])
def get_register_number():
    return jsonify({"register_number": "22ITl03"})  # Replace with your register number

@app.route('/department', methods=['GET'])
def get_department():
    return jsonify({"department": "Information Technology"})  # Replace with your department

