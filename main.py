# -*- coding: utf-8 -*-

import yaml
from platform.general_datas_class import GeneralDatas 
config_file = open('config.yml')

parameters = yaml.load(config_file)
path_to_features_folder = parameters.get('path_to_features')
platforms = parameters.get('platforms')

pageGeneralDatas = GeneralDatas(path_to_features_folder, platforms)
pageGeneralDatas.set_functional_datas_of_project()
for feature in pageGeneralDatas.array_features:
    print "FEATURE"
    print feature.feature_name
    print feature.get_total_number_scenarios_implemented()
    print feature.get_total_number_scenarios()
    print "SCEN .. IMPLEMENTED"
    for scenario in feature.array_scenarios_implemented:
        print scenario
    print "SCEN .. NOT IMPLEMENTED"
    for scenario in feature.array_scenarios_not_implemented:
        print scenario
    print feature.get_coverage()
print "PROJECT"
print pageGeneralDatas.project_functional_coverage
print pageGeneralDatas.total_scenarios_of_project