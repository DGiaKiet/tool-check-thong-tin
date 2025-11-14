"""
EXAMPLE TOOL TEMPLATE
=====================
Đây là template mẫu để tạo tool kiểm tra thông tin
Bạn có thể sử dụng code này làm starting point cho tool của mình

Author: Template
Version: 1.0
"""

import os
import sys
import time
from datetime import datetime

# Kiểm tra và import pystyle (nếu có)
try:
    from pystyle import Colors, Colorate, Center, Write
    PYSTYLE_AVAILABLE = True
except ImportError:
    PYSTYLE_AVAILABLE = False
    print("[!] Pystyle không được cài đặt. Chạy: pip install pystyle")
    print("[*] Tool sẽ chạy ở chế độ cơ bản...\n")

# ============================================
# CONFIGURATION
# ============================================

class Config:
    """Cấu hình cho tool"""
    TOOL_NAME = "Tool Kiểm Tra Thông Tin"
    VERSION = "1.0.0"
    AUTHOR = "Your Name"
    CONTACT = {
        "email": "your-email@example.com",
        "github": "https://github.com/yourusername",
        "facebook": "https://facebook.com/yourpage"
    }
    
    # Màu sắc theme (nếu có pystyle)
    COLOR_BANNER = Colors.blue_to_cyan if PYSTYLE_AVAILABLE else None
    COLOR_MENU = Colors.purple_to_blue if PYSTYLE_AVAILABLE else None
    COLOR_SUCCESS = Colors.green_to_yellow if PYSTYLE_AVAILABLE else None
    COLOR_ERROR = Colors.red_to_yellow if PYSTYLE_AVAILABLE else None
    COLOR_INFO = Colors.yellow if PYSTYLE_AVAILABLE else None

# ============================================
# UTILITY FUNCTIONS
# ============================================

def clear_screen():
    """Xóa màn hình console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color=None, center=False, interval=0):
    """In text có màu (nếu có pystyle)"""
    if PYSTYLE_AVAILABLE and color:
        if center:
            text = Center.XCenter(text)
        if interval > 0:
            Write.Print(text, color, interval=interval)
        else:
            print(Colorate.Horizontal(color, text))
    else:
        print(text)

def print_banner():
    """In banner của tool"""
    banner = f"""
    ╔══════════════════════════════════════════════╗
    ║                                              ║
    ║         {Config.TOOL_NAME}         ║
    ║              Version {Config.VERSION}                  ║
    ║           Coded by: {Config.AUTHOR}            ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
    """
    print_colored(banner, Config.COLOR_BANNER, center=True)

def print_menu():
    """In menu chính"""
    menu = """
    ┌───────────────────────────────────────┐
    │           MENU CHÍNH                  │
    ├───────────────────────────────────────┤
    │                                       │
    │  [1] Kiểm tra số điện thoại          │
    │  [2] Kiểm tra email                   │
    │  [3] Kiểm tra URL                     │
    │  [4] Xử lý file dữ liệu              │
    │  [5] Thống kê                         │
    │  [6] Cài đặt                          │
    │  [7] Hướng dẫn                        │
    │  [8] Thông tin tool                   │
    │  [0] Thoát                            │
    │                                       │
    └───────────────────────────────────────┘
    """
    print_colored(menu, Config.COLOR_MENU)

def input_with_prompt(prompt, color=None):
    """Nhận input với prompt có màu"""
    if PYSTYLE_AVAILABLE and color:
        Write.Print(prompt, color, interval=0.02)
        return input()
    else:
        return input(prompt)

def press_enter():
    """Chờ người dùng nhấn Enter"""
    input_with_prompt("\n[*] Nhấn Enter để tiếp tục...", Config.COLOR_INFO)

def show_loading(text="Đang xử lý", duration=2):
    """Hiển thị loading animation"""
    if PYSTYLE_AVAILABLE:
        Write.Print(f"\n{text}", Config.COLOR_INFO, interval=0.02)
    else:
        print(f"\n{text}", end="")
    
    for _ in range(duration):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

# ============================================
# VALIDATION FUNCTIONS
# ============================================

def validate_phone(phone):
    """Kiểm tra số điện thoại hợp lệ"""
    # Loại bỏ khoảng trắng và các ký tự đặc biệt
    clean_phone = ''.join(filter(str.isdigit, phone))
    
    # Kiểm tra độ dài (ví dụ: số VN 10-11 số)
    if len(clean_phone) < 10 or len(clean_phone) > 11:
        return False, "Số điện thoại phải có 10-11 chữ số"
    
    # Kiểm tra đầu số (ví dụ)
    valid_prefixes = ['03', '05', '07', '08', '09']
    if not any(clean_phone.startswith(prefix) for prefix in valid_prefixes):
        return False, "Đầu số không hợp lệ"
    
    return True, clean_phone

def validate_email(email):
    """Kiểm tra email hợp lệ"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True, email
    else:
        return False, "Email không đúng định dạng"

