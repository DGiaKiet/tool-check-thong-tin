# Hướng Dẫn Sử Dụng APIs Miễn Phí

## 📚 Tổng Quan

Tài liệu này liệt kê các APIs miễn phí mà bạn có thể tích hợp vào tool để thêm các tính năng tra cứu và xác thực thông tin.

## 🌐 APIs Miễn Phí Cho Tool

### 1. APIs Kiểm Tra Số Điện Thoại

#### 📱 Numverify (Khuyến nghị)
**Website**: https://numverify.com/

**Miễn phí**: 100 requests/tháng

**Tính năng**:
- Xác thực format số điện thoại
- Lấy thông tin quốc gia
- Xác định loại số (mobile/landline)
- Lấy thông tin carrier

**Code mẫu**:
```python
import requests

def check_phone_with_numverify(phone_number, api_key):
    """
    Kiểm tra số điện thoại bằng Numverify API
    
    Args:
        phone_number (str): Số điện thoại cần kiểm tra
        api_key (str): API key từ numverify.com
    
    Returns:
        dict: Thông tin số điện thoại
    """
    url = "http://apilayer.net/api/validate"
    
    params = {
        'access_key': api_key,
        'number': phone_number,
        'country_code': 'VN',  # Vietnam
        'format': 1
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data.get('valid'):
            return {
                'success': True,
                'phone': data.get('international_format'),
                'country': data.get('country_name'),
                'carrier': data.get('carrier'),
                'line_type': data.get('line_type'),
                'location': data.get('location')
            }
        else:
            return {
                'success': False,
                'error': 'Số điện thoại không hợp lệ'
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

# Sử dụng
API_KEY = "YOUR_NUMVERIFY_API_KEY"
result = check_phone_with_numverify("0912345678", API_KEY)
print(result)
```

**Cách lấy API Key**:
1. Truy cập: https://numverify.com/product
2. Sign Up (miễn phí)
3. Vào Dashboard → lấy API Key
4. Thay thế `YOUR_NUMVERIFY_API_KEY` trong code

---

#### 📱 Abstract API Phone Validation
**Website**: https://www.abstractapi.com/phone-validation-api

**Miễn phí**: 250 requests/tháng

**Code mẫu**:
```python
import requests

def check_phone_abstract(phone, api_key):
    url = f"https://phonevalidation.abstractapi.com/v1/"
    
    params = {
        'api_key': api_key,
        'phone': phone
    }
    
    response = requests.get(url, params=params)
    return response.json()
```

---

### 2. APIs Kiểm Tra Email

#### 📧 Hunter.io Email Verifier
**Website**: https://hunter.io/email-verifier

**Miễn phí**: 50 verifications/tháng

**Code mẫu**:
```python
import requests

def verify_email_hunter(email, api_key):
    """
    Xác thực email bằng Hunter.io API
    
    Args:
        email (str): Email cần kiểm tra
        api_key (str): API key từ hunter.io
    
    Returns:
        dict: Thông tin về email
    """
    url = "https://api.hunter.io/v2/email-verifier"
    
    params = {
        'email': email,
        'api_key': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if 'data' in data:
            result = data['data']
            return {
                'success': True,
                'email': result.get('email'),
                'status': result.get('status'),  # valid, invalid, accept_all
                'score': result.get('score'),  # 0-100
                'mx_records': result.get('mx_records'),
                'smtp_check': result.get('smtp_check')
            }
        else:
            return {
                'success': False,
                'error': 'Không thể xác thực email'
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

# Sử dụng
API_KEY = "YOUR_HUNTER_API_KEY"
result = verify_email_hunter("test@example.com", API_KEY)
print(result)
```

---

#### 📧 EmailValidation.io
**Website**: https://emailvalidation.io/

**Miễn phí**: 1000 validations/tháng

**Code mẫu**:
```python
import requests

def verify_email_io(email, api_key):
    url = f"https://api.emailvalidation.io/v1/info"
    
    params = {
        'email': email,
        'apikey': api_key
    }
    
    response = requests.get(url, params=params)
    return response.json()
```

---

### 3. APIs Kiểm Tra URL & Domain

