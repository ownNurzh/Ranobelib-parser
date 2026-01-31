import json

from bs4 import BeautifulSoup

from config import Config,Chapter

def get_json_text_from_file(file_name):
	with open(file_name, "r", encoding="utf-8") as f:
		result = json.load(f)
	return result

def get_chapters_id_from_file():
	result = []
	file_json = get_json_text_from_file(Config.file_name_for_chapter_id)
	chapters_id = file_json.get("data",{})

	for chapter in chapters_id:
		chapter_object = Chapter(chapter.get("name",""),chapter.get("volume",""),chapter.get("number",""))
		result.append(chapter_object)
	return result


def get_chapters_text_from_file():
	file_json = get_json_text_from_file(Config.file_name_for_chapter_text)
	return file_json

def html_content_to_dict(text:str):
	result = []
	soup = BeautifulSoup(text,"lxml")
	for p in soup.find_all("p"):
		paragraph_dict = {"type":"paragraph","content":{"type":"text","text":p.get_text()}}
		result.append(paragraph_dict)
	return result