def validate_url(url):
    """Kiểm tra URL hợp lệ"""
    import re
    pattern = r'^https?://[^\s<>"]+|www\.[^\s<>"]+'
    
    if re.match(pattern, url):
        return True, url
    else:
        return False, "URL không đúng định dạng"

# ============================================
# MAIN FEATURES
# ============================================

def feature_check_phone():
    """Chức năng kiểm tra số điện thoại"""
    clear_screen()
    print_banner()
    print_colored("\n[*] KIỂM TRA SỐ ĐIỆN THOẠI", Config.COLOR_SUCCESS)
    
    phone = input_with_prompt("\n[?] Nhập số điện thoại: ", Config.COLOR_INFO)
    
    if not phone.strip():
        print_colored("\n[!] Số điện thoại không được để trống!", Config.COLOR_ERROR)
        press_enter()
        return
    
    show_loading("Đang kiểm tra", 2)
    
    is_valid, result = validate_phone(phone)
    
    if is_valid:
        output = f"""
    ┌───────────────────────────────────────┐
    │        KẾT QUẢ KIỂM TRA              │
    ├───────────────────────────────────────┤
    │  Số điện thoại: {result}
    │  Trạng thái: ✓ HỢP LỆ
    │  Nhà mạng: [Chức năng mở rộng]
    │  Khu vực: [Chức năng mở rộng]
    │  Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    └───────────────────────────────────────┘
        """
        print_colored(output, Config.COLOR_SUCCESS)
    else:
        print_colored(f"\n[!] KHÔNG HỢP LỆ: {result}", Config.COLOR_ERROR)
    
    press_enter()

def feature_check_email():
    """Chức năng kiểm tra email"""
    clear_screen()
    print_banner()
    print_colored("\n[*] KIỂM TRA EMAIL", Config.COLOR_SUCCESS)
    
    email = input_with_prompt("\n[?] Nhập địa chỉ email: ", Config.COLOR_INFO)
    
    if not email.strip():
        print_colored("\n[!] Email không được để trống!", Config.COLOR_ERROR)
        press_enter()
        return
    
    show_loading("Đang kiểm tra", 2)
    
    is_valid, result = validate_email(email)
    
    if is_valid:
        domain = email.split('@')[1]
        output = f"""
    ┌───────────────────────────────────────┐
    │        KẾT QUẢ KIỂM TRA              │
    ├───────────────────────────────────────┤
    │  Email: {result}
    │  Domain: {domain}
    │  Trạng thái: ✓ HỢP LỆ
    │  Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    └───────────────────────────────────────┘
        """
        print_colored(output, Config.COLOR_SUCCESS)
    else:
        print_colored(f"\n[!] KHÔNG HỢP LỆ: {result}", Config.COLOR_ERROR)
    
    press_enter()

