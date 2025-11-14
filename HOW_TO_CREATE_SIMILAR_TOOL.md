# Hướng Dẫn Tạo Tool Tương Tự

## Giới Thiệu
Tài liệu này hướng dẫn chi tiết từng bước để tạo một tool kiểm tra thông tin tương tự như tool trong dự án này.

## Yêu Cầu Trước Khi Bắt Đầu

### 1. Kiến Thức Cần Có
- Python cơ bản (biến, hàm, vòng lặp, điều kiện)
- Làm việc với terminal/command line
- Git cơ bản (optional - để quản lý code)

### 2. Công Cụ Cần Cài Đặt
```bash
# Python 3.7 trở lên
python --version

# pip (Python package manager)
pip --version

# Git (optional)
git --version
```

## Bước 1: Setup Môi Trường

### 1.1 Tạo Thư Mục Dự Án
```bash
# Tạo folder cho project
mkdir my-tool
cd my-tool

# Tạo virtual environment (khuyến nghị)
python -m venv venv

# Kích hoạt virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 1.2 Cài Đặt Dependencies
```bash
# Cài đặt pystyle cho giao diện đẹp
pip install pystyle

# Các thư viện hữu ích khác
pip install requests      # Để gọi API
pip install colorama      # Màu sắc cho terminal
pip install python-dotenv # Quản lý environment variables
```

### 1.3 Tạo File requirements.txt
```bash
pip freeze > requirements.txt
```

## Bước 2: Tạo File Tool Cơ Bản

### 2.1 Tạo File main.py
```python
"""
Tool Check Thông Tin - Version 1.0
Author: Your Name
Description: Tool để kiểm tra và xử lý thông tin
"""

import os
import sys
from pystyle import Colors, Colorate, Center, Write, System

# ============================================
# CONFIGURATION
# ============================================
TOOL_NAME = "Tool Check Thông Tin"
VERSION = "1.0"
AUTHOR = "Your Name"

# ============================================
# UTILITY FUNCTIONS
# ============================================

