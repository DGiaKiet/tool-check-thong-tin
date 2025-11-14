# Hướng Dẫn Push Code Sang Repository Mới

## Tổng Quan

Tài liệu này hướng dẫn cách copy và push code tool (bao gồm tính năng tra cứu Facebook) sang repository mới:
- **Repository mới**: https://github.com/DGiaKiet/check-thong-tin-.git
- **Repository hiện tại**: https://github.com/DGiaKiet/tool-check-thong-tin

## Files Cần Copy

### 1. Files Chính
```
✅ EXAMPLE_TOOL_TEMPLATE.py      - Tool chính với menu 9 options
✅ facebook_phone_lookup.py       - Module tra cứu Facebook
✅ .gitignore                     - Git configuration
```

### 2. Files Documentation (Tùy chọn)
```
□ TOOL_ANALYSIS.md
□ HOW_TO_CREATE_SIMILAR_TOOL.md
□ ARCHITECTURE.md
□ SUMMARY.md
□ README.md
```

## Phương Pháp 1: Clone và Copy (Khuyến nghị)

### Bước 1: Clone Repository Mới

```bash
# Mở terminal/command prompt
cd ~/Desktop  # hoặc thư mục bạn muốn làm việc

# Clone repository mới
git clone https://github.com/DGiaKiet/check-thong-tin-.git
cd check-thong-tin-
```

### Bước 2: Copy Files Từ Repo Cũ

**Option A: Copy thủ công**
```bash
# Giả sử repo cũ ở ~/tool-check-thong-tin
cp ~/tool-check-thong-tin/EXAMPLE_TOOL_TEMPLATE.py .
cp ~/tool-check-thong-tin/facebook_phone_lookup.py .
cp ~/tool-check-thong-tin/.gitignore .
```

**Option B: Download từ GitHub**
1. Vào https://github.com/DGiaKiet/tool-check-thong-tin
2. Chọn branch `copilot/analyze-tool-creation-process`
3. Download từng file:
   - EXAMPLE_TOOL_TEMPLATE.py
   - facebook_phone_lookup.py
   - .gitignore
4. Copy vào folder `check-thong-tin-`

### Bước 3: Đổi Tên File (Tùy chọn)

```bash
# Đổi tên file chính để dễ nhớ hơn
mv EXAMPLE_TOOL_TEMPLATE.py tool_check_info.py

# Hoặc giữ nguyên tên cũng được
```

### Bước 4: Customize Code

**Sửa Config trong tool_check_info.py (hoặc EXAMPLE_TOOL_TEMPLATE.py):**

```python
class Config:
    """Cấu hình cho tool"""
    TOOL_NAME = "Tool Check Thông Tin Facebook"  # ← Đổi tên
    VERSION = "1.0.0"
    AUTHOR = "DGiaKiet"  # ← Đổi tên tác giả
    CONTACT = {
        "email": "your-email@example.com",  # ← Email của bạn
        "github": "https://github.com/DGiaKiet",  # ← GitHub của bạn
        "facebook": "https://facebook.com/yourpage"  # ← Facebook của bạn
    }
```

### Bước 5: Test Tool

```bash
# Test module Facebook lookup
python3 facebook_phone_lookup.py

# Test tool chính
python3 tool_check_info.py
# Chọn option 9 để test tính năng Facebook lookup
```

### Bước 6: Tạo README Mới

Tạo file `README.md` trong repo mới:

```markdown
# Tool Check Thông Tin

Tool kiểm tra và tra cứu thông tin với các tính năng:

## Tính Năng

1. ✅ Kiểm tra số điện thoại (validate format, đầu số)
2. ✅ Kiểm tra email (validate format)
3. ✅ Kiểm tra URL (validate format)
4. ✅ **Tra cứu SĐT qua Facebook** (NEW!)
5. 🔄 Xử lý file dữ liệu (đang phát triển)
6. 📊 Thống kê (đang phát triển)

## Cài Đặt

### Yêu Cầu
- Python 3.6+
- pip

### Dependencies (Tùy chọn)
```bash
# Cài pystyle cho giao diện đẹp (optional)
pip install pystyle

# Cài requests cho API calls (nếu dùng API mode)
pip install requests

# Cài beautifulsoup4 cho scraping (không khuyến khích)
pip install beautifulsoup4
```

### Chạy Tool
```bash
# Cách 1: Chạy file gốc
python3 EXAMPLE_TOOL_TEMPLATE.py

# Cách 2: Nếu đã đổi tên
python3 tool_check_info.py
```

## Sử Dụng Tính Năng Facebook Lookup

### Demo Mode (Khuyến nghị để test)
1. Chạy tool
2. Chọn option [9] - Tra cứu SĐT qua Facebook
3. Nhập Facebook URL (VD: https://facebook.com/username)
4. Chọn method [1] - Demo
5. Xem kết quả mẫu

### API Mode (Cần Facebook API Key)
1. Đăng ký Facebook Graph API
2. Lấy Access Token
3. Sửa code trong `facebook_phone_lookup.py`:
   ```python
   def _lookup_via_api(url, username):
       access_token = 'YOUR_ACCESS_TOKEN_HERE'
       # ... implement API call
   ```
4. Chọn method [2] - API khi dùng tool

### ⚠️ Lưu Ý Quan Trọng
- Chức năng tra cứu Facebook chỉ là DEMO
- Không sử dụng cho mục đích xâm phạm privacy
- Tuân thủ Facebook Terms of Service
- Chỉ tra cứu thông tin công khai và có permission

## Cấu Trúc Files

```
check-thong-tin-/
├── EXAMPLE_TOOL_TEMPLATE.py    # Tool chính
├── facebook_phone_lookup.py    # Module Facebook
├── .gitignore                  # Git config
└── README.md                   # Tài liệu này
```

## Phát Triển Thêm

Để thêm tính năng mới:
1. Xem code mẫu trong `EXAMPLE_TOOL_TEMPLATE.py`
2. Tạo function mới theo pattern có sẵn
3. Thêm option vào menu
4. Test kỹ trước khi deploy

## License

MIT License

## Tác Giả

- **Author**: DGiaKiet
- **GitHub**: https://github.com/DGiaKiet
- **Repository**: https://github.com/DGiaKiet/check-thong-tin-

---

Developed with ❤️ by DGiaKiet
```

