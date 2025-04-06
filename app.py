import os
from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

# Lấy thông tin xác thực từ biến môi trường
account_sid = os.getenv('AC9e1c95e1273edea03865c721259695e3')
auth_token = os.getenv('f7a9bc69023d2ada26f3cfb1a5a59688')
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