def clear_screen():
    """Xóa màn hình console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """In banner của tool"""
    banner = f"""
    ╔══════════════════════════════════════╗
    ║                                      ║
    ║     {TOOL_NAME}           ║
    ║          Version {VERSION}                 ║
    ║       Coded by: {AUTHOR}          ║
    ║                                      ║
    ╔══════════════════════════════════════╗
    """
    print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(banner)))

def print_menu():
    """In menu chính"""
    menu = """
    ┌─────────────────────────────────┐
    │         MENU CHÍNH              │
    ├─────────────────────────────────┤
    │  [1] Kiểm tra thông tin         │
    │  [2] Xử lý dữ liệu              │
    │  [3] Cài đặt                    │
    │  [4] Hướng dẫn sử dụng          │
    │  [0] Thoát                      │
    └─────────────────────────────────┘
    """
    print(Colorate.Horizontal(Colors.purple_to_blue, menu))

def press_enter_to_continue():
    """Chờ người dùng nhấn Enter"""
    input("\n[*] Nhấn Enter để tiếp tục...")

# ============================================
# MAIN FEATURES
# ============================================

def feature_check_info():
    """Chức năng kiểm tra thông tin"""
    clear_screen()
    print_banner()
    print(Colorate.Horizontal(Colors.green_to_yellow, "\n[*] CHỨC NĂNG KIỂM TRA THÔNG TIN"))
    
    # Nhập thông tin từ người dùng
    Write.Print("\n[?] Nhập thông tin cần kiểm tra: ", Colors.blue_to_cyan, interval=0.02)
    user_input = input()
    
    if not user_input.strip():
        Write.Print("\n[!] Lỗi: Thông tin không được để trống!\n", Colors.red_to_yellow, interval=0.02)
        press_enter_to_continue()
        return
    
    # Xử lý thông tin (ví dụ đơn giản)
    Write.Print("\n[*] Đang xử lý...\n", Colors.yellow, interval=0.02)
    
    # Giả lập xử lý
    import time
    time.sleep(1)
    
    # Hiển thị kết quả
    result = f"""
    ┌─────────────────────────────────┐
    │      KẾT QUẢ KIỂM TRA           │
    ├─────────────────────────────────┤
    │  Input: {user_input[:20]}{'...' if len(user_input) > 20 else ''}
    │  Độ dài: {len(user_input)} ký tự
    │  Loại: {'Số' if user_input.isdigit() else 'Chữ'}
    │  Trạng thái: ✓ Hợp lệ
    └─────────────────────────────────┘
    """
    print(Colorate.Horizontal(Colors.green_to_white, result))
    
    press_enter_to_continue()

def feature_process_data():
    """Chức năng xử lý dữ liệu"""
    clear_screen()
    print_banner()
    print(Colorate.Horizontal(Colors.green_to_yellow, "\n[*] CHỨC NĂNG XỬ LÝ DỮ LIỆU"))
    
    Write.Print("\n[!] Chức năng đang được phát triển...\n", Colors.yellow, interval=0.02)
    press_enter_to_continue()

def feature_settings():
    """Chức năng cài đặt"""
    clear_screen()
    print_banner()
    print(Colorate.Horizontal(Colors.green_to_yellow, "\n[*] CÀI ĐẶT"))
    
    settings_menu = """
    1. Thay đổi theme
    2. Cấu hình API
    3. Quay lại menu chính
    """
    print(settings_menu)
    
    choice = input("[?] Chọn: ")
    if choice == "1":
        Write.Print("\n[!] Chức năng đang được phát triển...\n", Colors.yellow, interval=0.02)
    elif choice == "2":
        Write.Print("\n[!] Chức năng đang được phát triển...\n", Colors.yellow, interval=0.02)
    
    press_enter_to_continue()

def feature_help():
    """Hiển thị hướng dẫn sử dụng"""
    clear_screen()
    print_banner()
    print(Colorate.Horizontal(Colors.green_to_yellow, "\n[*] HƯỚNG DẪN SỬ DỤNG"))
    
    help_text = """
    ┌─────────────────────────────────────────────────┐
    │           HƯỚNG DẪN SỬ DỤNG TOOL                │
    ├─────────────────────────────────────────────────┤
    │                                                 │
    │  [1] Kiểm tra thông tin:                        │
    │      - Nhập thông tin cần kiểm tra             │
    │      - Tool sẽ phân tích và trả về kết quả     │
    │                                                 │
    │  [2] Xử lý dữ liệu:                             │
    │      - Xử lý dữ liệu theo nhiều định dạng      │
    │      - Xuất kết quả ra file                    │
    │                                                 │
    │  [3] Cài đặt:                                   │
    │      - Tùy chỉnh theme và cấu hình tool        │
    │                                                 │
    │  Liên hệ hỗ trợ: your-email@example.com        │
    │                                                 │
    └─────────────────────────────────────────────────┘
    """
    print(help_text)
    
    press_enter_to_continue()

# ============================================
# MAIN FUNCTION
# ============================================

def main():
    """Hàm chính điều khiển luồng chương trình"""
    
    while True:
        try:
            clear_screen()
            print_banner()
            print_menu()
            
            # Nhận lựa chọn từ người dùng
            Write.Print("\n[?] Chọn chức năng: ", Colors.blue_to_cyan, interval=0.02)
            choice = input()
            
            # Xử lý lựa chọn
            if choice == "1":
                feature_check_info()
            elif choice == "2":
                feature_process_data()
            elif choice == "3":
                feature_settings()
            elif choice == "4":
                feature_help()
            elif choice == "0":
                Write.Print("\n[*] Cảm ơn bạn đã sử dụng tool! Tạm biệt!\n", Colors.green_to_yellow, interval=0.02)
                break
            else:
                Write.Print("\n[!] Lựa chọn không hợp lệ! Vui lòng chọn lại.\n", Colors.red_to_yellow, interval=0.02)
                press_enter_to_continue()
                
        except KeyboardInterrupt:
            Write.Print("\n\n[!] Đã dừng chương trình!\n", Colors.red, interval=0.02)
            break
        except Exception as e:
            Write.Print(f"\n[!] Lỗi: {str(e)}\n", Colors.red, interval=0.02)
            press_enter_to_continue()

# ============================================
# ENTRY POINT
# ============================================

if __name__ == "__main__":
    try:
        # Kiểm tra Python version
        if sys.version_info < (3, 7):
            print("[!] Tool yêu cầu Python 3.7 trở lên!")
            sys.exit(1)
        
        # Chạy chương trình chính
        main()
        
    except Exception as e:
        print(f"[!] Lỗi nghiêm trọng: {e}")
        sys.exit(1)
```

## Bước 3: Test Tool

### 3.1 Chạy Tool
```bash
python main.py
```

### 3.2 Test Từng Chức Năng
- Test menu navigation
- Test input validation
- Test error handling
- Test tất cả các tính năng

## Bước 4: Thêm Tính Năng Nâng Cao

### 4.1 Tích Hợp API
```python
import requests

def check_info_via_api(phone_number):
    """Kiểm tra thông tin qua API"""
    try:
        url = "https://api.example.com/check"
        payload = {"phone": phone_number}
        headers = {"Authorization": "Bearer YOUR_API_KEY"}
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "API request failed"}
            
    except Exception as e:
        return {"error": str(e)}
```

### 4.2 Lưu/Đọc File
```python
import json

def save_to_file(data, filename="output.json"):
    """Lưu dữ liệu ra file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")
        return False

