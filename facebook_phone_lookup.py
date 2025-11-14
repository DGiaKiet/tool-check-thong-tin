"""
Facebook Phone Lookup Module
=============================
Module tra cứu số điện thoại từ Facebook profile link

Author: Template
Version: 1.0

LƯU Ý BẢO MẬT:
- Module này chỉ demo cách trích xuất thông tin công khai
- Không sử dụng cho mục đích xâm phạm privacy
- Tuân thủ Terms of Service của Facebook
"""

import re
import json

# ============================================
# CONFIGURATION
# ============================================

class FacebookConfig:
    """Cấu hình cho Facebook lookup"""
    
    # Patterns để parse Facebook URLs
    FACEBOOK_URL_PATTERNS = [
        r'facebook\.com/([^/?]+)',
        r'fb\.com/([^/?]+)',
        r'facebook\.com/profile\.php\?id=(\d+)',
        r'm\.facebook\.com/([^/?]+)',
    ]
    
    # User agents để simulate browser request
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    ]

# ============================================
# VALIDATION FUNCTIONS
# ============================================

def validate_facebook_url(url):
    """
    Validate Facebook URL
    
    Args:
        url (str): URL cần validate
        
    Returns:
        tuple: (is_valid, username_or_id, error_message)
    """
    if not url or not url.strip():
        return False, None, "URL không được để trống"
    
    url = url.strip()
    
    # Kiểm tra có phải Facebook URL không
    if 'facebook.com' not in url and 'fb.com' not in url:
        return False, None, "Không phải Facebook URL"
    
    # Thử extract username/ID từ URL
    for pattern in FacebookConfig.FACEBOOK_URL_PATTERNS:
        match = re.search(pattern, url)
        if match:
            username_or_id = match.group(1)
            return True, username_or_id, None
    
    return False, None, "URL không đúng định dạng"

def extract_phone_from_text(text):
    """
    Extract phone numbers từ text
    
    Args:
        text (str): Text cần extract
        
    Returns:
        list: Danh sách số điện thoại tìm được
    """
    # Patterns cho số điện thoại Việt Nam
    phone_patterns = [
        r'(\+84|0)[0-9]{9,10}',  # Format chuẩn
        r'(\+84|0)\s?[0-9]{3}\s?[0-9]{3}\s?[0-9]{3,4}',  # Có khoảng trắng
        r'(\+84|0)[0-9]{2}[.-][0-9]{3}[.-][0-9]{4}',  # Có dấu chấm/gạch
    ]
    
    phones = []
    for pattern in phone_patterns:
        matches = re.findall(pattern, text)
        phones.extend(matches)
    
    # Clean và unique
    cleaned_phones = []
    for phone in phones:
        if isinstance(phone, tuple):
            phone = ''.join(phone)
        # Remove spaces, dots, dashes
        clean = re.sub(r'[\s\.\-]', '', phone)
        if clean and clean not in cleaned_phones:
            cleaned_phones.append(clean)
    
    return cleaned_phones

# ============================================
# MAIN LOOKUP FUNCTIONS
# ============================================

def lookup_phone_from_facebook(facebook_url, method='demo'):
    """
    Tra cứu số điện thoại từ Facebook URL
    
    Args:
        facebook_url (str): Facebook profile URL
        method (str): Phương thức tra cứu ('demo', 'api', 'scrape')
        
    Returns:
        dict: Kết quả tra cứu
    """
    # Validate URL
    is_valid, username, error = validate_facebook_url(facebook_url)
    
    if not is_valid:
        return {
            'success': False,
            'error': error,
            'url': facebook_url
        }
    
    # Tùy theo method, gọi function tương ứng
    if method == 'demo':
        return _lookup_demo(facebook_url, username)
    elif method == 'api':
        return _lookup_via_api(facebook_url, username)
    elif method == 'scrape':
        return _lookup_via_scraping(facebook_url, username)
    else:
        return {
            'success': False,
            'error': f'Method không hợp lệ: {method}',
            'url': facebook_url
        }

def _lookup_demo(url, username):
    """
    Demo mode - trả về dữ liệu mẫu
    
    QUAN TRỌNG: Đây chỉ là demo, không tra cứu thực tế
    """
    import random
    
    # Simulate processing time
    import time
    time.sleep(1)
    
    # Demo data
    demo_phones = [
        '0912345678',
        '0987654321',
        '0123456789',
    ]
    
    return {
        'success': True,
        'method': 'demo',
        'url': url,
        'username': username,
        'phones': [random.choice(demo_phones)] if random.random() > 0.3 else [],
        'note': '⚠️ Đây là dữ liệu DEMO, không phải kết quả thực tế',
        'message': 'Trong môi trường production, cần implement API hoặc web scraping'
    }

