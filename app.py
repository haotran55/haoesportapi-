from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/follow', methods=['GET'])
def follow():
    # Lấy các tham số từ query string
    username = request.args.get('username')
    key = request.args.get('key')
    
    if username and key:
        # Bạn có thể xử lý các tham số tại đây (ví dụ: lưu vào database, thực hiện hành động...)
        return jsonify({"message": f"Follow request for {username} with key {key} processed."}), 200
    else:
        return jsonify({"error": "Missing 'username' or 'key' parameters."}), 400

if __name__ == '__main__':
    app.run(debug=True)
