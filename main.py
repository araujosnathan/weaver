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


datas = {} 
datas['total_endpoints_tested'] = ""
datas['contract_test_coverage'] = ""
datas['total_scenarios'] = ""
datas['functional_coverage'] = ""
datas['features'] = []


datas['functional_coverage'] = (pageGeneralDatas.get_functional_coverage_projetc())
datas['total_scenarios'] = (pageGeneralDatas.total_scenarios_of_project)
datas['contract_test_coverage'] = (pageGeneralDatas.get_project_contract_coverage())
datas['total_endpoints_tested'] = (pageGeneralDatas.get_total_number_endpoints_tested())

for feature in pageGeneralDatas.array_features:
    datas['features'].append({
        'feature_name': feature.feature_name,
        'number_scenarios_implemented': feature.get_total_number_scenarios_implemented(),
        'total_number_scenarios': feature.get_total_number_scenarios(),
        'scenarios_implemented': map(str,feature.array_scenarios_implemented),
        'scenarios_not_implemented': feature.array_scenarios_not_implemented,
        'coverage': feature.get_coverage()
    })

datas =  json.dumps(datas, ensure_ascii=False)
with open('generalDatas.json', 'w') as outfile: 
    outfile.write("data = '" +  str(datas) + "'")
