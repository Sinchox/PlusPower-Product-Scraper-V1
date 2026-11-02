from parser import is_challenge_page, parse_product

def test_cloudflare_challenge_detection():
    assert is_challenge_page("<html><title>Just a moment...</title><body>Checking your browser</body></html>")

def test_rate_limit_detection():
    assert is_challenge_page("too many requests", 429)

def test_jsonld_product_parse():
    html = '''<html><script type="application/ld+json">{"@context":"https://schema.org","@type":"Product","name":"Test Whey","sku":"ABC1","offers":{"price":"29.90","priceCurrency":"EUR"}}</script></html>'''
    product = parse_product(html, "https://example.com/test")
    assert product.title == "Test Whey"
    assert product.sku == "ABC1"
    assert product.price == 29.90
