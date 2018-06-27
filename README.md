![](images/waever.png)

Weaver is a testing metrics report and review for agile teams. All projects need of overview about unit, service or functional testing and what is being built in sprints, in this way, weaver compiles all those informations and developing team/stakeholders can see it.

# View

# How to generate my report?
**Weaver**'s installation for git:
```
git clone https://github.com/nathsilv/weaver.git
````
After you have cloned, you can see three main files: `main.py`, `config.yml` and `requeriments.txt `<br>

# What is need for running it?
You need to have `python` installed in your machine. <br>
And you will need to have `pip` installed for managing dependencies of project. <br>
After these installations, you can execute command below for installing all dependencies. 
``` 
pip install -r requeriments.txt 
``` 

## Parameters
``` 
python main.py [-l, --lang] <language>
``` 
*[language]* is parameter for report language, today **Weaver** just supporting portuguese and english. But you can contribute and send a Pull Request to add your language: `template/datas/languages.js` <br>

Language Parameter List: <br>
<table> 
  <thead>
    <tr> 
      <th style="text-align: left">Parameter</th> 
      <th style="text-align: center">Language</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td style="text-align: left">pt-br</td> 
      <td style="text-align: center">Portuguese</td> 
    </tr> 
    <tr> 
      <td style="text-align: left">en</td> 
      <td style="text-align: center">English</td> 
    </tr>
  </tbody>
</table> 


## Setting up Config file: `config.yml`
These parameters below can be used: <br>

| Parameter        | Content           |
| ------------- |:-------------:|
|path_to_features:                      | set up full path to feature folder. Ex.: "/Users/MyProject/features/"                         |
|path_to_contract_tests:                | set up full path to contract tests folder. Ex.: "/Users/MyProject/test_files/"                |
|total_endpoints_used:                  | set up total number of endpoints used in project. Ex.: 77|
|platforms:                             | set up tags of the platforms being used in the scenario writing files in cucumber. Ex: If scenario is automated, set @android tag in *.feature* file and in *config.yml* set "android". If you have more platforms, set all tags. Ex: "android, ios, web"                                                                                                                 |
|report_name:                           | Set up report name or can used sprint name for better view in evolution tables and graphics. Ex.: "Sprint Dev 01"                                                                                                                    |
|ios_unit_test_report:                  | Set up full path to iOS unit test report of Slather. Ex.: "/Users/DevProject/reports/index.html"                                                                                                  |
|android_unit_test_report               | Set up full path to Android unit test report of Jacoco. Ex.: "/Users/DevProject/reports/index.html"                                                                                                  |
|jira_android:                          | Set up this tag if you want to get Android bugs metrics from jira. Ex.: "true"                |
|jira_ios:                              | Set up this tag if you want to get iOS bugs metrics from jira. Ex.: "true"                    |

# View JIRA Bugs

# View JIRA Activities

# Integration




