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
        except TypeError as error:
            print error
    
    def create_project_database(self, project_name):
        try:
            query = 'use ' + project_name
            self.conn.cursor().execute(query)
        except:
            query = 'create database ' + project_name
            self.conn.cursor().execute(query)
    
    def use_project_database(self, project_name):
        try:
            query = 'use ' + project_name
            self.conn.cursor().execute(query)
        except TypeError as error:
            print error

    def create_table_recent_sprints(self):
        if(self.conn.cursor().execute('show tables like "recent_sprints"') == 0):
            try:
                self.conn.cursor().execute('create table recent_sprints(platform_name varchar(100) NOT NULL, report_name varchar(100) NOT NULL, unit_test_coverage varchar(100) NOT NULL, functional_coverage varchar(100) NOT NULL, contract_coverage varchar(100) NOT NULL, number_endpoints varchar(100) NOT NULL)')
            except TypeError as error:
                print error   

    def insert_recent_sprint_metrics(self, platform_name, report_name, unit_test_coverage, functional_coverage, contract_coverage, number_endpoints):
        try:
            query = "insert into recent_sprints(platform_name, report_name, unit_test_coverage, functional_coverage, contract_coverage, number_endpoints) values ('" + platform_name + "'," + "'" + report_name + "'," + "'" +  unit_test_coverage + "'," + "'" +  functional_coverage + "'," + "'" +  contract_coverage + "'," + "'" +  number_endpoints + "')"
            self.conn.cursor().execute(query)
            self.conn.commit()
        except TypeError as error:
            print error
    
    def clear_recent_sprints_table(self):
        try:
            self.conn.cursor().execute('delete from recent_sprints')
            self.conn.commit()
        except TypeError as error:
            print error

project_name = "MyProect"
myConn = Connection('localhost','root','12345678')
myConn.connect_to_database()
myConn.create_project_database(project_name)
myConn.use_project_database(project_name)
myConn.create_table_recent_sprints()
myConn.insert_recent_sprint_metrics("web", "Sprint 03", "20", "45", "56", "31")
myConn.clear_recent_sprints_table()
