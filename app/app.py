from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    # Define IST timezone
    ist = pytz.timezone('Asia/Kolkata')
    
    # Get current time in IST
    ist_time = datetime.now(ist)
    
    return f"Hello from Kubernetes! Current IST Time: {ist_time.strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