def _lookup_via_api(url, username):
    """
    Tra cứu qua API (cần API key)
    
    LƯU Ý: 
    - Cần đăng ký API key từ Facebook Graph API
    - Cần permissions phù hợp
    - Tuân thủ rate limits
    """
    # TODO: Implement API lookup
    # Ví dụ sử dụng Facebook Graph API:
    # 
    # import requests
    # 
    # access_token = 'YOUR_ACCESS_TOKEN'
    # graph_url = f'https://graph.facebook.com/v12.0/{username}'
    # params = {
    #     'fields': 'name,email',  # phone thường không public
    #     'access_token': access_token
    # }
    # 
    # response = requests.get(graph_url, params=params)
    # data = response.json()
    
    return {
        'success': False,
        'method': 'api',
        'url': url,
        'username': username,
        'error': 'API method chưa được implement',
        'note': 'Cần Facebook API key và permissions để sử dụng'
    }

def _lookup_via_scraping(url, username):
    """
    Tra cứu qua web scraping
    
    LƯU Ý BẢO MẬT:
    - Web scraping Facebook vi phạm Terms of Service
    - Có thể bị block IP
    - Chỉ nên scrape thông tin công khai và với permission
    """
    # TODO: Implement scraping (CHÚ Ý: có thể vi phạm ToS)
    # Ví dụ concept:
    #
    # import requests
    # from bs4 import BeautifulSoup
    # 
    # headers = {'User-Agent': FacebookConfig.USER_AGENTS[0]}
    # response = requests.get(url, headers=headers)
    # soup = BeautifulSoup(response.content, 'html.parser')
    # 
    # # Extract phone từ HTML
    # phones = extract_phone_from_text(soup.get_text())
    
    return {
        'success': False,
        'method': 'scrape',
        'url': url,
        'username': username,
        'error': 'Scraping method chưa được implement',
        'note': '⚠️ Web scraping Facebook có thể vi phạm Terms of Service'
    }

# ============================================
# HELPER FUNCTIONS
# ============================================

def format_phone_vn(phone):
    """
    Format số điện thoại VN về dạng chuẩn
    
    Args:
        phone (str): Số điện thoại
        
    Returns:
        str: Số điện thoại đã format
    """
    # Remove all non-digits
    clean = re.sub(r'\D', '', phone)
    
    # Convert +84 to 0
    if clean.startswith('84'):
        clean = '0' + clean[2:]
    
    # Format: 0xxx xxx xxx
    if len(clean) == 10:
        return f"{clean[:4]} {clean[4:7]} {clean[7:]}"
    elif len(clean) == 11:
        return f"{clean[:4]} {clean[4:7]} {clean[7:]}"
    
    return phone

def get_carrier_info(phone):
    """
    Lấy thông tin nhà mạng từ đầu số
    
    Args:
        phone (str): Số điện thoại
        
    Returns:
        str: Tên nhà mạng
    """
    clean = re.sub(r'\D', '', phone)
    if clean.startswith('84'):
        clean = '0' + clean[2:]
    
    # Mapping đầu số -> nhà mạng (cập nhật 2024)
    carriers = {
        'Viettel': ['032', '033', '034', '035', '036', '037', '038', '039', '086', '096', '097', '098'],
        'Vinaphone': ['081', '082', '083', '084', '085', '088', '091', '094'],
        'Mobifone': ['070', '076', '077', '078', '079', '089', '090', '093'],
        'Vietnamobile': ['052', '056', '058', '092'],
        'Gmobile': ['059', '099'],
    }
    
    prefix = clean[:3] if len(clean) >= 3 else ''
    
    for carrier, prefixes in carriers.items():
        if prefix in prefixes:
            return carrier
    
    return 'Không xác định'

# ============================================
# EXAMPLE USAGE
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("FACEBOOK PHONE LOOKUP MODULE - TEST")
    print("=" * 60)
    
    # Test 1: Validate URL
    print("\n[TEST 1] Validate Facebook URLs:")
    test_urls = [
        "https://facebook.com/username",
        "https://www.facebook.com/profile.php?id=123456789",
        "https://m.facebook.com/username",
        "https://fb.com/username",
        "not-a-facebook-url",
    ]
    
    for url in test_urls:
        is_valid, username, error = validate_facebook_url(url)
        print(f"  {url[:40]:40} -> Valid: {is_valid}, User: {username}")
    
    # Test 2: Extract phones from text
    print("\n[TEST 2] Extract phone numbers:")
    test_text = """
    Contact me at: 0912345678 or +84987654321
    Phone: 0123 456 789
    Mobile: 0999-888-777
    """
    phones = extract_phone_from_text(test_text)
    print(f"  Found phones: {phones}")
    
    # Test 3: Lookup demo
    print("\n[TEST 3] Lookup phone (demo mode):")
    result = lookup_phone_from_facebook("https://facebook.com/testuser", method='demo')
    print(f"  Result: {json.dumps(result, indent=2, ensure_ascii=False)}")
    
    # Test 4: Format phone
    print("\n[TEST 4] Format phone numbers:")
    test_phones = ['0912345678', '+84987654321', '0123456789']
    for phone in test_phones:
        formatted = format_phone_vn(phone)
        carrier = get_carrier_info(phone)
        print(f"  {phone} -> {formatted} ({carrier})")
    
    print("\n" + "=" * 60)
