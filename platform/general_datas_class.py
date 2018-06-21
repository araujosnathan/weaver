# -*- coding: utf-8 -*-

import os, fnmatch, re
from functional_datas_class import FunctionalDatas

class GeneralDatas:
    path_to_features_folder = ""
    platform = ""
    total_scenarios_implemented_of_project = 0
    total_scenarios_of_project = 0
    project_functional_coverage = 0
    array_features = []

    def __init__(self, path_to_features_folder, platform):
        self.path_to_features_folder = path_to_features_folder
        self.platform = platform

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
                feature_name = line.split(':')[1]
        return feature_name

    def get_scenario_names_implemented_by_feature(self, path_to_feature_file):
        array_scenario_names_implemented = []
        with open(path_to_feature_file) as feature_file:
            for line in feature_file:
                if any(re.findall(r"%s" % self.platform, line)):
                    array_scenario_names_implemented.append(next(feature_file).split(':')[1])
        return array_scenario_names_implemented

    def get_scenario_names_by_feature(self, path_to_feature_file):
        array_scenario_names = []
        feature_file = open(path_to_feature_file, 'r')
        array_matches = ['Cenário','Cenario','Scenario']
        for line in feature_file.readlines():
            if any(re.findall(r"(?=("+'|'.join(array_matches)+r"))", line)):
                array_scenario_names.append(line.split(':')[1])
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
                