#### 🔗 URLScan.io
**Website**: https://urlscan.io/

**Miễn phí**: Không giới hạn (có rate limit)

**Code mẫu**:
```python
import requests
import time

def scan_url(url, api_key):
    """
    Quét URL để kiểm tra an toàn
    
    Args:
        url (str): URL cần quét
        api_key (str): API key từ urlscan.io
    
    Returns:
        dict: Kết quả quét
    """
    # Submit URL để quét
    submit_url = "https://urlscan.io/api/v1/scan/"
    
    headers = {
        'API-Key': api_key,
        'Content-Type': 'application/json'
    }
    
    data = {
        'url': url,
        'visibility': 'public'
    }
    
    try:
        # Submit
        response = requests.post(submit_url, json=data, headers=headers)
        result = response.json()
        
        if 'uuid' in result:
            scan_id = result['uuid']
            
            # Đợi kết quả (thường 5-10 giây)
            time.sleep(10)
            
            # Lấy kết quả
            result_url = f"https://urlscan.io/api/v1/result/{scan_id}/"
            result_response = requests.get(result_url)
            scan_result = result_response.json()
            
            return {
                'success': True,
                'url': url,
                'page_title': scan_result.get('page', {}).get('title'),
                'ip': scan_result.get('page', {}).get('ip'),
                'country': scan_result.get('page', {}).get('country'),
                'server': scan_result.get('page', {}).get('server'),
                'screenshot': result.get('screenshot'),
                'malicious': scan_result.get('verdicts', {}).get('malicious')
            }
        else:
            return {
                'success': False,
                'error': 'Không thể quét URL'
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }
```

---

#### 🔗 IP Geolocation API
**Website**: https://ipgeolocation.io/

**Miễn phí**: 1000 requests/ngày

**Code mẫu**:
```python
import requests

def get_domain_info(domain, api_key):
    url = "https://api.ipgeolocation.io/ipgeo"
    
    params = {
        'apiKey': api_key,
        'ip': domain
    }
    
    response = requests.get(url, params=params)
    return response.json()
```

---

### 4. APIs Tra Cứu Thông Tin Social Media

#### 🔍 Clearbit Enrichment API
**Website**: https://clearbit.com/enrichment

**Miễn phí**: 50 requests/tháng

**Code mẫu**:
```python
import requests

def enrich_email(email, api_key):
    """
    Lấy thông tin từ email (tìm social profiles)
    
    Args:
        email (str): Email address
        api_key (str): Clearbit API key
    
    Returns:
        dict: Thông tin người dùng
    """
    url = f"https://person.clearbit.com/v2/combined/find"
    
    params = {
        'email': email
    }
    
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            person = data.get('person', {})
            
            return {
                'success': True,
                'name': person.get('name', {}).get('fullName'),
                'bio': person.get('bio'),
                'location': person.get('location'),
                'facebook': person.get('facebook', {}).get('handle'),
                'twitter': person.get('twitter', {}).get('handle'),
                'linkedin': person.get('linkedin', {}).get('handle'),
                'github': person.get('github', {}).get('handle')
            }
        else:
            return {
                'success': False,
                'error': 'Không tìm thấy thông tin'
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }
```

---

### 5. APIs Khác Hữu Ích

#### 🌍 IPInfo.io - Tra Cứu IP
**Website**: https://ipinfo.io/

**Miễn phí**: 50,000 requests/tháng

```python
import requests

def get_ip_info(ip_address, api_key):
    url = f"https://ipinfo.io/{ip_address}/json"
    
    params = {
        'token': api_key
    }
    
    response = requests.get(url, params=params)
    return response.json()
```

---

#### 🔐 Have I Been Pwned - Kiểm Tra Data Breach
**Website**: https://haveibeenpwned.com/API/v3

**Miễn phí**: Có giới hạn rate

```python
import requests

def check_email_breach(email, api_key):
    """
    Kiểm tra email có bị rò rỉ không
    """
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    
    headers = {
        'hibp-api-key': api_key,
        'user-agent': 'YourToolName'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return {
            'success': True,
            'breached': True,
            'breaches': response.json()
        }
    elif response.status_code == 404:
        return {
            'success': True,
            'breached': False
        }
    else:
        return {
            'success': False,
            'error': 'Không thể kiểm tra'
        }
```

