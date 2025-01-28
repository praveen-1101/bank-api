from flask import Flask, jsonify

app = Flask(__name__)

# Data related to main banks
banks = [
    {"id": 1, "name": "STATE BANK OF INDIA"},
    {"id": 2, "name": "PUNJAB NATIONAL BANK"},
    {"id": 3, "name": "CANARA BANK"}
]

# Data related to its corresponding branches
branches = [
   
    {"branch_code": "ABHY0065001", "bank_id": 1, "branch": "RTGS-HO", "ifsc": "SBIN0001", "address": "ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024", "city": "MUMBAI", "district": "GREATER MUMBAI", "state": "MAHARASHTRA"},
    {"branch_code": "ABHY0065002", "bank_id": 1, "branch": "ABHYUDAYA NAGAR", "ifsc": "SBIN0002", "address": "ABHYUDAYA EDUCATION SOCIETY, OPP. BLDG. NO. 18, ABHYUDAYA NAGAR, KALACHOWKY, MUMBAI - 400033", "city": "MUMBAI", "district": "GREATER MUMBAI", "state": "MAHARASHTRA"},
    {"branch_code": "PNB001", "bank_id": 2, "branch": "BANGALORE BRANCH", "ifsc": "PNB0001", "address": "M.G. ROAD, BANGALORE, KARNATAKA - 560001", "city": "BANGALORE", "district": "BENGALURU", "state": "KARNATAKA"},
    {"branch_code": "PNB002", "bank_id": 2, "branch": "HYDERABAD BRANCH", "ifsc": "PNB0002", "address": "NEAR CHARMINAR, HYDERABAD, TELANGANA - 500065", "city": "HYDERABAD", "district": "HYDERABAD", "state": "TELANGANA"},
    {"branch_code": "CAN001", "bank_id": 3, "branch": "CHENNAI BRANCH", "ifsc": "CAN0001", "address": "R.A. PURAM, CHENNAI, TAMIL NADU - 600028", "city": "CHENNAI", "district": "CHENNAI", "state": "TAMIL NADU"},
    {"branch_code": "CAN002", "bank_id": 3, "branch": "KOCHI BRANCH", "ifsc": "CAN0002", "address": "MG ROAD, KOCHI, KERALA - 682035", "city": "KOCHI", "district": "ERNAKULAM", "state": "KERALA"}
]

#An endpoint to the starting route
@app.route('/')
def home():
    return "Hello, everyone!, Welcome to the Bank API"

# An endpoint to get all the banks
@app.route('/banks', methods=['GET'])
def get_banks():
    return jsonify({"banks": banks})

# An endpoint to get branches of all the banks
@app.route('/banks/<int:bank_id>/branches', methods=['GET'])
def get_branches_for_bank(bank_id):
    bank_branches = [branch for branch in branches if branch["bank_id"] == bank_id]
    return jsonify({"branches": bank_branches})

# An endpoint for non existing banks or branch ids
@app.errorhandler(404)
def page_not_found(error):
    response = {
        "error": "Not Found",
        "message": "The requested URL is not present at the moment. Please check the endpoint and try once again."
    }
    return jsonify(response), 404

#Main function
if __name__ == '__main__':
    app.run(debug=True)
