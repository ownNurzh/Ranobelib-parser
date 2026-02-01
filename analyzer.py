from util import get_chapters_text_from_file
from config import Config
class Analyzer:
	def __init__(self,chapters_dict):
		self.chapters = chapters_dict
	def print_volume_count_and_chapters_length(self):
		array_for_sum = []
		for volume_id,volume_chapters in self.chapters.items():
			array_for_sum.append(len(volume_chapters))
		length_volumes = len(array_for_sum)
		summ_chapters = sum(array_for_sum)
		chapter_avg = summ_chapters / length_volumes
		print(f"Количество томов {length_volumes}")
		print(f"Сумма всех глав {summ_chapters}")
		print(f"Авг глава за том {chapter_avg:.0f}")
	def search_text(self,goal_text:str):
		result = {}
		for volume_id,volume_chapters in self.chapters.items():
			for chapter_id , chapter_data in volume_chapters.items():
				chapter_name = chapter_data.get("name")
				chapter_content = chapter_data.get("content")
				for key,p in enumerate(chapter_content):
					p_type = p.get("type")
					p_content = p.get("content")
					if p_type and p_type == "paragraph" and p_content:
						object_for_calc_count_words = p_content if not isinstance(p_content,list) else p_content[0]
						text = object_for_calc_count_words.get("text","")
						if goal_text in text:
							print(f"{chapter_name} Том {volume_id} глава {chapter_id} параграф {key + 1}")
							return 
		print("Не найден")



	def print_count_paragraphs_and_count_words(self):
		result = {}
		for volume_id,volume_chapters in self.chapters.items():
			for chapter_id , chapter_data in volume_chapters.items():
				chapter_name = chapter_data.get("name")
				chapter_content = chapter_data.get("content")
				if not result.get(chapter_name):
					result[chapter_name] = {"count_p":0,"count_image":0,"count_word":0,"count_rimuru":0,"volume":volume_id,"chapter":chapter_id}
				
				for p in chapter_content:
					p_type = p.get("type")
					if p_type:
						if p_type == "image":
							result[chapter_name]["count_image"] += 1
						else:
							result[chapter_name]["count_p"] += 1

							p_content = p.get("content")
							if p_content:
								object_for_calc_count_words = p_content if not isinstance(p_content,list) else p_content[0]
								text = object_for_calc_count_words.get("text","")
								result[chapter_name]["count_word"] += len(text.split())
								if Config.character_name_to_search in text:
									result[chapter_name]["count_rimuru"] += 1


		paragraph = {"name_min":None,"name_max":None}
		words = {"name_min":None,"name_max":None}
		rimuru_word = {"name_min":None,"name_max":None}
		summ_word = []
		summ_p = []
		summ_rimuru= []
		for name,info in result.items():
			summ_word.append(info.get("count_word"))
			summ_p.append(info.get("count_p"))
			summ_rimuru.append(info.get("count_rimuru"))
			if not paragraph.get("min") and not paragraph.get("max"):
				paragraph["min"] = info.get("count_p")
				paragraph["max"] = info.get("count_p")
				paragraph["name_min"] = name
				paragraph["name_max"] = name
			if paragraph["min"] > info.get("count_p") and info.get("count_p") > 0:
				paragraph["min"] = info.get("count_p")
				paragraph["name_min"] = name
			if paragraph["max"] < info.get("count_p"):
				paragraph["max"] = info.get("count_p")
				paragraph["name_max"] = name

			if not words.get("min") and not words.get("max"):
				words["min"] = info.get("count_word")
				words["max"] = info.get("count_word")
				words["name_min"] = name
				words["name_max"] = name
			if words["min"] > info.get("count_word") and info.get("count_word") > 0:
				words["min"] = info.get("count_word")
				words["name_min"] = name
			if words["max"] < info.get("count_word"):
				words["max"] = info.get("count_word")
				words["name_max"] = name

			if not rimuru_word.get("min") and not rimuru_word.get("max"):
				rimuru_word["min"] = info.get("count_rimuru")
				rimuru_word["max"] = info.get("count_rimuru")
				rimuru_word["name_min"] = name
				rimuru_word["name_max"] = name
			if rimuru_word["min"] > info.get("count_rimuru") and info.get("count_rimuru") > 0:
				rimuru_word["min"] = info.get("count_rimuru")
				rimuru_word["name_min"] = name
			if rimuru_word["max"] < info.get("count_rimuru"):
				rimuru_word["max"] = info.get("count_rimuru")
				rimuru_word["name_max"] = name

			print(f"Название главы <{name}> , Кол. параграфов - {info.get("count_p")} , Кол. изображений - {info.get("count_image")},Кол слов - {info.get("count_word")},Кол упоминание Римуру - {info.get("count_rimuru")}")
		print(f"Глава с минимальным кол. параграфа {result[words["name_max"]]["volume"]} том {result[paragraph["name_max"]]["chapter"]} глава <{paragraph["name_min"]}> c {paragraph["min"]}")
		print(f"Глава с максимальным кол. параграфа {result[words["name_max"]]["volume"]} том {result[paragraph["name_max"]]["chapter"]} глава <{paragraph["name_max"]}> c {paragraph["max"]}")
		print(f"Глава с минимальным кол. слов {result[words["name_max"]]["volume"]} том {result[words["name_max"]]["chapter"]} глава <{words["name_min"]}> c {words["min"]}")
		print(f"Глава с максимальным кол. слов {result[words["name_max"]]["volume"]} том {result[words["name_max"]]["chapter"]} глава <{words["name_max"]}> c {words["max"]}")
		print(f"Глава с минимальным кол. упоминании Римуру {result[rimuru_word["name_max"]]["volume"]} том {result[rimuru_word["name_max"]]["chapter"]} глава <{rimuru_word["name_min"]}> c {rimuru_word["min"]}")
		print(f"Глава с максимальным кол. упоминании Римуру {result[rimuru_word["name_max"]]["volume"]} том {result[rimuru_word["name_max"]]["chapter"]} глава <{rimuru_word["name_max"]}> c {rimuru_word["max"]}")
		print(f"Сумма всех слов {sum(summ_word)}")
		print(f"Сумма всех параграфов {sum(summ_p)}")
		print(f"Сумма всех упоминаний {Config.character_name_to_search} {sum(summ_rimuru)}")




		
		
		
