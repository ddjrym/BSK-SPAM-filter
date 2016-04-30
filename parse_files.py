from dict_of_words import WordCounter
import os
import csv
import sys


class DataCreator(object):

    def __init__(self, directory):
        self.__directory = directory
        self.paths = []
        self.parse_files_list = []
        self.__get_files_paths()
        self.__parse_file()
        self.__create_csv()

    def __get_files_paths(self):
        [self.paths.append(self.__directory + "\\" + path) for path in os.listdir(self.__directory)]

    def __parse_file(self):
        [self.parse_files_list.append(WordCounter(mail).get_word_counts()) for mail in self.paths]

    def write_data_to_csv(self, w):
        for parsed_mail in self.parse_files_list:
            w.writerow(parsed_mail.values())

    def __create_csv(self):
        with open(self.__directory + ".csv", "a+") as infile:
            w = csv.writer(infile)
            self.write_data_to_csv(w)


def main():
    DataCreator(sys.argv[1])


main()
