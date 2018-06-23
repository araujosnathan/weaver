$(document).ready(function() {
        var generalDatas = JSON.parse(data);
        document.getElementById('FUNCTIONAL_PERCENTAGE').innerHTML = generalDatas.functional_coverage + "%";
        document.getElementById('FUNCTIONAL_SCENARIOS_NUMBER').innerHTML = generalDatas.total_scenarios;
        document.getElementById('CONTRACT_PERCENTAGE').innerHTML = generalDatas.contract_test_coverage + "%";
        document.getElementById('ENDPOINTS_NUMBER').innerHTML = generalDatas.total_endpoints_tested;
        for(var i = 0; i < generalDatas.features.length ; i++)
        {
            document.getElementById('ALL-FEATURES-AND-SCENARIOS').insertAdjacentHTML('beforeend', "<h4 id='PAINEL-SCENARIOS" + i + "' class='panel-title'>");
            document.getElementById('PAINEL-SCENARIOS' + i).insertAdjacentHTML('beforeend', "<a id='VIEW-COLLAPSE" + i + "' data-toggle='collapse' href='#collapse" + i +"'>");
            document.getElementById('VIEW-COLLAPSE' + i).insertAdjacentHTML('beforeend', "<p class='m-t-30 f-w-600'>" 
                                + generalDatas.features[i].feature_name 
                                + " (" + generalDatas.features[i].number_scenarios_implemented 
                                + "/" + generalDatas.features[i].total_number_scenarios 
                                + ") <span class='pull-right'>" + generalDatas.features[i].coverage + "%</span></p>");
            
            document.getElementById('VIEW-COLLAPSE' + i).insertAdjacentHTML('beforeend', "<div id='PROGRESS-SCENARIOS" + i +  "' class='progress'>");
            if(generalDatas.features[i].coverage >= 70 && generalDatas.features[i].coverage < 99){
                document.getElementById('PROGRESS-SCENARIOS' + i).innerHTML = "<div role='progressbar' style='width:" 
                                + generalDatas.features[i].coverage 
                                + "%; height:8px;' class='progress-bar bg-info wow animated progress-animated'> <span class='sr-only'>"
                                + generalDatas.features[i].coverage + "% Complete</span> </div>"
            }
            else if(generalDatas.features[i].coverage < 70){
                document.getElementById('PROGRESS-SCENARIOS' + i).innerHTML = "<div role='progressbar' style='width:" 
                                + generalDatas.features[i].coverage 
                                + "%; height:8px;' class='progress-bar bg-danger wow animated progress-animated'> <span class='sr-only'>"
                                + generalDatas.features[0].coverage + "% Complete</span> </div>"
            }
            else {
                document.getElementById('PROGRESS-SCENARIOS' + i).insertAdjacentHTML('beforeend', "<div role='progressbar' style='width:" 
                                + generalDatas.features[i].coverage 
                                + "%; height:8px;' class='progress-bar bg-success wow animated progress-animated'> <span class='sr-only'>"
                                + generalDatas.features[i].coverage + "% Complete</span> </div>");
            }
                
            document.getElementById('PROGRESS-SCENARIOS' + i).insertAdjacentHTML('beforeend', "</div>");
            document.getElementById('VIEW-COLLAPSE' + i).insertAdjacentHTML('beforeend', "</a>");
            
            document.getElementById('PAINEL-SCENARIOS' + i).insertAdjacentHTML('beforeend', "<div id='collapse" + i + "' class='panel-collapse collapse'>")
            var j = 0
            
            if(generalDatas.features[i].scenarios_implemented.length > 0){
                for(var j = 0; j < generalDatas.features[i].scenarios_implemented.length; j++){
                    document.getElementById('collapse' + i).insertAdjacentHTML('beforeend', "<div style='color:Green' class='panel'>" 
                                + generalDatas.features[i].scenarios_implemented[j] + "</div>")
                }
                
            }
            if(generalDatas.features[i].scenarios_not_implemented.length > 0)
            {
                for(var j = 0; j < generalDatas.features[i].scenarios_not_implemented.length; j++){
                    document.getElementById('collapse' + i).insertAdjacentHTML('beforeend', "<div style='color:lightCoral' class='panel'>" 
                                    + generalDatas.features[i].scenarios_not_implemented[j] +"</div>")
                }
            }
            
            document.getElementById('PAINEL-SCENARIOS' + i).insertAdjacentHTML('beforeend', "</div>");
            document.getElementById('PAINEL-SCENARIOS' + i).insertAdjacentHTML('beforeend', "</h4>");
        }
        
    }
)