"""
API Configuration Template
===========================
File này là template để cấu hình API keys cho tool.

⚠️  QUAN TRỌNG:
1. Copy file này thành `api_config.py`
2. Điền API keys của bạn vào
3. KHÔNG commit file api_config.py lên GitHub (đã có trong .gitignore)

📝 Cách sử dụng:
    cp api_config_template.py api_config.py
    # Sau đó sửa api_config.py và điền API keys

Author: Template
Version: 1.0
"""

# ============================================
# API KEYS CONFIGURATION
# ============================================

class APIConfig:
    """
    Cấu hình API keys cho các services
    
    🔐 BẢO MẬT:
    - Đổi tên file này thành `api_config.py`
    - Thay thế các giá trị 'YOUR_xxx_KEY_HERE' bằng API keys thật
    - File api_config.py đã được add vào .gitignore
    - KHÔNG BAO GIỜ commit API keys lên GitHub
    """
    
    # ============================================
    # PHONE VALIDATION APIs
    # ============================================
    
    # Numverify API - https://numverify.com/
    # Free: 100 requests/month
    # Đăng ký: https://numverify.com/product
    NUMVERIFY_API_KEY = "YOUR_NUMVERIFY_KEY_HERE"
    
    # Abstract API Phone Validation - https://www.abstractapi.com/phone-validation-api
    # Free: 250 requests/month
    # Đăng ký: https://app.abstractapi.com/users/signup
    ABSTRACT_PHONE_API_KEY = "YOUR_ABSTRACT_PHONE_KEY_HERE"
    
    # ============================================
    # EMAIL VALIDATION APIs
    # ============================================
    
    # Hunter.io Email Verifier - https://hunter.io/email-verifier
    # Free: 50 verifications/month
    # Đăng ký: https://hunter.io/users/sign_up
    HUNTER_API_KEY = "YOUR_HUNTER_KEY_HERE"
    
    # EmailValidation.io - https://emailvalidation.io/
    # Free: 1,000 validations/month
    # Đăng ký: https://emailvalidation.io/pricing
    EMAILVALIDATION_API_KEY = "YOUR_EMAILVALIDATION_KEY_HERE"
    
    # ============================================
    # URL & SECURITY APIs
    # ============================================
    
    # URLScan.io - https://urlscan.io/
    # Free: Unlimited (với rate limits)
    # Đăng ký: https://urlscan.io/user/signup
    URLSCAN_API_KEY = "YOUR_URLSCAN_KEY_HERE"
    
    # IP Geolocation API - https://ipgeolocation.io/
    # Free: 1,000 requests/day
    # Đăng ký: https://ipgeolocation.io/signup.html
    IPGEOLOCATION_API_KEY = "YOUR_IPGEOLOCATION_KEY_HERE"
    
    # ============================================
    # SOCIAL MEDIA APIs
    # ============================================
    
    # Clearbit Enrichment API - https://clearbit.com/enrichment
    # Free: 50 requests/month
    # Đăng ký: https://dashboard.clearbit.com/signup
    CLEARBIT_API_KEY = "YOUR_CLEARBIT_KEY_HERE"
    
    # Facebook Graph API - https://developers.facebook.com/
    # Free: Standard access
    # Đăng ký: https://developers.facebook.com/apps/
    # Lưu ý: Cần tạo App và lấy Access Token
    FACEBOOK_ACCESS_TOKEN = "YOUR_FACEBOOK_ACCESS_TOKEN_HERE"
    FACEBOOK_APP_ID = "YOUR_FACEBOOK_APP_ID_HERE"
    FACEBOOK_APP_SECRET = "YOUR_FACEBOOK_APP_SECRET_HERE"
    
    # ============================================
    # OTHER USEFUL APIs
    # ============================================
    
    # IPInfo.io - https://ipinfo.io/
    # Free: 50,000 requests/month
    # Đăng ký: https://ipinfo.io/signup
    IPINFO_API_KEY = "YOUR_IPINFO_KEY_HERE"
    
    # Have I Been Pwned - https://haveibeenpwned.com/API/v3
    # Paid: API key required cho automated access
    # Đăng ký: https://haveibeenpwned.com/API/Key
    HIBP_API_KEY = "YOUR_HIBP_KEY_HERE"  # Optional - có rate limit nếu không có key
    
    # ============================================
    # ADVANCED CONFIGURATION
    # ============================================
    
    # Bật/tắt từng API
    ENABLE_NUMVERIFY = True
    ENABLE_ABSTRACT_PHONE = True
    ENABLE_HUNTER = True
    ENABLE_EMAILVALIDATION = True
    ENABLE_URLSCAN = True
    ENABLE_IPGEOLOCATION = True
    ENABLE_CLEARBIT = True
    ENABLE_FACEBOOK = False  # Tắt mặc định vì cần setup phức tạp
    ENABLE_IPINFO = True
    ENABLE_HIBP = False  # Tắt mặc định vì cần pay
    
    # Timeouts (seconds)
    API_TIMEOUT = 10
    
    # Retry settings
    MAX_RETRIES = 3
    RETRY_DELAY = 1  # seconds
    
    # Cache settings (hours)
    CACHE_DURATION = 24  # 24 hours


# ============================================
# HELPER FUNCTIONS
# ============================================

