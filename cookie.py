import browser_cookie3

def get_cookie():
	cookies = browser_cookie3.chrome(domain_name=".acmicpc.net")
	cookie_str = ""
	for cookie in cookies:
			cookie_str += cookie.name + "=" + cookie.value + "; "
	cookie_str += ' _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1;'
	return cookie_str

	