
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
        self.coverage = (self.total_number_scenarios_implemented*100.0)/(self.total_number_scenarios)

    def get_coverage(self):
        return "%.2f" % self.coverage