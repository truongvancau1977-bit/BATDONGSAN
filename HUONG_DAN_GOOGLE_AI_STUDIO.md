# HƯỚNG DẪN SỬ DỤNG AGENT QLDA BĐS TRÊN ĐIỆN THOẠI (QUA GOOGLE AI STUDIO)

Hệ thống đã được đóng gói sẵn trong thư mục `APP_MOBILE_AGENT/`, tích hợp dữ liệu thực tế mới nhất của cả **03 dự án** (mặc định là **Dự án BĐS Thần Lĩnh - Nghệ An**).

---

## CÁCH 1: DÙNG WEB APP MOBILE RIÊNG (KHUYÊN DÙNG — GIAO DIỆN ĐẸP, CÓ NÚT LỆNH NHANH & GIỌNG NÓI)

### Bước 1: Lấy API Key miễn phí từ Google AI Studio
1. Truy cập: https://aistudio.google.com/apikey (đăng nhập bằng tài khoản Google).
2. Nhấn **Create API key** và sao chép mã khóa (bắt đầu bằng `AIzaSy...`).

### Bước 2: Đưa Web App lên mạng để mở trên điện thoại mọi lúc mọi nơi
* **Cách nhanh nhất (30 giây, miễn phí, không cần cài đặt)**:
  1. Truy cập https://app.netlify.com/drop trên máy tính.
  2. Kéo và thả nguyên thư mục `APP_MOBILE_AGENT` vào khung trên trang web.
  3. Netlify sẽ cấp ngay một đường link dạng `https://ten-ngau-nhien.netlify.app`.
* **Hoặc dùng tại văn phòng qua WiFi nội bộ**:
  - Chạy lệnh trong Terminal: `./APP_MOBILE_AGENT/start_server.sh` và mở link IP hiện trên màn hình.

### Bước 3: Cài thành App trên điện thoại (iPhone / Android)
1. Mở đường link ở Bước 2 bằng **Safari** (iPhone) hoặc **Chrome** (Android).
2. Bấm biểu tượng **Chia sẻ (Share)** trên iPhone -> Chọn **"Thêm vào MH chính" (Add to Home Screen)** (trên Android bấm dấu 3 chấm -> **Cài đặt ứng dụng**).
3. Mở App từ màn hình chính -> Bấm biểu tượng bánh răng **⚙️** ở góc trên bên phải -> Dán **Google AI Studio API Key** -> Nhấn **Lưu cấu hình**.
4. Từ giờ anh/chị có thể ra lệnh bằng văn bản hoặc bấm nút **🎙️** nói trực tiếp trên điện thoại!

---

## CÁCH 2: ĐỒNG BỘ KHI CÓ DỮ LIỆU MỚI TRONG `DATA/`
Mỗi khi anh/chị thêm tài liệu mới vào thư mục `DATA/` và tôi đã cập nhật vào file `.md`:
1. Chạy `python3 APP_MOBILE_AGENT/sync_data.py` để tự động đóng gói dữ liệu mới vào `knowledge.js` (hoặc yêu cầu tôi chạy giúp).
2. Nếu đang host trên Netlify, chỉ cần kéo thả lại thư mục `APP_MOBILE_AGENT` hoặc bấm nút **⚙️ -> Nạp file .md cập nhật nóng** ngay trên điện thoại.

---

## CÁCH 3: DÙNG TRỰC TIẾP TRONG GOOGLE AI STUDIO (`aistudio.google.com`)
Nếu anh/chị muốn mở trực tiếp trang web của Google AI Studio trên điện thoại mà không cần host Web App riêng:
1. Vào https://aistudio.google.com trên trình duyệt -> Chọn **Create new prompt** (hoặc tab **Build** để tạo app trực tiếp trong AI Studio).
2. Ở ô **System Instructions**, dán đoạn chỉ dẫn sau:
   > *Bạn là Trợ lý Pháp lý & Điều hành Dự án BĐS Thần Lĩnh (Nghệ An). Chỉ sử dụng dữ liệu từ tài liệu đính kèm, tuyệt đối không bịa số liệu, luôn trích dẫn số hiệu văn bản gốc.*
3. Nhấn nút **(+) Add to prompt** -> Upload file `HO_SO_DU_LIEU_DU_AN_THAN_LINH.md`.
4. Nhấn **Save** (Lưu vào Google Drive). Sau đó trên điện thoại chỉ cần mở `aistudio.google.com` -> chọn đúng Prompt đã lưu để chat và ra lệnh.
