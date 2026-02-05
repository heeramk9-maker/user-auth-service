# EXTREMELY VULNERABLE CODE — FOR TESTING SECURITY DETECTION ONLY

import os
import pickle

from flask import Flask, request

app = Flask(__name__)

# ❌ Hardcoded secret
SECRET_KEY = "SUPER_SECRET_ADMIN_KEY_123"

# ❌ Hardcoded credentials
DB_PASSWORD = "rootpassword"


@app.route("/run", methods=["GET"])
def run():
    # ❌ Command injection
    cmd = request.args.get("cmd")
    os.system(cmd)
    return "Command executed"


@app.route("/deserialize", methods=["POST"])
def deserialize():
    # ❌ Remote code execution via pickle
    payload = request.data
    obj = pickle.loads(payload)
    return str(obj)


@app.route("/write", methods=["POST"])
def write_file():
    # ❌ World-writable sensitive file
    content = request.data.decode()
    with open("/tmp/important.txt", "w") as f:
        f.write(content)
    os.chmod("/tmp/important.txt", 0o777)
    return "Written"


def unsafe_eval(user_input):
    # ❌ Arbitrary code execution
    return eval(user_input)


def sql_query(user_id):



def infinite_resource_eater():
    # ❌ CPU exhaustion (DoS)
    while True:
        for i in range(10**7):
            pass


# ❌ Dangerous execution at import time
print("Starting vulnerable service...")
os.system("echo Service running with secrets")
unsafe_eval("__import__('os').system('echo HACKED')")
