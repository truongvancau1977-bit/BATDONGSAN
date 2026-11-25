# Trợ Lý QLDA BĐS - Mobile Web Agent

Ứng dụng Web Mobile (PWA) điều hành và tra cứu hồ sơ pháp lý các dự án bất động sản, sử dụng model **Gemini 3.5 Flash-Lite** (`gemini-3.5-flash-lite`) qua Google AI Studio API.

## Tính năng
- Tối ưu giao diện Mobile (iOS/Android), hỗ trợ **Thêm vào Màn hình chính (PWA)**.
- Kết nối trực tiếp Google AI Studio API (`gemini-3.5-flash-lite`) bằng API Key cá nhân (lưu an toàn tại `localStorage` trên thiết bị).
- Nạp sẵn dữ liệu thực tế từ hồ sơ dự án (`knowledge.js`), hỗ trợ chuyển đổi nhanh giữa các dự án.
- Thanh lệnh nhanh & nhập liệu bằng giọng nói (`vi-VN`).

## Triển khai
- **GitHub Pages**: Bật *Settings -> Pages -> Deploy from a branch (`main` / `root`)*.
- **Netlify / Vercel**: Kết nối trực tiếp repository này để tự động deploy mỗi khi `git push`.
- **Cập nhật dữ liệu mới**: Chạy `python3 sync_data.py` ở máy tính để đóng gói lại `knowledge.js`, sau đó `git add . && git commit -m "Update data" && git push`.
