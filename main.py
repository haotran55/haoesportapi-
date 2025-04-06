from flask import Flask, request, jsonify
import random
import os

app = Flask(__name__)

# Dữ liệu giả lập người dùng trong bộ nhớ
users = {
    "10251125": {
        "username": "Quang FF",
        "likes": 100
    },
    "10000001": {
        "username": "Trung Thủ Lĩnh",
        "likes": 78
    }
}

# API key tĩnh
VALID_API_KEY = "haoesport"

@app.route('/freefire/like.php', methods=['GET'])
def like():
    api_key = request.args.get("key")
    uid = request.args.get("uid")

    # Kiểm tra API key
    if api_key != VALID_API_KEY:
        return jsonify({"status": "error", "message": "API key không hợp lệ"}), 401

    # Kiểm tra UID trong bộ nhớ
    user = users.get(uid)
    
    if user is None:
        return jsonify({"status": "error", "message": "UID không tồn tại"}), 404

    likes_before = user["likes"]
    likes_given = random.randint(10, 50)  # Số lượt like buff giả lập
    likes_after = likes_before + likes_given

    # Cập nhật lại số like trong bộ nhớ
    user["likes"] = likes_after

    return jsonify({
        "status": "success",
        "username": user["username"],
        "uid": uid,
        "likes_before": likes_before,
        "likes_after": likes_after,
        "likes_given": likes_given
    })

# Lấy cổng từ biến môi trường PORT mà Render cung cấp, mặc định là 5000 nếu không có
port = int(os.getenv("PORT", 5000))

# Lắng nghe trên tất cả các địa chỉ IP và cổng được Render chỉ định
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=port)
