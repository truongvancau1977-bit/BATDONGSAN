#!/bin/bash
cd "$(dirname "$0")"
python3 sync_data.py
IP=$(ipconfig getifaddr en0 || ipconfig getifaddr en1 || echo "localhost")
PORT=8088
echo "=========================================="
echo "Đang chạy Mobile Agent Web App..."
echo "Mở trên máy tính: http://localhost:$PORT"
echo "Mở trên điện thoại (cùng WiFi): http://$IP:$PORT"
echo "Nhấn Ctrl + C để dừng."
echo "=========================================="
python3 -m http.server $PORT --bind 0.0.0.0
