import requests
import time
import json
from typing import List

from config import Chapter,Config
from util import html_content_to_dict
class InitChaptersText():
	def __init__(self,url_base:str):
		self.url_base = url_base
	def save(self,chapters_list:List[Chapter]):
		result = {}
		length = len(chapters_list)
		for key,chapter in enumerate(chapters_list):
			print(f"Saving chapter name {chapter.name} ")
			volume = chapter.volume
			number = chapter.number
			new_params = {
				"number":number,
				"volume":volume
			}
			headers = {
				"Accept": "application/json", 
				"Content-Type": "application/json", 
				"User-Agent": "Mozilla/5.0"
			}
			if not result.get(volume):
				result[volume] = {}
			if not result.get(volume,{}).get(number):
				result[volume][number] = {"name":chapter.name,"content":[]}
			response = requests.get(self.url_base,params=new_params,headers=headers)
			if response.status_code == 200:
				response_text = response.json()
				paragraphs = response_text.get("data",{}).get("content",{})
				if not isinstance(paragraphs,dict):
					paragraphs = {"content":html_content_to_dict(paragraphs)}
					print("Translated html->dict succes!")
				paragraphs = paragraphs.get("content")
				result[volume][number]["content"] = paragraphs
				print(f"Current {key} , Max {length}")
				time.sleep(3.5)
			else:
				print(f"HTTP status code - {response.status_code}")
		self._save_file(result)
	def _save_file(self,array:dict):
		with open(Config.file_name_for_chapter_text, "w", encoding="utf-8") as f:
			json.dump(array, f, ensure_ascii=False, indent=4)