def feature_check_url():
    """Chức năng kiểm tra URL"""
    clear_screen()
    print_banner()
    print_colored("\n[*] KIỂM TRA URL", Config.COLOR_SUCCESS)
    
    url = input_with_prompt("\n[?] Nhập URL: ", Config.COLOR_INFO)
    
    if not url.strip():
        print_colored("\n[!] URL không được để trống!", Config.COLOR_ERROR)
        press_enter()
        return
    
    show_loading("Đang kiểm tra", 2)
    
    is_valid, result = validate_url(url)
    
    if is_valid:
        output = f"""
    ┌───────────────────────────────────────┐
    │        KẾT QUẢ KIỂM TRA              │
    ├───────────────────────────────────────┤
    │  URL: {result[:30]}...
    │  Trạng thái: ✓ HỢP LỆ
    │  Protocol: {'HTTPS' if 'https' in result else 'HTTP'}
    │  Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    └───────────────────────────────────────┘
        """
        print_colored(output, Config.COLOR_SUCCESS)
    else:
        print_colored(f"\n[!] KHÔNG HỢP LỆ: {result}", Config.COLOR_ERROR)
    
    press_enter()

def feature_process_file():
    """Chức năng xử lý file"""
    clear_screen()
    print_banner()
    print_colored("\n[*] XỬ LÝ FILE DỮ LIỆU", Config.COLOR_SUCCESS)
    
    print_colored("\n[!] Chức năng đang được phát triển...", Config.COLOR_INFO)
    print("\nCác tính năng sẽ có:")
    print("  - Đọc file TXT/CSV/JSON")
    print("  - Xử lý hàng loạt")
    print("  - Xuất kết quả ra file")
    
    press_enter()

def feature_statistics():
    """Hiển thị thống kê"""
    clear_screen()
    print_banner()
    print_colored("\n[*] THỐNG KÊ", Config.COLOR_SUCCESS)
    
    stats = f"""
    ┌───────────────────────────────────────┐
    │          THỐNG KÊ SỬ DỤNG            │
    ├───────────────────────────────────────┤
    │  Tổng số lần kiểm tra: 0
    │  Kiểm tra hôm nay: 0
    │  Thành công: 0
    │  Thất bại: 0
    │  Lần sử dụng cuối: Chưa có
    └───────────────────────────────────────┘
    
    [*] Ghi chú: Tính năng thống kê cần được
        kết nối với database để lưu trữ dữ liệu
    """
    print(stats)
    
    press_enter()

def feature_settings():
    """Cài đặt"""
    clear_screen()
    print_banner()
    print_colored("\n[*] CÀI ĐẶT", Config.COLOR_SUCCESS)
    
    settings_menu = """
    ┌───────────────────────────────────────┐
    │  [1] Thay đổi theme màu
    │  [2] Cấu hình API
    │  [3] Ngôn ngữ
    │  [4] Reset cài đặt
    │  [0] Quay lại
    └───────────────────────────────────────┘
    """
    print(settings_menu)
    
    choice = input_with_prompt("\n[?] Chọn: ", Config.COLOR_INFO)
    
    if choice in ["1", "2", "3", "4"]:
        print_colored("\n[!] Chức năng đang được phát triển...", Config.COLOR_INFO)
        press_enter()

def feature_help():
    """Hướng dẫn sử dụng"""
    clear_screen()
    print_banner()
    print_colored("\n[*] HƯỚNG DẪN SỬ DỤNG", Config.COLOR_SUCCESS)
    
    help_text = """
    ┌─────────────────────────────────────────────┐
    │           HƯỚNG DẪN CHI TIẾT                │
    ├─────────────────────────────────────────────┤
    │                                             │
    │  1. KIỂM TRA SỐ ĐIỆN THOẠI                 │
    │     - Nhập số điện thoại cần kiểm tra      │
    │     - Tool sẽ validate format và đầu số    │
    │     - Hiển thị kết quả chi tiết            │
    │                                             │
    │  2. KIỂM TRA EMAIL                          │
    │     - Nhập địa chỉ email                   │
    │     - Kiểm tra format chuẩn                │
    │     - Phân tích domain                      │
    │                                             │
    │  3. KIỂM TRA URL                            │
    │     - Nhập URL website                      │
    │     - Validate format và protocol          │
    │                                             │
    │  4-5. CÁC CHỨC NĂNG MỞ RỘNG               │
    │       Đang được phát triển                 │
    │                                             │
    │  LIÊN HỆ HỖ TRỢ:                          │
    │  Email: {Config.CONTACT['email']}
    │  GitHub: {Config.CONTACT['github']}
    │                                             │
    └─────────────────────────────────────────────┘
    """
    print(help_text)
    
    press_enter()

