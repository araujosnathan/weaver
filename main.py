# -*- coding: utf-8 -*-

import yaml
import json
import shutil
import fnmatch
from platform.general_datas_class import GeneralDatas 
from platform.generate_generalDatas_class import GenerateGeneralDatas 
import sys, getopt

def main(argv):
    global lang
    lang = ''
    teams = 1
    if (len(argv) < 1):
        print 'usage: main.py [-l, --lang] <language>'
        sys.exit(2)
    else:
        try:
            opts, args = getopt.getopt(argv,"l:t:",["lang=","teams="])
        except getopt.GetoptError:
            print 'usage: main.py [-l, --lang] <language>'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print 'usage: main.py [-l, --lang] <language>'
                sys.exit()
            elif opt in ("-l", "--lang"):
                lang = arg
            elif opt in ("-t", "--teams"):
                teams = arg

def check_language(language):
    lang_file = open('./template/datas/languages.js', 'r')
    status = False
    for line in lang_file.readlines():
        pattern = '*"tag":' + '"' + language + '"*'
        if fnmatch.fnmatch(line, pattern):
            status = True
    if not status:
        print "\033[33mThis language: \033[4m" + language + "\033[0m\033[33m was not found in language dictionary.\nSo, report will be generate in english. \nYou can add your langue in \033[4mtemplate/datas/languages.js\033[m"


def weaver():
    config_file = open('config.yml')
    parameters                          = yaml.load(config_file)
    path_to_features_folder             = parameters.get('path_to_features')
    path_to_contract_tests_folder       = parameters.get('path_to_contract_tests')
    total_endpoints_used                = parameters.get('total_endpoints_used')
    path_unit_test_ios                  = parameters.get('ios_unit_test_report')
    path_unit_test_android              = parameters.get('android_unit_test_report')
    platforms                           = parameters.get('platforms')
    report_name                         = parameters.get('report_name')


    dashboard_menu = {}
    dashboard_menu['menu_platforms'] = []
    dashboard_menu['language'] = ""
    dashboard_menu['language'] = lang
    sprint_platforms = {}
    sprint_platforms['platforms'] = []

    for platform in platforms.split(','):
        platform = platform.strip()
        pageGeneralDatas = GeneralDatas(path_to_features_folder, path_to_contract_tests_folder, total_endpoints_used, path_unit_test_ios, path_unit_test_android, platform)
        generateGeneralDatas = GenerateGeneralDatas(pageGeneralDatas, platform, report_name)

        sprint_datas = generateGeneralDatas.set_dashboard_by_platform()
        sprint_platforms['platforms'].append(sprint_datas)
        generateGeneralDatas.set_sprint_metrics_dashbord_by_platform()
        dashboard_menu['menu_platforms'].append(platform)
        shutil.copy2('template/index.html', 'template/index-' + platform + '.html')

    sprint_platforms = json.dumps(sprint_platforms, ensure_ascii=False)
    with open('template/datas/generalDatas.json', 'w') as outfile: 
                outfile.write("data = '" +  str(sprint_platforms) + "'")

    dashboard_menu = json.dumps(dashboard_menu, ensure_ascii=False)
    with open('template/datas/dashboardMenu.json', 'w') as outfile:
        outfile.write("dashboard_menu = '" +  str(dashboard_menu) + "'")

print "Generating Weaver Report ... "
main(sys.argv[1:])
check_language(lang)
weaver()
print "Weaver Report generated with successful ... "
   
