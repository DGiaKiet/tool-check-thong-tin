# Kiến Trúc và Luồng Hoạt Động Của Tool

## Tổng Quan Kiến Trúc

### 1. Sơ Đồ Cấu Trúc High-Level

```
┌─────────────────────────────────────────────────────────┐
│                    TOOL ENTRY POINT                      │
│                    (xcattoolv2.py)                       │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                   INITIALIZATION                         │
│  - Load dependencies (pystyle, etc)                      │
│  - Setup configuration                                   │
│  - Initialize variables                                  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                   MAIN MENU LOOP                         │
│  ┌───────────────────────────────────────────┐          │
│  │  1. Display Banner                        │          │
│  │  2. Show Menu Options                     │          │
│  │  3. Get User Input                        │          │
│  │  4. Route to Feature Handler              │          │
│  └───────────────┬───────────────────────────┘          │
└──────────────────┼──────────────────────────────────────┘
                   │
        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐
   │Feature 1│ │Feature 2│ │Feature N│
   │ Handler │ │ Handler │ │ Handler │
   └────┬────┘ └────┬────┘ └────┬────┘
        │           │           │
        └───────────┴───────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │  Process & Display    │
        │      Results          │
        └───────────────────────┘
```

### 2. Kiến Trúc Module (Recommended Structure)

```
tool-check-thong-tin/
│
├── main.py                    # Entry point
│   └── main()                 # Main function
│
├── config.py                  # Configuration
│   ├── Config class
│   ├── API_KEYS
│   └── SETTINGS
│
├── ui/                        # User Interface
│   ├── __init__.py
│   ├── banner.py             # Banner display
│   ├── menu.py               # Menu system
│   └── styles.py             # Color themes
│
├── features/                  # Feature modules
│   ├── __init__.py
│   ├── check_phone.py        # Phone checker
│   ├── check_email.py        # Email checker
│   └── process_data.py       # Data processor
│
├── utils/                     # Utilities
│   ├── __init__.py
│   ├── validators.py         # Input validators
│   ├── file_handler.py       # File operations
│   └── api_client.py         # API interactions
│
└── requirements.txt           # Dependencies
```

## Luồng Hoạt Động Chi Tiết

### Flow 1: Khởi Động Tool

```
START
  │
  ▼
┌─────────────────────┐
│ Check Python Version│
│   (>= 3.6)          │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Import Dependencies │
│  - pystyle          │
│  - requests         │
│  - etc.             │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Load Configuration  │
│  - API keys         │
│  - Settings         │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Initialize Logger   │
│ (if enabled)        │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Clear Screen       │
│  Show Welcome       │
└──────┬──────────────┘
       │
       ▼
   MAIN LOOP
```

### Flow 2: Main Loop (Menu System)

```
┌────────────────────────────────────────┐
│         MAIN LOOP (Infinite)           │
│                                        │
│  ┌──────────────────────────────────┐ │
│  │ 1. Clear Screen                  │ │
│  │ 2. Display Banner                │ │
│  │ 3. Display Menu                  │ │
│  │ 4. Wait for Input                │ │
│  └─────────────┬────────────────────┘ │
│                │                       │
│                ▼                       │
│  ┌──────────────────────────────────┐ │
│  │     Validate Input               │ │
│  └─────────────┬────────────────────┘ │
│                │                       │
│       ┌────────┴────────┐             │
│       ▼                 ▼             │
│  ┌─────────┐      ┌──────────┐       │
│  │ Valid   │      │ Invalid  │       │
│  │ Choice  │      │ Choice   │       │
│  └────┬────┘      └────┬─────┘       │
│       │                │             │
│       │                ▼             │
│       │      ┌─────────────────┐    │
│       │      │ Show Error Msg  │    │
│       │      └─────────┬───────┘    │
│       │                │             │
│       │                │             │
│       └────────┬───────┘             │
│                │                       │
│                ▼                       │
│  ┌──────────────────────────────────┐ │
│  │    Call Feature Handler          │ │
│  └─────────────┬────────────────────┘ │
│                │                       │
│                ▼                       │
│  ┌──────────────────────────────────┐ │
│  │    Return to Loop                │ │
│  │    (unless exit selected)        │ │
│  └──────────────────────────────────┘ │
│                                        │
└────────────────────────────────────────┘
```

### Flow 3: Feature Handler (Example: Check Phone)

```
START Feature
     │
     ▼
┌──────────────────┐
│ Clear Screen     │
│ Show Feature     │
│ Banner           │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Prompt for Input │
│ (phone number)   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Validate Input   │
│ - Not empty?     │
│ - Correct format?│
└────────┬─────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌─────────┐
│ Valid  │ │ Invalid │
└───┬────┘ └────┬────┘
    │           │
    │           ▼
    │    ┌──────────────┐
    │    │ Show Error   │
    │    │ Return       │
    │    └──────────────┘
    │
    ▼
┌──────────────────┐
│ Show Loading     │
│ Animation        │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Process Data     │
│ - Clean format   │
│ - Check validity │
│ - Lookup info    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Format Results   │
│ - Create box     │
│ - Add colors     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Display Results  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Wait for Enter   │
└────────┬─────────┘
         │
         ▼
   RETURN TO MENU
```

## Components Chi Tiết

### 1. UI Layer (Giao Diện)