def feature_about():
    """Thông tin về tool"""
    clear_screen()
    print_banner()
    print_colored("\n[*] THÔNG TIN TOOL", Config.COLOR_SUCCESS)
    
    about_text = f"""
    ┌─────────────────────────────────────────────┐
    │              THÔNG TIN                      │
    ├─────────────────────────────────────────────┤
    │                                             │
    │  Tool: {Config.TOOL_NAME}
    │  Version: {Config.VERSION}
    │  Author: {Config.AUTHOR}
    │                                             │
    │  Ngôn ngữ: Python {sys.version.split()[0]}
    │  Pystyle: {'✓ Đã cài đặt' if PYSTYLE_AVAILABLE else '✗ Chưa cài đặt'}
    │                                             │
    │  LIÊN HỆ:                                  │
    │  • Email: {Config.CONTACT['email']}
    │  • GitHub: {Config.CONTACT['github'][:35]}...
    │  • Facebook: {Config.CONTACT['facebook'][:35]}...
    │                                             │
    │  © 2024 All rights reserved                │
    │                                             │
    └─────────────────────────────────────────────┘
    """
    print(about_text)
    
    press_enter()

# ============================================
# MAIN FUNCTION
# ============================================

def main():
    """Hàm chính - điều khiển luồng chương trình"""
    
    # Hiển thị welcome message
    clear_screen()
    print_banner()
    print_colored("\n[*] Chào mừng đến với tool!", Config.COLOR_SUCCESS, interval=0.02)
    time.sleep(1)
    
    # Main loop
    while True:
        try:
            clear_screen()
            print_banner()
            print_menu()
            
            # Nhận lựa chọn từ người dùng
            choice = input_with_prompt("\n[?] Chọn chức năng (0-8): ", Config.COLOR_INFO)
            
            # Xử lý lựa chọn
            if choice == "1":
                feature_check_phone()
            elif choice == "2":
                feature_check_email()
            elif choice == "3":
                feature_check_url()
            elif choice == "4":
                feature_process_file()
            elif choice == "5":
                feature_statistics()
            elif choice == "6":
                feature_settings()
            elif choice == "7":
                feature_help()
            elif choice == "8":
                feature_about()
            elif choice == "0":
                clear_screen()
                print_banner()
                print_colored("\n[*] Cảm ơn bạn đã sử dụng tool!", Config.COLOR_SUCCESS, interval=0.02)
                print_colored("[*] Tạm biệt! 👋\n", Config.COLOR_SUCCESS, interval=0.02)
                break
            else:
                print_colored("\n[!] Lựa chọn không hợp lệ! Vui lòng chọn 0-8.", Config.COLOR_ERROR)
                press_enter()
                
        except KeyboardInterrupt:
            print_colored("\n\n[!] Đã dừng chương trình (Ctrl+C)\n", Config.COLOR_ERROR)
            break
        except Exception as e:
            print_colored(f"\n[!] Lỗi: {str(e)}\n", Config.COLOR_ERROR)
            press_enter()

# ============================================
# ENTRY POINT
# ============================================

if __name__ == "__main__":
    try:
        # Kiểm tra Python version
        if sys.version_info < (3, 6):
            print("[!] Tool yêu cầu Python 3.6 trở lên!")
            print(f"[!] Bạn đang dùng Python {sys.version}")
            sys.exit(1)
        
        # Chạy chương trình chính
        main()
        
    except Exception as e:
        print(f"\n[!] Lỗi nghiêm trọng: {e}")
        input("\nNhấn Enter để thoát...")
        sys.exit(1)
