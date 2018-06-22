# -*- coding: utf-8 -*-

import yaml
import json
from platform.general_datas_class import GeneralDatas 
config_file = open('config.yml')

parameters = yaml.load(config_file)
path_to_features_folder = parameters.get('path_to_features')
path_to_contract_tests_folder = parameters.get('path_to_contract_tests')
total_endpoints_used = parameters.get('total_endpoints_used')
platforms = parameters.get('platforms')

pageGeneralDatas = GeneralDatas(path_to_features_folder, path_to_contract_tests_folder, total_endpoints_used, platforms)
pageGeneralDatas.set_functional_datas_of_project()

# print "HEAD"
# print pageGeneralDatas.project_functional_coverage
# print pageGeneralDatas.total_scenarios_of_project
# print pageGeneralDatas.project_contract_coverage()
# print pageGeneralDatas.get_total_number_endpoints_tested()

datas = {} 



datas['total_endpoints_tested'] = ""
datas['contract_test_coverage'] = ""
datas['total_scenarios'] = ""
datas['functional_coverage'] = ""
datas['features'] = []


datas['functional_coverage'] = (pageGeneralDatas.project_functional_coverage)
datas['total_scenarios'] = (pageGeneralDatas.total_scenarios_of_project)
datas['contract_test_coverage'] = (pageGeneralDatas.project_contract_coverage())
datas['total_endpoints_tested'] = (pageGeneralDatas.get_total_number_endpoints_tested())


# # print "FEATURES"
for feature in pageGeneralDatas.array_features:
    datas['features'].append({
        'feature_name': feature.feature_name,
        'number_scenarios_implemented': feature.get_total_number_scenarios_implemented(),
        'total_number_scenarios': feature.get_total_number_scenarios(),
        'scenarios_implemented': map(str,feature.array_scenarios_implemented),
        'scenarios_not_implemented': feature.array_scenarios_not_implemented,
        'coverage': feature.get_coverage()
    })
    # print feature.feature_name
    # print feature.get_total_number_scenarios_implemented()
    # print feature.get_total_number_scenarios()
    # print "IMPLEMENTED"
    # for scenario in feature.array_scenarios_implemented:
    #     print scenario
    # print "NOT IMPLEMENTED"
    # for scenario in feature.array_scenarios_not_implemented:
    #     print scenario
    # print feature.get_coverage()
with open('generalDatas.json', 'w') as outfile:  
    json.dump(datas, outfile)
