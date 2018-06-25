# -*- coding: utf-8 -*-

import os

class Commons:

    def check_path_to_feature_folder(self, path):
        if path is None:
            print '\033[91m' + "Please, set correct tag for path to features in " + "\033[4mconfig.yml\033[0m" + '\033[0m'
            exit(1)
        if not os.path.isdir(path):
            print '\033[91m' + "Do not exist any folder: " + path + " \nPlease, set correct folder in " + "\033[4mconfig.yml\033[0m" + "\033[m"
            exit(1)

    def check_path_to_feature_file(self, path):
        if not os.path.isfile(path):
            print '\033[91m' + "This file: \n" + path + " do not exist. \nPlease check this path!\033[m"
            exit(1)
    
    def check_tag_to_contract_folder(self, path):
        if path is None:
            return False
        else:
            return True 
    
    def check_path_to_contract_folder(self, path):
        if not os.path.isdir(path):
            print '\033[91m' + "Do not exist any folder: " + path + " \nPlease, set correct folder to contract test in " + "\033[4mconfig.yml\033[0m" + "\033[m"
            exit(1)
    
    def check_path_to_contract_file(self, path):
        if not os.path.isfile(path):
            print '\033[91m' + "It was not found any file with " + "\033[4mname\033[0m\033[91m" +  ": \n" + path + "\nPlease set correct folder with contract tests or add " + "\033[4mtesting\033[0m\033[91m" +  " in all contract test file names!"+ '\033[0m'
            exit(1)

    def check_tag_to_unit_test_ios(self, path):
        if path is None:
            return False
        else:
            return True 

    def check_path_to_unit_test_ios(self, path):
        if not os.path.isfile(path):
            print '\033[91m' + "File not found: " + path +" \nPlease, set a correct path to unit test file in tag: "+ "\033[4mios_unit_test_report\033[m"
            exit(1)