# -*- coding: utf-8 -*-
import os, fnmatch, re
from functional_datas_class import FunctionalDatas

class GeneralDatas:
    path_to_features_folder = ""
    path_to_contract_tests_folder = ""
    platform = ""
    total_scenarios_implemented_of_project = 0
    total_scenarios_of_project = 0
    project_functional_coverage = 0
    total_endpoints_used = 0
    project_contract_coverage = 0
    total_number_of_endpoints = 0
    array_features = []
    array_endpoints = []

    def __init__(self, path_to_features_folder, path_to_contract_tests_folder, total_endpoints_used, platform):
        self.path_to_features_folder = path_to_features_folder
        self.path_to_contract_tests_folder = path_to_contract_tests_folder
        self.platform = platform
        self.total_endpoints_used = total_endpoints_used

    def get_features_from_project(self):
        list_of_feature_files = os.listdir(self.path_to_features_folder)
        file_pattern = "*.feature"
        array_features_file = []
        for file_in_dir in list_of_feature_files:  
            if fnmatch.fnmatch(file_in_dir, file_pattern):
                array_features_file.append(file_in_dir)
        return array_features_file

    def get_feature_name(self, path_to_feature_file):
        feature_file = open(path_to_feature_file, 'r')
        array_matches = ['Funcionalidade','Feature']
        for line in feature_file.readlines():
            if any(re.findall(r"(?=("+'|'.join(array_matches)+r"))", line)):
                feature_name = line.split(':')[1].strip()
        return feature_name

    def get_scenario_names_implemented_by_feature(self, path_to_feature_file):
        array_scenario_names_implemented = []
        with open(path_to_feature_file) as feature_file:
            for line in feature_file:
                if any(re.findall(r"%s" % self.platform, line)):
                    array_scenario_names_implemented.append(next(feature_file).split(':')[1].strip())
        return array_scenario_names_implemented

    def get_scenario_names_by_feature(self, path_to_feature_file):
        array_scenario_names = []
        feature_file = open(path_to_feature_file, 'r')
        array_matches = ['Cenário','Cenario','Scenario']
        for line in feature_file.readlines():
            if any(re.findall(r"(?=("+'|'.join(array_matches)+r"))", line)):
                array_scenario_names.append(line.split(':')[1].strip())
        return array_scenario_names

    def set_functional_data_by_feature(self):
        array_features = []
        for file in self.get_features_from_project():
            feature_name = self.get_feature_name(self.path_to_features_folder + file)
            scenario_implemented = self.get_scenario_names_implemented_by_feature(self.path_to_features_folder + file)
            scenario_not_implemented = list(set(self.get_scenario_names_by_feature(self.path_to_features_folder + file)) 
                                        - set(self.get_scenario_names_implemented_by_feature(self.path_to_features_folder + file)))
            feature = FunctionalDatas(feature_name, scenario_implemented, scenario_not_implemented)
            feature.set_total_number_scenarios_implemented()
            feature.set_total_number_scenarios_not_implemented()
            feature.set_total_number_scenarios()
            feature.set_coverage()
            self.array_features.append(feature)
    
    def set_functional_datas_of_project(self): 
        self.set_functional_data_by_feature()
        for feature in self.array_features:
            self.total_scenarios_implemented_of_project = self.total_scenarios_implemented_of_project + feature.get_total_number_scenarios_implemented()
            self.total_scenarios_of_project = self.total_scenarios_of_project + feature.get_total_number_scenarios()
        self.project_functional_coverage = (self.total_scenarios_implemented_of_project*100.0)/self.total_scenarios_of_project
    
    def get_contract_tests_from_project(self):
        list_of_contract_tests_files = os.listdir(self.path_to_contract_tests_folder)
        file_pattern = "*testing*"
        array_contract_tests_files = []
        for file_in_dir in list_of_contract_tests_files:  
            if fnmatch.fnmatch(file_in_dir, file_pattern):
                array_contract_tests_files.append(file_in_dir)
        return array_contract_tests_files

    def set_endpoints_from_file(self, path_to_contract_tests_file):
        contract_tests_file = open(path_to_contract_tests_file, 'r')
        for line in contract_tests_file.readlines():
            if any(re.findall(r"const PATH", line)):
                self.array_endpoints.append(line.split("=")[0])

    def remove_duplicates(self, array_duplicate):
        unique_endpoints = []
        for endpoint in array_duplicate:
            if endpoint not in unique_endpoints:
                unique_endpoints.append(endpoint)
        return unique_endpoints

    def remove_white_spaces(self, array):
        unique_endpoints = []
        for endpoint in array:
            unique_endpoints.append(endpoint.replace(' ', ''))
        return unique_endpoints

    def get_total_endpoints_from_project(self):
        for each_file in self.get_contract_tests_from_project():
            self.set_endpoints_from_file(self.path_to_contract_tests_folder + each_file)
        
        self.array_endpoints = self.remove_white_spaces(self.array_endpoints)
        self.array_endpoints = self.remove_duplicates(self.array_endpoints)
        return self.array_endpoints

    def get_total_number_endpoints_tested(self):
        self.total_number_of_endpoints = 0
        self.get_total_endpoints_from_project()
        self.total_number_of_endpoints = self.total_number_of_endpoints + len(self.array_endpoints)
        return self.total_number_of_endpoints

    def project_contract_coverage(self):
        self.project_contract_coverage = (self.get_total_number_endpoints_tested()*100.0)/self.total_endpoints_used
        return self.project_contract_coverage
    