### Bước 7: Commit và Push

```bash
# Check status
git status

# Add tất cả files
git add .

# Commit với message rõ ràng
git commit -m "Add tool with Facebook phone lookup feature

- Add EXAMPLE_TOOL_TEMPLATE.py (main tool with 9 features)
- Add facebook_phone_lookup.py (Facebook lookup module)
- Add README.md (documentation)
- Add .gitignore (Git configuration)

Features:
- Phone/Email/URL validation
- Facebook phone lookup (demo/api/scrape modes)
- Statistics and settings (coming soon)
"

# Push lên GitHub
git push origin main

# Nếu lỗi, có thể cần force push lần đầu:
# git push -u origin main
```

## Phương Pháp 2: Direct Clone và Modify

### Bước 1: Clone Repo Hiện Tại

```bash
# Clone repo có code
git clone -b copilot/analyze-tool-creation-process \
  https://github.com/DGiaKiet/tool-check-thong-tin.git \
  temp-tool-repo

cd temp-tool-repo
```

### Bước 2: Thay Đổi Remote

```bash
# Remove remote cũ
git remote remove origin

# Add remote mới
git remote add origin https://github.com/DGiaKiet/check-thong-tin-.git

# Check
git remote -v
```

### Bước 3: Clean Up Files Không Cần

```bash
# Xóa file tool gốc (obfuscated)
rm xcattoolv2.py

# Giữ lại files cần thiết:
# - EXAMPLE_TOOL_TEMPLATE.py
# - facebook_phone_lookup.py
# - .gitignore
# - README.md (sửa lại)

# Xóa các docs không cần (tùy chọn)
# rm TOOL_ANALYSIS.md HOW_TO_CREATE_SIMILAR_TOOL.md ARCHITECTURE.md SUMMARY.md
```

### Bước 4: Commit và Push

```bash
# Reset git history (optional - để có lịch sử sạch)
rm -rf .git
git init
git add .
git commit -m "Initial commit: Tool with Facebook lookup feature"

# Add remote và push
git remote add origin https://github.com/DGiaKiet/check-thong-tin-.git
git branch -M main
git push -u origin main --force  # Dùng --force nếu repo mới đã có commits
```

## Phương Pháp 3: Upload Trực Tiếp Qua GitHub Web

### Bước 1: Vào Repository Mới
1. Truy cập: https://github.com/DGiaKiet/check-thong-tin-
2. Click "Add file" → "Upload files"

### Bước 2: Upload Files
1. Kéo thả hoặc chọn files:
   - EXAMPLE_TOOL_TEMPLATE.py
   - facebook_phone_lookup.py
   - .gitignore
2. Thêm commit message: "Add tool with Facebook lookup feature"
3. Click "Commit changes"

### Bước 3: Tạo README
1. Click "Add file" → "Create new file"
2. Tên file: `README.md`
3. Copy nội dung README từ phần trên
4. Commit

## Troubleshooting

### Lỗi: Permission denied (publickey)
**Giải pháp**: Sử dụng HTTPS thay vì SSH
```bash
git remote set-url origin https://github.com/DGiaKiet/check-thong-tin-.git
```

### Lỗi: Repository not found
**Giải pháp**: Check lại URL và quyền truy cập
```bash
# Xem remote hiện tại
git remote -v

# Sửa lại nếu sai
git remote set-url origin https://github.com/DGiaKiet/check-thong-tin-.git
```

### Lỗi: Updates were rejected
**Giải pháp**: Pull trước khi push
```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

### Module facebook_phone_lookup không import được
**Giải pháp**: Đảm bảo cả 2 files ở cùng thư mục
```bash
ls -la *.py
# Phải thấy cả EXAMPLE_TOOL_TEMPLATE.py và facebook_phone_lookup.py
```

## Next Steps

Sau khi push thành công:

1. **Verify trên GitHub**
   - Vào https://github.com/DGiaKiet/check-thong-tin-
   - Check tất cả files đã có
   - Đọc README hiển thị đúng

2. **Test Local**
   ```bash
   cd ~/Desktop
   git clone https://github.com/DGiaKiet/check-thong-tin-.git
   cd check-thong-tin-
   python3 EXAMPLE_TOOL_TEMPLATE.py
   ```

3. **Phát Triển Thêm**
   - Thêm tính năng mới
   - Improve UI
   - Add tests
   - Deploy as web service

4. **Share**
   - Share repository link
   - Viết blog post
   - Làm video demo

## Resources

- **Git Documentation**: https://git-scm.com/doc
- **GitHub Guides**: https://guides.github.com
- **Python Documentation**: https://docs.python.org
- **Facebook Graph API**: https://developers.facebook.com/docs/graph-api

## Support

Nếu gặp vấn đề:
1. Check lại từng bước trong guide này
2. Đọc error message cẩn thận
3. Search lỗi trên Google/Stack Overflow
4. Tạo issue trên GitHub repository

---

**Good luck with your new repository!** 🚀