def read_from_file(filename="input.json"):
    """Đọc dữ liệu từ file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return None
```

### 4.3 Thêm Configuration File
```python
# config.py
class Config:
    # API Configuration
    API_KEY = "your_api_key_here"
    API_URL = "https://api.example.com"
    
    # Tool Configuration
    THEME = "blue_to_cyan"
    LANGUAGE = "vi"
    
    # Logging
    ENABLE_LOG = True
    LOG_FILE = "tool.log"
```

## Bước 5: Obfuscate Code (Tùy Chọn)

### 5.1 Sử Dụng PyArmor
```bash
# Cài đặt PyArmor
pip install pyarmor

# Obfuscate code
pyarmor obfuscate --recursive main.py

# Code đã obfuscate sẽ ở trong folder dist/
```

### 5.2 Sử Dụng PyInstaller để tạo EXE
```bash
# Cài đặt PyInstaller
pip install pyinstaller

# Tạo file executable
pyinstaller --onefile --name="MyTool" main.py

# File .exe sẽ ở trong folder dist/
```

### 5.3 Custom Obfuscation Script
```python
# obfuscate.py
import base64
import zlib

def obfuscate_file(input_file, output_file):
    """Obfuscate Python file"""
    
    # Đọc code gốc
    with open(input_file, 'r', encoding='utf-8') as f:
        original_code = f.read()
    
    # Nén và encode
    compressed = zlib.compress(original_code.encode('utf-8'))
    encoded = base64.b64encode(compressed).decode('utf-8')
    
    # Tạo wrapper code
    wrapper = f'''
import base64
import zlib

_obf = "{encoded}"

try:
    exec(zlib.decompress(base64.b64decode(_obf)))
except Exception as e:
    print(f"Error: {{e}}")
'''
    
    # Lưu file đã obfuscate
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(wrapper)
    
    print(f"[+] Đã obfuscate: {input_file} -> {output_file}")

if __name__ == "__main__":
    obfuscate_file("main.py", "main_obfuscated.py")
```

Chạy script:
```bash
python obfuscate.py
```

## Bước 6: Tạo Documentation

### 6.1 Tạo README.md
```markdown
# Tool Check Thông Tin

## Mô tả
Tool để kiểm tra và xử lý thông tin một cách tự động.

## Tính năng
- ✅ Kiểm tra thông tin
- ✅ Xử lý dữ liệu
- ✅ Giao diện console đẹp
- ✅ Dễ sử dụng

## Cài đặt

### Yêu cầu
- Python 3.7+
- pip

### Các bước cài đặt
```bash
# Clone repo
git clone https://github.com/yourusername/your-tool.git
cd your-tool

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy tool
python main.py
```

## Sử dụng
1. Chạy tool: `python main.py`
2. Chọn chức năng từ menu
3. Làm theo hướng dẫn

## Screenshots
[Thêm ảnh chụp màn hình ở đây]

## Liên hệ
- Email: your-email@example.com
- Facebook: [link]
- GitHub: [link]

## License
MIT License
```

## Bước 7: Upload lên GitHub

### 7.1 Tạo Repository
```bash
# Khởi tạo git
git init

# Tạo .gitignore
echo "venv/
__pycache__/
*.pyc
.env
dist/
build/" > .gitignore

# Add và commit
git add .
git commit -m "Initial commit"

# Push lên GitHub
git remote add origin https://github.com/yourusername/your-tool.git
git branch -M main
git push -u origin main
```

## Bước 8: Maintain và Update

### 8.1 Version Control
```python
# Trong code, quản lý version
VERSION = "1.0.0"  # Major.Minor.Patch

# 1.0.0 -> 1.0.1: Bug fixes
# 1.0.0 -> 1.1.0: New features (backward compatible)
# 1.0.0 -> 2.0.0: Breaking changes
```

### 8.2 Changelog
```markdown
# CHANGELOG.md

## [1.0.0] - 2024-01-01
### Added
- Initial release
- Basic features

## [1.1.0] - 2024-02-01
### Added
- New feature X
### Fixed
- Bug Y
```

## Tips và Best Practices

### 1. Code Quality
- Viết code rõ ràng, dễ đọc
- Comment cho các phần phức tạp
- Sử dụng meaningful variable names
- Follow PEP 8 style guide

### 2. Error Handling
- Luôn xử lý exceptions
- Validate user input
- Hiển thị error messages rõ ràng

### 3. Security
- Không hardcode sensitive data
- Sử dụng environment variables
- Validate và sanitize input

### 4. User Experience
- Giao diện trực quan
- Loading indicators
- Clear instructions
- Helpful error messages

### 5. Performance
- Optimize code cho tốc độ
- Cache kết quả khi cần
- Async operations cho I/O

## Kết Luận

Bạn đã có đầy đủ kiến thức để tạo một tool tương tự! 

**Các bước tóm tắt:**
1. Setup môi trường
2. Viết code cơ bản
3. Test và debug
4. Thêm tính năng
5. Obfuscate (optional)
6. Tạo documentation
7. Upload lên GitHub
8. Maintain và update

**Resources hữu ích:**
- [Python Documentation](https://docs.python.org)
- [Pystyle Documentation](https://github.com/billythegoat356/pystyle)
- [PyArmor Documentation](https://pyarmor.readthedocs.io)
- [PyInstaller Documentation](https://pyinstaller.org)

Chúc bạn thành công! 🚀
