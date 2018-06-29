
class FunctionalDatas: 

    def __init__(self, feature_name, array_scenarios_implemented, array_scenarios_not_implemented):
        self.feature_name = feature_name
        self.array_scenarios_implemented = array_scenarios_implemented
        self.array_scenarios_not_implemented = array_scenarios_not_implemented
        self.total_number_scenarios_implemented = 0
        self.total_number_scenarios_not_implemented = 0
        self.total_number_scenarios = 0
        self.coverage = 0

    def set_total_number_scenarios_implemented(self):
        self.total_number_scenarios_implemented = len(self.array_scenarios_implemented)
    
    def set_total_number_scenarios_not_implemented(self):
        self.total_number_scenarios_not_implemented = len(self.array_scenarios_not_implemented)
    
    def get_total_number_scenarios_implemented(self):
        return self.total_number_scenarios_implemented
    
    def get_total_number_scenarios_not_implemented(self):
        return self.total_number_scenarios_not_implemented

    def set_total_number_scenarios(self):
        self.total_number_scenarios =  self.total_number_scenarios_implemented + self.total_number_scenarios_not_implemented
    
    def get_total_number_scenarios(self):
        return self.total_number_scenarios

    def set_coverage(self):
        if self.total_number_scenarios > 0:
            self.coverage = (self.total_number_scenarios_implemented*100.0)/(self.total_number_scenarios)
        else:
            print "\033[33mThis feature: \033[4m" + self.feature_name + "\033[0m\033[33m has not test scenarios.\nSo it is not possible to generate any metric about this feature!!\033[m"

    def get_coverage(self):
        return "%.2f" % self.coverage