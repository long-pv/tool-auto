# Hướng Dẫn Cài Đặt và Đóng Gói Ứng Dụng Python

## Cài Đặt Python và Thư Viện

1. **Tải và Cài Đặt Python:**
   - Tải **Python 3.10.11** từ [đây](https://www.python.org/downloads/release/python-31011/).
   - Chọn phiên bản **Windows installer (64-bit)**.

2. **Kiểm Tra Phiên Bản Python:**
   - Mở Command Prompt và chạy lệnh sau để kiểm tra phiên bản Python đã cài đặt:

     ```bash
     python --version
     ```

3. **Kiểm Tra Phiên Bản pip:**
   - Để kiểm tra xem **pip** đã được cài đặt hay chưa, chạy:

     ```bash
     python -m pip --version
     ```

4. **Cài Đặt Thư Viện Cần Thiết:**
   - Cài đặt các thư viện cần thiết cho dự án bằng cách chạy lệnh sau:

     ```bash
     python -m pip install pyautogui opencv-python pillow numpy keyboard
     ```

5. **Cài Đặt PyInstaller:**
   - Cài đặt **PyInstaller** để đóng gói ứng dụng:

     ```bash
     python -m pip install pyinstaller
     ```

   - Cập nhật **PyInstaller** lên phiên bản mới nhất:

     ```bash
     python -m pip install --upgrade pyinstaller
     ```

## Đóng Gói Ứng Dụng Python

1. **Đóng Gói Ứng Dụng Python:**
   - Sử dụng lệnh sau để đóng gói ứng dụng Python thành file `.exe`:

     ```bash
     python -m PyInstaller --onefile --windowed main.py
     ```

2. **Ném Thư Mục Ảnh vào Thư Mục `dist`:**
   - Sau khi đóng gói, PyInstaller sẽ tạo ra thư mục **`dist/`** chứa file `.exe` của bạn.
   - Đảm bảo rằng bạn **ném thư mục ảnh** (`images/`) vào trong thư mục **`dist/`**.

### Cấu Trúc Thư Mục `dist`:

