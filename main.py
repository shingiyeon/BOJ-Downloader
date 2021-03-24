import browser_cookie3
import urllib
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS
from abc import *
import http.client
import sys
import json
import time
import random
from cookie import get_cookie
from file_type import file_type
from header import header, source_header

def get_response(url, query=None, header=None):
    data = None
    req = Request(url+query, data, header)
    try:
        response = urlopen(req)
        return response
    except urllib.error.HTTPError:
        print(urllib.error.HTTPError)
        sys.exit(1)

def make_remark(title_name, writer, time_stamp, solution_id, language) :
    remark = "//# Author : " + writer + " " + "=" * (34-len(writer)) + "#\n"
    remark += "//# Solution : " + solution_id + " " + "=" * (32-len(solution_id)) + "#\n"
    remark += "//# Time Stamp : " + time_stamp + " " + "=" * (30-len(time_stamp)) + "#\n"
    remark += "//# Problem Title : " + title_name + " " + "=" * (23-len(title_name)) + "#\n"
    remark += "//# Language : " + language + " " + "=" * (32-len(language)) + "#\n\n"
    return remark

def analysis_info(tds):
    solution_id = tds[0].text.strip()
    user_id = tds[1].find('span', {'class': 'user-cyan'}).text.strip()
    title_id = tds[2].text.strip()
    title_name = tds[2].find('a').get('title')
    result = tds[3].text.strip()
    language = tds[6].text.strip().split("/")[0][:-1]
    time_stamp = tds[-1].find('a').get('title')

    return solution_id, user_id, title_id, title_name, result, language, time_stamp

def download_data(user_id, code_path, code_list_path):
	ret = get_response("https://acmicpc.net/status?", "user_id=" + user_id, header)
	res = BS(ret, 'html.parser')
	ret.close()

	try:
		with open(code_list_path, "r", encoding="utf-8") as f:
			title_map = json.load(f)
	except:
		print(code_list_path + "를 읽어오는 중 에러가 발생했습니다. 파일이 있는지 확인해주십시오.")
		sys.exit(1)
	
	while res.find('a', {'id': 'next_page'}) != None:
		next_page = res.find('a', {'id' : 'next_page'}).get('href')
		trs = res.find_all('tr')

		for idx, tr in enumerate(trs):
			id = tr.get('id')
			if id == None:
					continue
			tds = tr.find_all('td')

			solution_id, user_id, title_id, title_name, result, language, time_stamp = analysis_info(tds)   
			if result != "맞았습니다!!":
					continue

			if title_id in title_map:
					if solution_id in title_map[title_id]:
							continue
					else:
							file_name = title_id + "_" + str(len(title_map[title_id]))
							title_map[title_id].append(solution_id)
			else:
					file_name = title_id
					title_map[title_id] = [solution_id]
			file_name += file_type[language]

			remark = make_remark(title_name, user_id, time_stamp, solution_id, language)

			source_ret = get_response("https://acmicpc.net/source/" , solution_id, header=source_header)
			source_res = BS(source_ret, 'html.parser')

			source_ret.close()
			code = source_res.find('textarea').text.strip()

			try:
				with open(code_path + file_name, "w", encoding="utf-8") as f:
						f.write(remark + code)
			except:
				print(code_path + "가 존재하지 않거나 파일이 열려있는 상태입니다.")
				sys.exit(1)

			time.sleep(random.uniform(2,4))

	ret = get_response("https://acmicpc.net", next_page, header)
	res = BS(ret, 'html.parser')
	ret.close()

	try:
		with open(code_list_path, "w", encoding="utf-8") as f:
			json.dump(title_map, f)
	except:
		print(code_list_path + "를 다시 작성중 오류가 발생했습니다.")
		sys.exit(1)

if __name__ == "__main__":
	with open("./personal_info.json", "r", encoding="utf-8") as f:
		personal_data = json.load(f)

	user_id = personal_data["id"]

	if user_id == "":
		print(user_id + "가 비어있습니다.")
		sys.exit(1)
  

	cookie = get_cookie()
	source_header["cookie"] = cookie

	code_path = personal_data["code_path"]
	code_list_path = personal_data["code_list_path"]

	download_data(user_id, code_path, code_list_path)

	