---

## 🔧 Tích Hợp Vào Tool

### File Config Mẫu

Tạo file `api_config.py`:

```python
"""
API Configuration File
======================
Lưu API keys của bạn ở đây
⚠️ QUAN TRỌNG: Không commit file này lên GitHub!
"""

class APIConfig:
    """Cấu hình API keys"""
    
    # Phone Validation
    NUMVERIFY_API_KEY = "your_numverify_key_here"
    ABSTRACT_PHONE_API_KEY = "your_abstract_key_here"
    
    # Email Validation
    HUNTER_API_KEY = "your_hunter_key_here"
    EMAILVALIDATION_API_KEY = "your_emailvalidation_key_here"
    
    # URL & Security
    URLSCAN_API_KEY = "your_urlscan_key_here"
    IPGEOLOCATION_API_KEY = "your_ipgeo_key_here"
    
    # Social Media
    CLEARBIT_API_KEY = "your_clearbit_key_here"
    
    # Others
    IPINFO_API_KEY = "your_ipinfo_key_here"
    HIBP_API_KEY = "your_hibp_key_here"

# Kiểm tra API keys đã được set chưa
def check_api_keys():
    """Kiểm tra xem API keys đã được cấu hình chưa"""
    keys = {
        'Numverify': APIConfig.NUMVERIFY_API_KEY,
        'Hunter.io': APIConfig.HUNTER_API_KEY,
        'URLScan': APIConfig.URLSCAN_API_KEY,
    }
    
    for name, key in keys.items():
        if key and key != f"your_{name.lower()}_key_here":
            print(f"✅ {name}: Configured")
        else:
            print(f"❌ {name}: Not configured")
```

### Thêm vào `.gitignore`

```bash
# API Configuration - KHÔNG COMMIT
api_config.py
*.key
.env
```

### Sử dụng Trong Tool

Cập nhật `EXAMPLE_TOOL_TEMPLATE.py`:

```python
# Import API config
try:
    from api_config import APIConfig
    API_CONFIGURED = True
except ImportError:
    API_CONFIGURED = False
    print("[!] api_config.py không tìm thấy. Tạo file này để sử dụng APIs.")

# Trong feature function
def feature_check_phone_advanced():
    """Kiểm tra số điện thoại với API"""
    clear_screen()
    print_banner()
    
    if not API_CONFIGURED:
        print_colored("\n[!] API chưa được cấu hình!", Config.COLOR_ERROR)
        print("\nĐể sử dụng tính năng này:")
        print("1. Tạo file api_config.py")
        print("2. Thêm API keys vào file")
        print("3. Xem FREE_APIS_GUIDE.md để biết cách lấy API keys")
        press_enter()
        return
    
    phone = input_with_prompt("\n[?] Nhập số điện thoại: ", Config.COLOR_INFO)
    
    show_loading("Đang kiểm tra qua API...", 3)
    
    # Sử dụng API
    result = check_phone_with_numverify(phone, APIConfig.NUMVERIFY_API_KEY)
    
    # Hiển thị kết quả
    if result['success']:
        print_colored(f"\n✅ Số điện thoại hợp lệ!", Config.COLOR_SUCCESS)
        print(f"  Carrier: {result['carrier']}")
        print(f"  Location: {result['location']}")
    else:
        print_colored(f"\n❌ {result['error']}", Config.COLOR_ERROR)
```

---

## 📋 Checklist Sử Dụng APIs

### Trước Khi Bắt Đầu

- [ ] Đọc Terms of Service của từng API
- [ ] Đăng ký tài khoản trên các platform
- [ ] Lấy API keys
- [ ] Tạo file `api_config.py`
- [ ] Add `api_config.py` vào `.gitignore`
- [ ] Test từng API riêng lẻ
- [ ] Kiểm tra rate limits

### Best Practices

✅ **DO**:
- Lưu API keys trong file config riêng
- Add config file vào `.gitignore`
- Handle errors gracefully
- Respect rate limits
- Cache results khi có thể
- Log API usage

