
from config import Config
from util import get_chapters_id_from_file,get_chapters_text_from_file
from init_chapters_text import InitChaptersText
from analyzer import Analyzer

chapters_list = get_chapters_id_from_file()

#initer_text = InitChaptersText(Config.url_base_for_get_chapter)
#initer_text.save(chapters_list)

analyzer_object = Analyzer(get_chapters_text_from_file())

#analyzer_object.print_volume_count_and_chapters_length()
analyzer_object.print_count_paragraphs_and_count_words()


text = "Он понимал насколько силен Рудра, но не предполагал, что тот сможет победить его теперь, когда была Стража Замка."
analyzer_object.search_text(text)