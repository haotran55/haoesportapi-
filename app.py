import os
from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

# Lấy thông tin xác thực từ biến môi trường (sử dụng biến môi trường đúng tên)
account_sid = os.getenv('TWILIO_ACCOUNT_SID')  # Cập nhật tên biến môi trường đúng
auth_token = os.getenv('TWILIO_AUTH_TOKEN')  # Cập nhật tên biến môi trường đúng

# Kiểm tra nếu không có thông tin xác thực trong biến môi trường
if not account_sid or not auth_token:
    raise ValueError("No Twilio credentials provided! Please set 'TWILIO_ACCOUNT_SID' and 'TWILIO_AUTH_TOKEN'.")

client = Client(account_sid, auth_token)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    # Lấy thông tin từ request
    data = request.get_json()

    # Kiểm tra nếu không có thông tin cần thiết
    if 'phone_number' not in data or 'message' not in data:
        return jsonify({'error': 'Missing phone_number or message'}), 400

    phone_number = data['phone_number']
    message_text = data['message']

    try:
        # Gửi SMS
        message = client.messages.create(
            body=message_text,
            from_='+84343626390',  # Số điện thoại Twilio của bạn
            to=phone_number  # Số điện thoại nhận
        )
        return jsonify({'message_sid': message.sid, 'status': 'success'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