❌ **DON'T**:
- Commit API keys lên GitHub
- Hardcode API keys trong code
- Vượt quá rate limits
- Share API keys
- Ignore error handling

---

## 🚀 Quick Start

### 1. Chọn APIs Bạn Cần

```bash
# Ví dụ: Chỉ cần phone validation
- Numverify (100 req/tháng)
- Abstract API (250 req/tháng)
```

### 2. Đăng Ký và Lấy Keys

```bash
# 1. Truy cập website
# 2. Sign up
# 3. Verify email
# 4. Vào Dashboard
# 5. Copy API key
```

### 3. Tạo Config File

```bash
# Tạo file mới
touch api_config.py

# Copy template từ phần trên
# Thay YOUR_KEY bằng API key thật
```

### 4. Test

```python
# Test đơn giản
python3 -c "
from api_config import APIConfig
print('API Keys loaded successfully!')
print(f'Numverify: {APIConfig.NUMVERIFY_API_KEY[:10]}...')
"
```

---

## 💡 Tips & Tricks

### Tối Ưu Sử Dụng APIs Miễn Phí

1. **Caching**: Lưu kết quả đã tra cứu
```python
import json
from datetime import datetime, timedelta

cache = {}

def cached_api_call(key, api_function, *args, cache_hours=24):
    if key in cache:
        cached_time, cached_result = cache[key]
        if datetime.now() - cached_time < timedelta(hours=cache_hours):
            return cached_result
    
    result = api_function(*args)
    cache[key] = (datetime.now(), result)
    return result
```

2. **Rate Limiting**: Tránh vượt quá giới hạn
```python
import time
from datetime import datetime

class RateLimiter:
    def __init__(self, max_calls, period_seconds):
        self.max_calls = max_calls
        self.period = period_seconds
        self.calls = []
    
    def wait_if_needed(self):
        now = datetime.now()
        self.calls = [t for t in self.calls 
                     if (now - t).seconds < self.period]
        
        if len(self.calls) >= self.max_calls:
            sleep_time = self.period - (now - self.calls[0]).seconds
            time.sleep(sleep_time)
        
        self.calls.append(now)

# Sử dụng
limiter = RateLimiter(max_calls=100, period_seconds=3600)  # 100 calls/hour
limiter.wait_if_needed()
result = api_call()
```

3. **Fallback Strategy**: Dùng nhiều APIs
```python
def check_phone_with_fallback(phone):
    # Try API 1
    try:
        return check_with_numverify(phone)
    except:
        pass
    
    # Try API 2
    try:
        return check_with_abstract(phone)
    except:
        pass
    
    # Fallback to offline validation
    return validate_phone_offline(phone)
```

---

## 📚 Resources

### Tìm Thêm APIs Miễn Phí

- **RapidAPI**: https://rapidapi.com/hub (marketplace lớn nhất)
- **Public APIs**: https://github.com/public-apis/public-apis
- **API List**: https://apilist.fun/
- **FreeAPI**: https://free-apis.github.io/

### Documentation

- Mỗi API đều có docs chi tiết
- Đọc kỹ rate limits
- Xem code examples
- Join community/forums

---

## ⚠️ Lưu Ý Quan Trọng

1. **Security**: Không bao giờ commit API keys
2. **Rate Limits**: Respect giới hạn của free tier
3. **Terms of Service**: Đọc và tuân thủ ToS
4. **Backup Plan**: Có fallback khi API down
5. **Monitoring**: Track API usage của bạn

---

## 🎓 Kết Luận

Với các APIs miễn phí này, bạn có thể:
- ✅ Xác thực số điện thoại chính xác
- ✅ Verify email addresses
- ✅ Quét URLs an toàn
- ✅ Tra cứu thông tin IP/domain
- ✅ Tìm social media profiles

**Next Steps**:
1. Chọn APIs phù hợp với nhu cầu
2. Đăng ký và lấy API keys
3. Tích hợp vào tool
4. Test kỹ càng
5. Deploy và sử dụng!

---

**Happy Coding!** 🚀

*Document được tạo cho DGiaKiet/tool-check-thong-tin*
