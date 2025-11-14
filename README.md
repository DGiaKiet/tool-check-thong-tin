# Tool Check Thông Tin

## Giới Thiệu
Tool kiểm tra thông tin được viết bằng Python với mã nguồn được bảo vệ (obfuscated code).

## Tài Liệu Phân Tích

Để hiểu rõ cách tool này được tạo ra và cách tạo tool tương tự, vui lòng xem các tài liệu sau:

### 📚 Tài Liệu Chi Tiết

1. **[TOOL_ANALYSIS.md](./TOOL_ANALYSIS.md)** - Phân tích chi tiết về cách tạo tool
   - Cấu trúc dự án
   - Kỹ thuật được sử dụng (Obfuscation, Pystyle)
   - Quy trình tạo tool từng bước
   - Best practices

2. **[HOW_TO_CREATE_SIMILAR_TOOL.md](./HOW_TO_CREATE_SIMILAR_TOOL.md)** - Hướng dẫn tạo tool tương tự
   - Setup môi trường
   - Code mẫu chi tiết
   - Cách thêm tính năng
   - Cách obfuscate code
   - Cách đóng gói và phân phối

3. **[EXAMPLE_TOOL_TEMPLATE.py](./EXAMPLE_TOOL_TEMPLATE.py)** - Template code hoàn chỉnh
   - Code mẫu có thể chạy được ngay
   - Tích hợp Pystyle
   - Các chức năng validation
   - Error handling
   - Menu system

## Cài Đặt

### Yêu Cầu
- Python 3.7 trở lên
- pip (Python package manager)

### Cài Đặt Dependencies
```bash
pip install pystyle
```

### Chạy Tool Gốc
```bash
python xcattoolv2.py
```

### Chạy Tool Template Mẫu
```bash
python EXAMPLE_TOOL_TEMPLATE.py
```

## Tính Năng Của Tool Gốc

Tool gốc (xcattoolv2.py) có các đặc điểm:
- ✅ Code được obfuscate để bảo vệ
- ✅ Giao diện console đẹp với Pystyle
- ✅ Chức năng kiểm tra thông tin
- ✅ Single-file executable

## Học Cách Tạo Tool Tương Tự

Nếu bạn muốn tạo tool tương tự, hãy làm theo thứ tự:

1. Đọc **TOOL_ANALYSIS.md** để hiểu kiến trúc và kỹ thuật
2. Làm theo **HOW_TO_CREATE_SIMILAR_TOOL.md** để tạo tool của bạn
3. Sử dụng **EXAMPLE_TOOL_TEMPLATE.py** làm starting point
4. Tùy chỉnh và thêm các chức năng của riêng bạn

## Cấu Trúc Dự Án

```
tool-check-thong-tin/
├── README.md                      # Tài liệu này
├── xcattoolv2.py                 # Tool gốc (obfuscated)
├── TOOL_ANALYSIS.md              # Phân tích kỹ thuật
├── HOW_TO_CREATE_SIMILAR_TOOL.md # Hướng dẫn từng bước
└── EXAMPLE_TOOL_TEMPLATE.py      # Template code mẫu
```

## Thông Tin Tác Giả Tool Gốc

- **Tool**: pymeoV2.1
- **Author**: ngocuyencoder
- **Facebook**: https://www.facebook.com/datishnu1907
- **Telegram**: https://t.me/huynhngocuyenn

## License

No Cyber Security

## Liên Hệ & Hỗ Trợ

Nếu có câu hỏi về cách tạo tool hoặc cần hỗ trợ, vui lòng:
- Đọc kỹ các tài liệu hướng dẫn
- Tham khảo code mẫu trong EXAMPLE_TOOL_TEMPLATE.py
- Mở issue trên GitHub repository

---

📖 **Ghi chú**: Dự án này nhằm mục đích giáo dục, giúp hiểu cách tạo và cấu trúc các tool Python với giao diện console.
