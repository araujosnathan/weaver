$(document).ready(function() {
    var dod_unit_test = 96;
    var dod_functional_test = 70;
    var dod_contract_test = 70;
    var fileName = location.href.split("/").slice(-1)[0]; 
    let keys = Object.keys(sprintsTableJSON).sort()
    
    var set_dashboard = function(key_plat, key){
        for(var i = 0; i < Object.keys(sprintsTableJSON[key].platforms).length; i ++){   
            if(key_plat.includes(Object.keys(sprintsTableJSON[key].platforms)[i])){
                document.getElementById('FUNCTIONAL_PERCENTAGE').innerHTML = sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].functional_coverage + "%";
                document.getElementById('FUNCTIONAL_SCENARIOS_NUMBER').innerHTML = sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].total_scenarios;
                if(sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].contract_test_coverage == "N/A"){
                    document.getElementById('CONTRACT_PERCENTAGE').innerHTML = sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].contract_test_coverage;
                }
                else{
                    document.getElementById('CONTRACT_PERCENTAGE').innerHTML = sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].contract_test_coverage + "%";
                }
                document.getElementById('ENDPOINTS_NUMBER').innerHTML = sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].total_endpoints_tested;
                
                document.getElementById('ALL-FEATURES-AND-SCENARIOS').innerHTML = ""
                for(var index_feature = 0; index_feature < sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features.length ; index_feature++)
                {
                    document.getElementById('ALL-FEATURES-AND-SCENARIOS').insertAdjacentHTML('beforeend', "<h4 id='PAINEL-SCENARIOS" + index_feature + "' class='panel-title'>");
                    document.getElementById('PAINEL-SCENARIOS' + index_feature).insertAdjacentHTML('beforeend', "<a id='VIEW-COLLAPSE" + index_feature + "' data-toggle='collapse' href='#collapse" + index_feature +"'>");
                    document.getElementById('VIEW-COLLAPSE' + index_feature).insertAdjacentHTML('beforeend', "<p class='m-t-30 f-w-600'>" 
                                        + sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].feature_name 
                                        + " (" + sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].number_scenarios_implemented 
                                        + "/" + sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].total_number_scenarios 
                                        + ") <span class='pull-right'>" + sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].coverage + "%</span></p>");
                    
                    document.getElementById('VIEW-COLLAPSE' + index_feature).insertAdjacentHTML('beforeend', "<div id='PROGRESS-SCENARIOS" + index_feature +  "' class='progress'>");
                    if(sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].coverage >= dod_functional_test && sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].coverage < 99){
                        document.getElementById('PROGRESS-SCENARIOS' + index_feature).innerHTML = "<div role='progressbar' style='width:" 
                                        + sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].coverage 
                                        + "%; height:8px;' class='progress-bar bg-info wow animated progress-animated'> <span class='sr-only'>"
                                        + sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].coverage + "% Complete</span> </div>"
                    }
                    else if(sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].coverage < dod_functional_test){
                        document.getElementById('PROGRESS-SCENARIOS' + index_feature).innerHTML = "<div role='progressbar' style='width:" 
                                        + sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].coverage 
                                        + "%; height:8px;' class='progress-bar bg-danger wow animated progress-animated'> <span class='sr-only'>"
                                        + sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].coverage + "% Complete</span> </div>"
                    }
                    else {
                        document.getElementById('PROGRESS-SCENARIOS' + index_feature).insertAdjacentHTML('beforeend', "<div role='progressbar' style='width:" 
                                        + sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].coverage 
                                        + "%; height:8px;' class='progress-bar bg-success wow animated progress-animated'> <span class='sr-only'>"
                                        + sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].coverage + "% Complete</span> </div>");
                    }
                        
                    document.getElementById('PROGRESS-SCENARIOS' + index_feature).insertAdjacentHTML('beforeend', "</div>");
                    document.getElementById('VIEW-COLLAPSE' + index_feature).insertAdjacentHTML('beforeend', "</a>");
                    
                    document.getElementById('PAINEL-SCENARIOS' + index_feature).insertAdjacentHTML('beforeend', "<div id='collapse" + index_feature + "' class='panel-collapse collapse'>")
                    
                    if("scenarios_implemented" in sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature]){

                        if(sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].scenarios_implemented.length > 0){
                            for(var j = 0; j < sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].scenarios_implemented.length; j++){
                                document.getElementById('collapse' + index_feature).insertAdjacentHTML('beforeend', "<div style='color:Green' class='panel'>" 
                                            + sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].scenarios_implemented[j] + "</div>")
                            }
                            
                        }
                    }

                    if("scenarios_not_implemented" in sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature]){
                        if(sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].scenarios_not_implemented.length > 0)
                        {
                            for(var j = 0; j < sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].scenarios_not_implemented.length; j++){
                                document.getElementById('collapse' + index_feature).insertAdjacentHTML('beforeend', "<div style='color:lightCoral' class='panel'>" 
                                            + sprintsTableJSON[key].platforms[Object.keys(sprintsTableJSON[key].platforms)[i]].features[index_feature].scenarios_not_implemented[j] +"</div>")
                            }
                        }
                    }
                    
                    document.getElementById('PAINEL-SCENARIOS' + index_feature).insertAdjacentHTML('beforeend', "</div>");
                    document.getElementById('PAINEL-SCENARIOS' + index_feature).insertAdjacentHTML('beforeend', "</h4>");

                }
            }
        }

    }

    var set_name = function(){
        document.getElementById('REPORT_PLATFORM_NAME').innerHTML = ""
        var key = this.id.split(":")[1];
        for(var i = 0; i < Object.keys(sprintsTableJSON[key].platforms).length; i ++){
            document.getElementById('REPORT_PLATFORM_NAME').insertAdjacentHTML('beforeend', "<li><a id='menu-"+ Object.keys(sprintsTableJSON[key].platforms)[i] +"' href='javascript:void(0)'>"+ Object.keys(sprintsTableJSON[key].platforms)[i] +"</a></li>")
            document.getElementById('menu-' + Object.keys(sprintsTableJSON[key].platforms)[i]).addEventListener("click", function () {
                set_dashboard(this.id, key);
            }, false);
        }
    
    }

    for(var i = 0; i < keys.length; i++)
    {
        document.getElementById("name:" + keys[i]).onclick = set_name
        document.getElementById("img:" + keys[i]).onclick = set_name
    }
    
    //         var sprintMetricDatas = JSON.parse(data_metrics);
    //         for(var index_sprint = sprintMetricDatas.metrics.length - 1; index_sprint >= 0; index_sprint--){
    //             if(sprintMetricDatas.metrics[index_sprint].platform == generalDatas.platforms[i].platform){
    //                 document.getElementById('TABLE-SPRINT-METRICS').insertAdjacentHTML('beforeend', "<tr id='COLUMNS-SPRINT-METRICS" + index_sprint + "'>");
    //                 document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td> <div class='round-img'> <a href=''> <img src='images/report_scrum.png' alt=''> </a> </div> </td>");
    //                 document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td>" + sprintMetricDatas.metrics[index_sprint].report_name + "</td>");
    //                 if(sprintMetricDatas.metrics[index_sprint].unit_test_coverage == "N/A"){
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-warning'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].unit_test_coverage + "</span></td>");
    //                 }
    //                 else if(sprintMetricDatas.metrics[index_sprint].unit_test_coverage >= dod_unit_test && sprintMetricDatas.metrics[index_sprint].unit_test_coverage < 100)
    //                 {
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-info'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].unit_test_coverage + "%</span></td>");
                                            
    //                 }
    //                 else if(sprintMetricDatas.metrics[index_sprint].unit_test_coverage < dod_unit_test){
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-danger'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].unit_test_coverage + "%</span></td>");
    //                 }
    //                 else{
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-success'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].unit_test_coverage + "%</span></td>");
    //                 }
            
    //                 if(sprintMetricDatas.metrics[index_sprint].functional_coverage >= dod_functional_test && sprintMetricDatas.metrics[0].functional_coverage < 100)
    //                 {
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-info'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].functional_coverage + "%</span></td>");
                                            
    //                 }
    //                 else if(sprintMetricDatas.metrics[index_sprint].functional_coverage < dod_functional_test){
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-danger'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].functional_coverage + "%</span></td>");
    //                 }
    //                 else{
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-success'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].functional_coverage + "%</span></td>");
    //                 }
                    
    //                 if(sprintMetricDatas.metrics[index_sprint].contract_coverage == "N/A"){
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-warning'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].contract_coverage + "</span></td>");
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-warning'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].number_endpoints + "</span></td>");
    //                 }
    //                 else if(sprintMetricDatas.metrics[index_sprint].contract_coverage >= dod_contract_test && sprintMetricDatas.metrics[index_sprint].contract_coverage < 100)
    //                 {
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-info'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].contract_coverage + "%</span></td>");
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-info'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].number_endpoints + "</span></td>");
                                            
    //                 }
    //                 else if(sprintMetricDatas.metrics[index_sprint].contract_coverage < dod_contract_test){
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-danger'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].contract_coverage + "%</span></td>");
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-danger'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].number_endpoints + "</span></td>");
    //                 }
    //                 else{
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-success'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].contract_coverage + "%</span></td>");
    //                     document.getElementById('COLUMNS-SPRINT-METRICS' + index_sprint).insertAdjacentHTML('beforeend', "<td><span class='badge badge-success'>"
    //                                         + sprintMetricDatas.metrics[index_sprint].number_endpoints + "</span></td>");
    //                 }
                    
    //             }
    //             document.getElementById('TABLE-SPRINT-METRICS').insertAdjacentHTML('beforeend', "</tr>");
    //         }

        
    //     }
    // }
    
})