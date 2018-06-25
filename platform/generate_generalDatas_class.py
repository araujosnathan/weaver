import json
import os

class GenerateGeneralDatas:
  
    def __init__(self, pageGeneralDatas, platform, report_name):
        self.pageGeneralDatas = pageGeneralDatas
        self.platform = platform
        self.report_name = report_name

    def set_dashboard_by_platform(self):
        self.pageGeneralDatas.set_functional_datas_of_project()
        datas = {} 
        datas['total_endpoints_tested'] = ""
        datas['contract_test_coverage'] = ""
        datas['total_scenarios'] = ""
        datas['functional_coverage'] = ""
        datas['features'] = []

        datas['platform'] = self.platform
        datas['functional_coverage'] = (self.pageGeneralDatas.get_functional_coverage_projetc())
        datas['total_scenarios'] = (self.pageGeneralDatas.total_scenarios_of_project)
        datas['contract_test_coverage'] = (self.pageGeneralDatas.get_project_contract_coverage())
        datas['total_endpoints_tested'] = (self.pageGeneralDatas.get_total_number_endpoints_tested())

        for feature in self.pageGeneralDatas.array_features:
            datas['features'].append({
                'feature_name': feature.feature_name,
                'number_scenarios_implemented': feature.get_total_number_scenarios_implemented(),
                'total_number_scenarios': feature.get_total_number_scenarios(),
                'scenarios_implemented': map(str,feature.array_scenarios_implemented),
                'scenarios_not_implemented': feature.array_scenarios_not_implemented,
                'coverage': feature.get_coverage()
            })
        return datas
    
    def set_sprint_metrics_dashbord_by_platform(self):
        sprint_historic = {}
        if not os.path.isfile("template/datas/sprintHistoric.json"):
            sprint_historic['metrics'] = []
            sprint_historic =  json.dumps(sprint_historic, ensure_ascii=False)
            with open('template/datas/sprintHistoric.json', 'w') as outfile: 
                outfile.write(sprint_historic)

        sprint_metric = {
            'report_name': self.report_name,
            'platform': self.platform,
            'unit_test_coverage': "N/A",
            'functional_coverage': self.pageGeneralDatas.get_functional_coverage_projetc(),
            'contract_coverage': self.pageGeneralDatas.get_project_contract_coverage(),
            'number_endpoints': self.pageGeneralDatas.get_total_number_endpoints_tested()
        }

        with open('template/datas/sprintHistoric.json') as json_data:
            new_metrics = json.load(json_data)
            
        new_metrics['metrics'].append(sprint_metric)
        new_metrics = json.dumps(new_metrics, ensure_ascii=False)

        with open('template/datas/sprintHistoric.json', 'w') as outfile: 
            outfile.write(new_metrics)
        with open('template/datas/sprintMetrics.json', 'w') as outfile:
            outfile.write("data_metrics = '" +  str(new_metrics) + "'")





