import sublime
import sublime_plugin
import random
import os
import re

plugin_package_path = os.getcwd()


def str_validation(content):
    return re.match(r"^lorem\( *\d* *,? *\d* *\)$", content, re.IGNORECASE)


def check_char(c):
    return c in ("loremLOREM(,)0123456789 ")


class LoremTextCommand(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view
        self.random_word_list = None
        self.pword1 = None
        self.pword2 = None
        self.csentence = []
        self.psentence = []

        self.fixed_word_list = None
        self.init_word_list()

        self.settings = None
        self.load_settings()

    def init_word_list(self):
        packages_path = sublime.packages_path()

        try:
            word_list_path = os.path.join(plugin_package_path, "wordlist/word_list_random.txt")
            f = open(word_list_path, "r")
            lines = f.readlines()
            words = []
            for line in lines:
                line = line.rstrip()
                words.append(line)
            self.random_word_list = words
            f.close()
        except IOError:
            # sublime.status_message("LoremText plugin could not load random word list")
            pass

        try:
            word_list_path = os.path.join(plugin_package_path, "wordlist/word_list_fixed.txt")
            f = open(word_list_path, "r")
            lines = f.readlines()
            words = []
            for line in lines:
                line = line.rstrip()
                words.append(line)
            self.fixed_word_list = words
            f.close()
        except IOError:
            # sublime.status_message("LoremText plugin could not load fixed word list")
            pass

    def load_settings(self):
        settings = sublime.load_settings("LoremText.sublime-settings")

        settings.clear_on_change("default_paragraph_count")
        settings.add_on_change("default_paragraph_count", self.load_settings)

        self.settings = settings

    def get_word(self):
        word = random.choice(self.random_word_list)
        return word

    def get_sentence_length(self):
        r = random.randint(1, 10)
        return r

    def get_punctuation(self):
        r = random.random()
        if (r > 0.72):
            return "."
        return ","

    def run(self, edit, word_count, paragraph_count, generate_random_text=True, start_with_lorem_ipsum=True):
        settings = self.settings

        generate_random_text_value = settings.get("generate_random_text")
        if (isinstance(generate_random_text_value, bool)):
            generate_random_text = generate_random_text_value

        if (generate_random_text and not self.random_word_list):
            self.view.set_status("LoremText", "LoremText plugin could not load random word list")
            return

        if (not generate_random_text and not self.fixed_word_list):
            self.view.set_status("LoremText", "LoremText plugin could not load fixed word list")
            return

        if (not isinstance(word_count, (int, long))):
            default_word_count = settings.get("default_word_count")
            if (isinstance(default_word_count, (int, long)) and default_word_count > 0):
                word_count = default_word_count
        if (not isinstance(paragraph_count, (int, long))):
            default_paragraph_count = settings.get("default_paragraph_count")
            if (isinstance(default_paragraph_count, (int, long)) and default_paragraph_count > 0):
                paragraph_count = default_paragraph_count

        always_start_with_lorem_ipsum = settings.get("always_start_with_lorem_ipsum")
        if (isinstance(always_start_with_lorem_ipsum, bool)):
            start_with_lorem_ipsum = always_start_with_lorem_ipsum

        self.check_regions()

        region_set = self.view.sel()
        for region in region_set:
            self.insert_lorem_text(edit, region, word_count, paragraph_count, generate_random_text, start_with_lorem_ipsum)

        self.optimize_view()

    def check_regions(self):
        new_regions = []

        region_set = self.view.sel()
        for region in region_set:
            begin = region.begin()
            end = region.end()
            size = self.view.size()

            region_valid = False
            new_region = None

            region_content = self.view.substr(region).lower()
            if (str_validation(region_content)):
                region_valid = True
            else:
                get_l = False
                get_cb = False
                cb = region_content.find(")")
                l = region_content.find("l")
                length = len(region_content)

                if ((length > 0 and re.search(r"[^loremLOREM0-9() ,]", region_content)) or
                    (cb != -1 and cb != length - 1) or
                    (l != -1 and l != 0)):
                    pass
                else:
                    if (length == 0):
                        end -= 1

                    if (l == -1):
                        begin -= 1
                        while (begin >= 0):
                            c = self.view.substr(begin)
                            if (check_char(c)):
                                if (c == "l" or c == "L"):
                                    get_l = True
                                    break
                            else:
                                break
                            begin -= 1
                    else:
                        get_l = True

                    if (get_l):
                        if (cb == -1):
                            while (end < size):
                                c = self.view.substr(end)
                                end += 1
                                if (check_char(c)):
                                    if (c == ")"):
                                        get_cb = True
                                        break
                                else:
                                    break
                            pass
                        else:
                            get_cb = True

                region_valid = get_l and get_cb
                if (region_valid):
                    new_region = sublime.Region(begin, end)
                    if(str_validation(self.view.substr(new_region))):
                        new_regions.append(new_region)

        for r in new_regions:
            # don't worry, repeat regions will not be duplicated,
            # and new region will be merged with the old regions
            region_set.add(r)

    def insert_lorem_text(self, edit, region, word_count, paragraph_count, generate_random_text, start_with_lorem_ipsum):
        region_content = self.view.substr(region)
        if (str_validation(region_content)):
            region_content = region_content.lower()
            region_content = re.sub(r"[lorem() ]", "", region_content)
            counts = region_content.split(",")
            if (counts[0].isdigit()):
                word_count = int(counts[0])
            if (len(counts) > 1 and counts[1].isdigit()):
                paragraph_count = int(counts[1])

        result = None
        if (generate_random_text):
            result = self.random_lorem_text(word_count, paragraph_count, start_with_lorem_ipsum)
        else:
            result = self.fixed_lorem_text(word_count, paragraph_count)
        self.view.replace(edit, region, result)

    def random_lorem_text(self, word_count, paragraph_count, start_with_lorem_ipsum):
        result = []
        for j in range(1, paragraph_count + 1):
            rc = word_count
            if (j == 1 and start_with_lorem_ipsum):
                lorem = ("Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipisicing", "elit")
                if (word_count <= 5):
                    for k in range(0, word_count):
                        result.append(lorem[k])
                        if (k < word_count - 1):
                            result.append(" ")
                        else:
                            result.append(".")
                    continue
                else:
                    for k in range(0, 5):
                        result.append(lorem[k])
                        if (k < 4):
                            result.append(" ")
                        else:
                            result.append(", ")

                    rmax = min(8, word_count)
                    for k in range(5, rmax):
                        result.append(lorem[k])
                        if (k < rmax - 1):
                            result.append(" ")
                        else:
                            result.append(".")

                    if (word_count > 8):
                        result.append(" ")
                        rc = word_count - 8
                    else:
                        continue

            sentence_length = self.get_sentence_length()
            plength = 0
            punctuation = self.get_punctuation()
            cap = True
            for i in range(1, rc + 1):
                word = self.get_word()
                if (cap):
                    word = word.capitalize()
                    cap = False
                plength += 1
                result.append(word)
                if (i == rc):
                    result.append(".")
                    break
                if (plength == sentence_length):
                    result.append(punctuation)
                    if (punctuation == "."):
                        cap = True
                    sentence_length = self.get_sentence_length()
                    plength = 0
                    punctuation = self.get_punctuation()
                result.append(" ")

            if (j < paragraph_count):
                result.append("\n")
        return "".join(result)

    def fixed_lorem_text(self, word_count, paragraph_count):
        length = len(self.fixed_word_list)
        c = 0
        result = []
        for j in range(1, paragraph_count + 1):
            i = 1
            while (i <= word_count):
                w = self.fixed_word_list[c]
                c += 1
                if (c == length):
                    c = 0

                if (i == 1 and (w == "," or w == ".")):
                    continue
                if (i == 1):
                    w = w.capitalize()
                elif (i > 1 and w != "," and w != "."):
                    result.append(" ")

                result.append(w)
                if (i == word_count and w != "," and w != "."):
                    result.append(".")
                if (w != "," and w != "."):
                    i += 1

            if (j < paragraph_count):
                result.append("\n")
        return "".join(result)

    def optimize_view(self):
        new_regions = []
        region_set = self.view.sel()
        for region in region_set:
            new_regions.append(sublime.Region(region.end(), region.end()))
        region_set.clear()
        for r in new_regions:
            region_set.add(r)
        if (len(new_regions) > 0):
            self.view.show(new_regions[0])
