user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests' : '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': user_agent
}

source_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests' : '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': user_agent,
    'referer' : 'https://www.acmicpc.net/',
    'sec-ch-ua' : '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile' : '?0',
    'sec-fetch-dest' : 'document',
    'sec-fetch-mode' : 'navigate',
    'sec-fetch-site' : 'same-origin',
    'sec-fetch-user' : '?1',
}