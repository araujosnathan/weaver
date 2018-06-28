import pymysql

class Connection:

    def __init__(self, host, username, password):
        self.conn = ()
        self.host = host
        self.username = username
        self.password = password

    def connect_to_database(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.username, password=self.password)
        except:
             print "\033[31;1m" + "It is NOT possible to connect to database. \nPlease, set corret host, username or password " +"\033[m"
    
    def create_project_database(self, project_name):
        try:
            query = 'use ' + project_name
            self.conn.cursor().execute(query)
        except:
            query = 'create database ' + project_name
            self.conn.cursor().execute(query)
    
    def use_database_project(self, project_name):
        try:
            query = 'use ' + project_name
            self.conn.cursor().execute(query)
        except TypeError as e:
            # print "\033[31;1m" + "It not possible to use \033[4m" + project_name + "\033[0m \033[31;1mdatabase. \nPlease, check this database in your MySQL!\033[m"
            print e

    def create_table_recent_sprints(self, project_name):
        try:
            self.conn.cursor().execute('create table recent_sprints(platform_name varchar(100) NOT NULL, report_name varchar(100) NOT NULL, unit_test_coverage varchar(100) NOT NULL, functional_coverage varchar(100) NOT NULL, contract_coverage varchar(100) NOT NULL, number_endpoints varchar(100) NOT NULL)')
        except TypeError as e:
            print e
            # print "\033[31;1m" + "It not possible to create \033[4m" + "recent_sprints" + "\033[0m \033[31;1mtable. \nPlease, check this table in your MySQL!\033[m"
            

    def insert_recent_sprint_metrics(platform_name, report_name, unit_test_coverage, functional_coverage, contract_coverage, number_endpoints):
        try:
            # self.conn.cursor().execute('create table recent_sprints(platform_name varchar(100) NOT NULL, report_name varchar(100) NOT NULL, unit_test_coverage varchar(100) NOT NULL, functional_coverage varchar(100) NOT NULL, contract_coverage varchar(100) NOT NULL, number_endpoints varchar(100) NOT NULL)')
            query = 'insert into recent_sprints(platform_name, report_name, unit_test_coverage, functional_coverage, contract_coverage, number_endpoints) values (' + (platform_name, report_name, unit_test_coverage, functional_coverage, contract_coverage, number_endpoints) + ")"
            self.conn().execute(query)
        except TypeError as e:
            print e

project_name = "MyProect"
myConn = Connection('localhost','root','12345678')
myConn.connect_to_database()
myConn.create_project_database(project_name)
myConn.use_database_project(project_name)
# myConn.create_table_recent_sprints(project_name)
myConn.insert_recent_sprint_metrics("Sprint 01","20","45","56","31")
