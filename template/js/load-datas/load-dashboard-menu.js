$(document).ready(function() {
    var dashboard = JSON.parse(dashboard_menu);
    var status = false
    for(var i = 0; i < dashboard.menu_platforms.length; i++){
        document.getElementById('REPORT_PLATFORM_NAME').insertAdjacentHTML('beforeend', "<li><a href='index-" + dashboard.menu_platforms[i] + ".html'>"+ dashboard.menu_platforms[i] +"</a></li>")
    }
    for(var i = 0; i < langJSON.languages.length; i++){
        if(langJSON.languages[i].tag == dashboard.language){
            status = true
            document.getElementById('title_report').innerHTML = langJSON.languages[i].title_report
            document.getElementById('platform_menu_label').innerHTML = langJSON.languages[i].platform_menu_label
            document.getElementById('report_label').innerHTML = langJSON.languages[i].report_label
            document.getElementById('functional_testing_coverage').innerHTML = langJSON.languages[i].functional_testing_coverage
            document.getElementById('functional_scenarios_card').innerHTML = langJSON.languages[i].functional_scenarios_card
            document.getElementById('contract_testing_coverage').innerHTML = langJSON.languages[i].contract_testing_coverage
            document.getElementById('contract_endpoints_card').innerHTML = langJSON.languages[i].contract_endpoints_card
            document.getElementById('coverage_by_feature_title').innerHTML = langJSON.languages[i].coverage_by_feature_title
            document.getElementById('title_table_sprints').innerHTML = langJSON.languages[i].title_table_sprints
            document.getElementById('name_column_table').innerHTML = langJSON.languages[i].name_column_table
            document.getElementById('unit_test_column_table').innerHTML = langJSON.languages[i].unit_test_column_table
            document.getElementById('functional_column_table').innerHTML = langJSON.languages[i].functional_column_table
            document.getElementById('contract_test_column_table').innerHTML = langJSON.languages[i].contract_test_column_table
            document.getElementById('endpoints_column_table').innerHTML = langJSON.languages[i].endpoints_column_table   
        }
    }
    if(status == false){
        var tag = "en"
        for(var i = 0; i < langJSON.languages.length; i++){
            if(langJSON.languages[i].tag == tag){
                document.getElementById('title_report').innerHTML = langJSON.languages[i].title_report
                document.getElementById('platform_menu_label').innerHTML = langJSON.languages[i].platform_menu_label
                document.getElementById('report_label').innerHTML = langJSON.languages[i].report_label
                document.getElementById('functional_testing_coverage').innerHTML = langJSON.languages[i].functional_testing_coverage
                document.getElementById('functional_scenarios_card').innerHTML = langJSON.languages[i].functional_scenarios_card
                document.getElementById('contract_testing_coverage').innerHTML = langJSON.languages[i].contract_testing_coverage
                document.getElementById('contract_endpoints_card').innerHTML = langJSON.languages[i].contract_endpoints_card
                document.getElementById('coverage_by_feature_title').innerHTML = langJSON.languages[i].coverage_by_feature_title
                document.getElementById('title_table_sprints').innerHTML = langJSON.languages[i].title_table_sprints
                document.getElementById('name_column_table').innerHTML = langJSON.languages[i].name_column_table
                document.getElementById('unit_test_column_table').innerHTML = langJSON.languages[i].unit_test_column_table
                document.getElementById('functional_column_table').innerHTML = langJSON.languages[i].functional_column_table
                document.getElementById('contract_test_column_table').innerHTML = langJSON.languages[i].contract_test_column_table
                document.getElementById('endpoints_column_table').innerHTML = langJSON.languages[i].endpoints_column_table
            }
        }
    }
    
})