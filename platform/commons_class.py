# -*- coding: utf-8 -*-

import os

class Commons:

    def check_path_to_feature_folder(self, path):
        if path is None:
            print '\033[91m' + "Please, set correct tag for path to features in " + "\033[4mconfig.yml\033[0m" + '\033[0m'
            exit(1)
        if not os.path.isdir(path):
            print "\033[31;1mDo not exist any folder: " + path + " \nPlease, set correct folder in " + "\033[4mconfig.yml\033[0m" + "\033[m"
            exit(1)

    def check_path_to_feature_file(self, path):
        if not os.path.isfile(path):
            print "\033[31;1mThis file: \n" + path + " do not exist. \nPlease check this path!\033[m"
            exit(1)
        
