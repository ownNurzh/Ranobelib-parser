import random

from config import Config
from util import get_chapters_id_from_file,get_chapters_text_from_file
from init_chapters_text import InitChaptersText
from analyzer import Analyzer

chapters_list = get_chapters_id_from_file()
chapters_text = get_chapters_text_from_file()
choice = random.choice(chapters_list)

random_chapter_paragraphs = chapters_text[choice.volume][choice.number].get("content")
idx = random.randrange(len(random_chapter_paragraphs))
random_paragraph = random_chapter_paragraphs[idx]
print(choice.name ,choice.volume,choice.number,idx,random_paragraph.get("content").get("text"))
#initer_text = InitChaptersText(Config.url_base_for_get_chapter)
#initer_text.save(chapters_list)

analyzer_object = Analyzer(chapters_text)

#analyzer_object.print_volume_count_and_chapters_length()
#analyzer_object.print_count_paragraphs_and_count_words()


text = "Мы вернулись примерно через час, следуя по проложенной нами тропе. Я воспользовался Мысленным Общением, чтобы предупредить Гельда, так что по прибытии нам приготовили еду. Трое моих спутников не могли выглядеть более смущенными."
analyzer_object.search_text(text)