```python
# Nhiệm vụ:
- Hiển thị banner
- Tạo menu
- Hiển thị kết quả
- Apply colors và styles

# Key Functions:
def print_banner()
def print_menu()
def print_colored(text, color)
def show_loading(text, duration)
def create_box(text, title)
```

### 2. Input Validation Layer

```python
# Nhiệm vụ:
- Validate phone numbers
- Validate emails
- Validate URLs
- Sanitize inputs

# Key Functions:
def validate_phone(phone) -> (bool, str)
def validate_email(email) -> (bool, str)
def validate_url(url) -> (bool, str)
def sanitize_input(text) -> str
```

### 3. Business Logic Layer

```python
# Nhiệm vụ:
- Xử lý logic chính
- Gọi APIs
- Xử lý dữ liệu
- Format outputs

# Key Functions:
def check_phone_info(phone)
def lookup_email(email)
def process_bulk_data(file_path)
def generate_report(data)
```

### 4. Data Layer

```python
# Nhiệm vụ:
- Đọc/ghi file
- Cache results
- Log activities
- Store history

# Key Functions:
def read_file(path)
def write_file(path, data)
def cache_result(key, value)
def log_activity(action, details)
```

## Error Handling Flow

```
┌────────────────────────────────────┐
│         TRY BLOCK                  │
│                                    │
│  ┌──────────────────────────────┐ │
│  │   Execute Operation          │ │
│  └──────────────┬───────────────┘ │
└─────────────────┼──────────────────┘
                  │
         ┌────────┴────────┐
         │                 │
    SUCCESS            EXCEPTION
         │                 │
         ▼                 ▼
┌─────────────────┐  ┌─────────────────────┐
│  Return Result  │  │  EXCEPTION HANDLER  │
└─────────────────┘  │                     │
                     │  ┌───────────────┐  │
                     │  │ Specific      │  │
                     │  │ Exception?    │  │
                     │  └───┬───────────┘  │
                     │      │              │
                     │  ┌───┴────┐         │
                     │  │        │         │
                     │  ▼        ▼         │
                     │ Known  Unknown      │
                     │  │        │         │
                     │  ▼        ▼         │
                     │ Log    Log Full     │
                     │ Error  Traceback    │
                     │  │        │         │
                     │  └────┬───┘         │
                     │       │             │
                     │       ▼             │
                     │  Show User          │
                     │  Friendly Msg       │
                     │                     │
                     └─────────────────────┘
```

## Security Considerations

### 1. Input Sanitization Flow

```
User Input
    │
    ▼
┌──────────────────┐
│ Strip whitespace │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Remove dangerous │
│ characters       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Validate format  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Limit length     │
└────────┬─────────┘
         │
         ▼
  Clean Input
```

### 2. API Security

```
API Call Request
      │
      ▼
┌──────────────────┐
│ Use Environment  │
│ Variables for    │
│ API Keys         │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Use HTTPS Only   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Rate Limiting    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Timeout Handling │
└────────┬─────────┘
         │
         ▼
  Safe API Call
```

## Performance Optimization

### 1. Caching Strategy

```
Request for Data
      │
      ▼
┌──────────────────┐
│ Check Cache      │
└────────┬─────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌─────┐   ┌──────┐
│Found│   │Not   │
│     │   │Found │
└──┬──┘   └───┬──┘
   │          │
   │          ▼
   │     ┌──────────┐
   │     │ Fetch    │
   │     │ from API │
   │     └────┬─────┘
   │          │
   │          ▼
   │     ┌──────────┐
   │     │ Store in │
   │     │ Cache    │
   │     └────┬─────┘
   │          │
   └────┬─────┘
        │
        ▼
   Return Data
```

### 2. Async Operations (Advanced)

```
┌────────────────────────────────────┐
│       ASYNC OPERATIONS             │
│                                    │
│  Task 1 ────┐                     │
│             │                     │
│  Task 2 ────┼─── Run Parallel    │
│             │                     │
│  Task 3 ────┘                     │
│             │                     │
│             ▼                     │
│      Wait for All                 │
│             │                     │
│             ▼                     │
│      Aggregate Results            │
│                                    │
└────────────────────────────────────┘
```

## Deployment Architecture

### Option 1: Python Script
```
User → python tool.py → Direct Execution
```

### Option 2: Executable (PyInstaller)
```
User → tool.exe → Bundled Python Runtime → Execution
```

### Option 3: Web API (Advanced)
```
User → Browser → Flask/FastAPI → Tool Logic → Response
```

## Logging Architecture

```
Application Events
        │
        ▼
┌──────────────────┐
│  Logger Module   │
│                  │
│  ┌────────────┐  │
│  │ Log Levels │  │
│  │ - DEBUG    │  │
│  │ - INFO     │  │
│  │ - WARNING  │  │
│  │ - ERROR    │  │
│  │ - CRITICAL │  │
│  └────────────┘  │
└────────┬─────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌─────────┐ ┌──────────┐
│ Console │ │   File   │
│ Output  │ │  Output  │
└─────────┘ └──────────┘
```

## Kết Luận

Kiến trúc tool được thiết kế theo nguyên tắc:

1. **Separation of Concerns**: Tách biệt UI, logic, data
2. **Modularity**: Dễ mở rộng và bảo trì
3. **Error Handling**: Xử lý lỗi toàn diện
4. **Security**: Validate input, bảo mật API
5. **Performance**: Caching, async operations
6. **User Experience**: Loading, feedback, clear messages

Sử dụng các sơ đồ này để hiểu rõ và thiết kế tool của bạn!
