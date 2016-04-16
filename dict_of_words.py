#!/usr/bin/python
import re


class WordCounter(object):

    def __init__(self, file_path):
        self.__word_counts = {}
        self.__reg_exp_list = []
        self.__mail = open(file_path)
        self.create_reg_exps()
        self.count_all_expressions()
        self.count_capital_leters()

    def __count_word(self, reg_exp):
        words = re.findall(reg_exp, self.__mail.read().lower())
        self.__word_counts[reg_exp] = len(words)

    def __count_all_expressions(self):
        for expression in self.__reg_exp_list:
            self.__count_word(expression)

    def __count_capital_leters(self):
        self.__reg_exp_list["CapitalLetters"] = sum(1 for c in self.__mail.read() if c.isupper())

    def __create_reg_exps(self):
        self.__reg_exp_list.append(re.compile('data', re.I))
        self.__reg_exp_list.append(re.compile('\d\d\d', re.I))
        self.__reg_exp_list.append(re.compile('technolog', re.I))
        self.__reg_exp_list.append(re.compile('technique', re.I))
        self.__reg_exp_list.append(re.compile('technic', re.I))
        self.__reg_exp_list.append(re.compile('[1-2]\d\d\d', re.I))
        self.__reg_exp_list.append(re.compile('part', re.I))
        self.__reg_exp_list.append(re.compile('[a,p]m', re.I))
        self.__reg_exp_list.append(re.compile('cs', re.I))
        self.__reg_exp_list.append(re.compile('direct', re.I))
        self.__reg_exp_list.append(re.compile('meeting', re.I))
        self.__reg_exp_list.append(re.compile('or[i,y]ginal', re.I))
        self.__reg_exp_list.append(re.compile('project', re.I))
        self.__reg_exp_list.append(re.compile('re', re.I))
        self.__reg_exp_list.append(re.compile('edu', re.I))
        self.__reg_exp_list.append(re.compile('table', re.I))
        self.__reg_exp_list.append(re.compile('conference', re.I))
        self.__reg_exp_list.append(re.compile('sale', re.I))
        self.__reg_exp_list.append(re.compile('award', re.I))
        self.__reg_exp_list.append(re.compile('winner', re.I))
        self.__reg_exp_list.append(re.compile('lucky', re.I))
        self.__reg_exp_list.append(re.compile('$', re.I))
        self.__reg_exp_list.append(re.compile('#', re.I))

    def get_word_counts(self):
        return self.__word_counts


if __name__ == "__main__":
    pass
