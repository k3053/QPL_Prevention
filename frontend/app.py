from flask import Flask, render_template, request
from web3 import Web3
import json

# Initalize Flask app
app = Flask(__name__)

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# check connection
if not web3.is_connected():
    print("Could not connect to Ganache")
else:
    print("Connected to Ganache")

# Load contract ABI and address
contract_address = "0xf84ddf6a7d3f6E6919E5FB812Cc9b221cC479b5d" # Contract Address

with open(r"C:\Users\kulde\OneDrive\Desktop\Blockchain_OEP\QPL_Prevention\Backend\build\contracts\GetSet.json", "r") as file:
    contract_json = json.load(file)
    contract_abi = contract_json["abi"]
    contract_address = contract_json['networks']['5777']['address']

# print(f"Contract Address: {contract_address}")
# print(f"Contract ABI: {contract_abi}")

# stored_message = contract.functions.Get().call()
# print(f"Stored Message: {stored_message}")


# Create contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

account = web3.eth.accounts[0]

@app.route("/", methods=["GET", "POST"])

def home():
    stored_message = None
    value = None

    if request.method == "POST":
        if "set_button" in request.form:
            # GEt user input from the form
            value = request.form.get("user_input")

            # set the message in the smart comtract (send a transaction)
            tx_hash = contract.functions.Set(value).transact({'from': account})
            web3.eth.wait_for_transaction_receipt(tx_hash)

        if "get_button" in request.form:
            # Get the message from the smart contract (call a function)
            stored_message = contract.functions.Get().call()

    # Pass the value to the template
    return render_template("index.html", value=stored_message)

if __name__ == "__main__":
    app.run(debug=True)
