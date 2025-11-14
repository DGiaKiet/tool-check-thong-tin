# Quick Start: Tính Năng Tra Cứu Facebook

## 🚀 Nhanh Chóng Bắt Đầu

### Files Cần Thiết (Đã Tạo)

```
✅ EXAMPLE_TOOL_TEMPLATE.py       # Tool chính (cập nhật với option 9)
✅ facebook_phone_lookup.py        # Module tra cứu Facebook
✅ GUIDE_PUSH_TO_NEW_REPO.md      # Hướng dẫn chi tiết
```

### 1️⃣ Copy Files Sang Repo Mới

```bash
# Cách nhanh nhất
cd ~/Desktop
git clone https://github.com/DGiaKiet/check-thong-tin-.git
cd check-thong-tin-

# Download 2 files từ repo hiện tại:
# - EXAMPLE_TOOL_TEMPLATE.py
# - facebook_phone_lookup.py
# Copy vào folder check-thong-tin-
```

### 2️⃣ Test Ngay

```bash
# Test module Facebook
python3 facebook_phone_lookup.py

# Test tool đầy đủ
python3 EXAMPLE_TOOL_TEMPLATE.py
# → Chọn [9] Tra cứu SĐT qua Facebook
```

### 3️⃣ Push Lên GitHub

```bash
git add .
git commit -m "Add tool with Facebook lookup feature"
git push origin main
```

## 📋 Tính Năng Mới: Option 9

### Menu Đã Cập Nhật

```
┌───────────────────────────────────────┐
│           MENU CHÍNH                  │
├───────────────────────────────────────┤
│  [1] Kiểm tra số điện thoại          │
│  [2] Kiểm tra email                   │
│  [3] Kiểm tra URL                     │
│  [4] Xử lý file dữ liệu              │
│  [5] Thống kê                         │
│  [6] Cài đặt                          │
│  [7] Hướng dẫn                        │
│  [8] Thông tin tool                   │
│  [9] Tra cứu SĐT qua Facebook ⭐     │  ← MỚI!
│  [0] Thoát                            │
└───────────────────────────────────────┘
```

### Cách Sử Dụng

1. **Chạy tool**: `python3 EXAMPLE_TOOL_TEMPLATE.py`
2. **Chọn option**: `9`
3. **Nhập URL**: `https://facebook.com/username`
4. **Chọn method**:
   - `[1]` Demo - Dữ liệu mẫu (khuyến nghị)
   - `[2]` API - Cần Facebook API key
   - `[3]` Scraping - Không khuyến khích
5. **Xem kết quả**

### Demo Output

```
┌─────────────────────────────────────────────┐
│           KẾT QUẢ TRA CỨU                   │
├─────────────────────────────────────────────┤
│  URL: https://facebook.com/testuser
│  Username: testuser
│  Method: DEMO
│                                             │
│  SỐ ĐIỆN THOẠI TÌM THẤY:                   │
│  [1] 0912 345 678 (Viettel)
│                                             │
│  Thời gian: 2024-11-14 17:40:00
└─────────────────────────────────────────────┘

⚠️ Đây là dữ liệu DEMO, không phải kết quả thực tế
```

## 🔧 Module facebook_phone_lookup.py

### Functions Chính

```python
# Validate Facebook URL
validate_facebook_url(url)
# → Returns: (is_valid, username, error)

# Tra cứu chính
lookup_phone_from_facebook(url, method='demo')
# → Returns: dict với keys: success, phones, note, etc.

# Format số điện thoại
format_phone_vn(phone)
# → Returns: "0912 345 678"

# Lấy thông tin nhà mạng
get_carrier_info(phone)
# → Returns: "Viettel", "Vinaphone", etc.
```

### Example Usage

```python
from facebook_phone_lookup import lookup_phone_from_facebook

# Tra cứu demo
result = lookup_phone_from_facebook(
    "https://facebook.com/username",
    method='demo'
)

if result['success']:
    phones = result.get('phones', [])
    print(f"Found {len(phones)} phones")
    for phone in phones:
        print(f"  - {phone}")
```

## ⚙️ Customize

### Thay Đổi Config

Sửa trong `EXAMPLE_TOOL_TEMPLATE.py`:

```python
class Config:
    TOOL_NAME = "Tool Check Thông Tin Facebook"  # ← Đổi tên
    VERSION = "1.0.0"
    AUTHOR = "DGiaKiet"  # ← Tên bạn
    CONTACT = {
        "email": "your@email.com",
        "github": "https://github.com/DGiaKiet",
        "facebook": "https://facebook.com/yourpage"
    }
```

### Implement API Method

Sửa trong `facebook_phone_lookup.py`:

```python
def _lookup_via_api(url, username):
    import requests
    
    access_token = 'YOUR_FACEBOOK_ACCESS_TOKEN'
    graph_url = f'https://graph.facebook.com/v12.0/{username}'
    
    params = {
        'fields': 'name,email',
        'access_token': access_token
    }
    
    response = requests.get(graph_url, params=params)
    data = response.json()
    
    # Extract phone if available
    # ...
    
    return {
        'success': True,
        'phones': [...],
        # ...
    }
```

## ⚠️ Lưu Ý Quan Trọng

### Bảo Mật & Privacy

```
❌ KHÔNG được:
   - Sử dụng để spam
   - Xâm phạm privacy người khác
   - Vi phạm Facebook ToS
   - Scrape without permission

✅ CHỈ được:
   - Demo với dữ liệu mẫu
   - Tra cứu thông tin công khai
   - Sử dụng với permission
   - Tuân thủ luật pháp
```

### Giới Hạn

- **Demo mode**: Chỉ trả về dữ liệu mẫu
- **API mode**: Cần Facebook API key và permissions
- **Scrape mode**: Vi phạm ToS, không khuyến khích

## 📚 Tài Liệu Đầy Đủ

Xem file `GUIDE_PUSH_TO_NEW_REPO.md` để biết:
- Hướng dẫn chi tiết push sang repo mới
- Troubleshooting
- Advanced configuration
- Deployment options

## 🐛 Troubleshooting Nhanh

### Module không import được
```bash
# Check files ở cùng folder
ls -la *.py

# Phải có cả 2 files:
# - EXAMPLE_TOOL_TEMPLATE.py
# - facebook_phone_lookup.py
```

### Tool không chạy
```bash
# Check Python version
python3 --version  # Cần >= 3.6

# Check syntax
python3 -m py_compile EXAMPLE_TOOL_TEMPLATE.py
```

### Lỗi khi push
```bash
# Sử dụng HTTPS
git remote set-url origin https://github.com/DGiaKiet/check-thong-tin-.git

# Force push nếu cần
git push -u origin main --force
```

## 🎯 Checklist Hoàn Thành

Sau khi làm xong, check:

- [ ] Copy 2 files chính sang repo mới
- [ ] Test tool chạy được
- [ ] Test option 9 Facebook lookup
- [ ] Customize config (tên, author, contact)
- [ ] Tạo README.md cho repo mới
- [ ] Commit và push lên GitHub
- [ ] Verify trên GitHub web
- [ ] Clone lại và test

## 🚀 Next Steps

1. **Improve UI**: Thêm màu sắc với pystyle
2. **Add Features**: Thêm tính năng mới
3. **Implement API**: Kết nối Facebook Graph API thật
4. **Add Tests**: Viết unit tests
5. **Deploy**: Deploy as web service

---

**Happy Coding!** 🎉

*Nếu cần giúp đỡ, xem file GUIDE_PUSH_TO_NEW_REPO.md*