def check_api_keys():
    """
    Kiểm tra xem API keys nào đã được cấu hình
    
    Returns:
        dict: Status của từng API key
    """
    keys_status = {}
    
    # Phone APIs
    keys_status['Numverify'] = {
        'configured': APIConfig.NUMVERIFY_API_KEY != "YOUR_NUMVERIFY_KEY_HERE",
        'enabled': APIConfig.ENABLE_NUMVERIFY
    }
    
    keys_status['Abstract Phone'] = {
        'configured': APIConfig.ABSTRACT_PHONE_API_KEY != "YOUR_ABSTRACT_PHONE_KEY_HERE",
        'enabled': APIConfig.ENABLE_ABSTRACT_PHONE
    }
    
    # Email APIs
    keys_status['Hunter.io'] = {
        'configured': APIConfig.HUNTER_API_KEY != "YOUR_HUNTER_KEY_HERE",
        'enabled': APIConfig.ENABLE_HUNTER
    }
    
    keys_status['EmailValidation'] = {
        'configured': APIConfig.EMAILVALIDATION_API_KEY != "YOUR_EMAILVALIDATION_KEY_HERE",
        'enabled': APIConfig.ENABLE_EMAILVALIDATION
    }
    
    # URL & Security APIs
    keys_status['URLScan'] = {
        'configured': APIConfig.URLSCAN_API_KEY != "YOUR_URLSCAN_KEY_HERE",
        'enabled': APIConfig.ENABLE_URLSCAN
    }
    
    keys_status['IP Geolocation'] = {
        'configured': APIConfig.IPGEOLOCATION_API_KEY != "YOUR_IPGEOLOCATION_KEY_HERE",
        'enabled': APIConfig.ENABLE_IPGEOLOCATION
    }
    
    # Social Media APIs
    keys_status['Clearbit'] = {
        'configured': APIConfig.CLEARBIT_API_KEY != "YOUR_CLEARBIT_KEY_HERE",
        'enabled': APIConfig.ENABLE_CLEARBIT
    }
    
    keys_status['Facebook'] = {
        'configured': APIConfig.FACEBOOK_ACCESS_TOKEN != "YOUR_FACEBOOK_ACCESS_TOKEN_HERE",
        'enabled': APIConfig.ENABLE_FACEBOOK
    }
    
    # Other APIs
    keys_status['IPInfo'] = {
        'configured': APIConfig.IPINFO_API_KEY != "YOUR_IPINFO_KEY_HERE",
        'enabled': APIConfig.ENABLE_IPINFO
    }
    
    keys_status['HIBP'] = {
        'configured': APIConfig.HIBP_API_KEY != "YOUR_HIBP_KEY_HERE",
        'enabled': APIConfig.ENABLE_HIBP
    }
    
    return keys_status


def print_api_status():
    """In ra status của các API keys"""
    print("=" * 60)
    print("API KEYS STATUS")
    print("=" * 60)
    
    status = check_api_keys()
    
    for api_name, info in status.items():
        if info['configured'] and info['enabled']:
            status_str = "✅ READY"
        elif info['configured'] and not info['enabled']:
            status_str = "⚠️  CONFIGURED BUT DISABLED"
        elif not info['configured'] and info['enabled']:
            status_str = "❌ NOT CONFIGURED"
        else:
            status_str = "⚪ DISABLED"
        
        print(f"{api_name:20} : {status_str}")
    
    print("=" * 60)
    
    # Đếm số APIs ready
    ready_count = sum(1 for info in status.values() if info['configured'] and info['enabled'])
    total_count = len(status)
    
    print(f"\n📊 Summary: {ready_count}/{total_count} APIs ready to use")
    
    if ready_count == 0:
        print("\n⚠️  WARNING: No APIs configured!")
        print("Please edit api_config.py and add your API keys.")
        print("See FREE_APIS_GUIDE.md for registration links.")


def get_configured_apis():
    """
    Lấy danh sách các APIs đã được cấu hình và enabled
    
    Returns:
        list: Tên các APIs sẵn sàng sử dụng
    """
    status = check_api_keys()
    return [name for name, info in status.items() 
            if info['configured'] and info['enabled']]


# ============================================
# EXAMPLE USAGE
# ============================================

if __name__ == "__main__":
    """
    Test script để kiểm tra API configuration
    
    Chạy script này sau khi đã điền API keys:
        python api_config.py
    """
    print("\n" + "=" * 60)
    print("API CONFIGURATION TEST")
    print("=" * 60 + "\n")
    
    print("📝 Checking API keys configuration...\n")
    
    # Print status
    print_api_status()
    
    # Get configured APIs
    configured = get_configured_apis()
    
    if configured:
        print(f"\n✅ Configured APIs: {', '.join(configured)}")
    else:
        print("\n❌ No APIs configured yet!")
        print("\n📋 Next steps:")
        print("1. Copy this file to api_config.py:")
        print("   cp api_config_template.py api_config.py")
        print("\n2. Edit api_config.py and replace placeholders with real API keys")
        print("\n3. See FREE_APIS_GUIDE.md for registration links")
        print("\n4. Run this script again to verify")
    
    print("\n" + "=" * 60)
    print("For detailed API documentation, see:")
    print("📚 FREE_APIS_GUIDE.md")
    print("=" * 60 + "\n")
