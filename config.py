class Config:
	url_base_for_get_chapter = "https://api.cdnlibs.org/api/manga/59249--tensei-shitara-slime-datta-ken-light-novel/chapter"
	#url_for_get_chapter = "https://api.cdnlibs.org/api/manga/59249--tensei-shitara-slime-datta-ken-light-novel/chapter?number=0.5&volume=1"
	file_name_for_chapter_id = "chapters_id.json"
	file_name_for_chapter_text = "chapters_text.json"
	character_name_to_search = "Вельгринд"


class Chapter:
	def __init__(self,name:str,volume:int,number:int):
		self.name = name
		self.volume = volume
		self.number = number