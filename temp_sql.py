import sys
import MySQLdb

class mysqlUserDb:
    # warnings.filterwarnings('error')

    def __init__(self):
        self.root = 'root'
        self.host = '127.0.0.1'
        self.rootpw = 'root'
        self.db = 'test_python'

        try:
            print '\nChecking MySQL connection...'
            self.db = MySQLdb.connect(
                self.host, self.root, self.rootpw, self.db)
            self.cursor = self.db.cursor()
            self.cursor.execute('select version()')
            print 'Connection OK, proceeding.'
        except MySQLdb.Error as error:
            print 'Error: %s ' % error + '\nStop.\n'
            sys.exit()

    def createtable(self, table):
        print '\nCreating table...'
        try:
            sql = 'CREATE TABLE IF NOT EXISTS ' + table + \
                ' (id int(11) NOT NULL AUTO_INCREMENT, hostname varchar(200), description varchar(1000), PRIMARY KEY (id))'
            self.cursor.execute(sql)
            tbs = self.cursor.fetchone()
            print 'table created: %s' % tbs
        except Warning as warn:
            print 'Warning: %s ' % warn + '\nStop.\n'
            sys.exit()

    def insert(self, table, hostname, description):
        try:
            sql_insert = "INSERT INTO example (id, hostname, description) VALUES (NULL, '" + \
                hostname + "', '" + description + "')"
            print sql_insert
            self.cursor.execute(sql_insert)
            self.db.commit()
        except Warning as warn:
            print 'Warning: %s ' % warn + '\nStop.\n'
            self.db.rollback()
            sys.exit()

    def query(self, table, hostname, description):
        try:
            sql_query = "SELECT * FROM " + table + " WHERE hostname LIKE '%" + \
                hostname + "%' or description LIKE '%" + description + "%' "
            result_query = self.cursor.execute(sql_query)
            qur = self.cursor.fetchall()
            for (id, hostname, description) in qur:
                print 'ID: {} \thostname: {} \tdescription: {}'.format(id, hostname, description)
        except Warning as warn:
            print 'Warning: %s ' % warn + '\nStop.\n'
            sys.exit()

    def delete(self, table, hostname):
        try:
            sql_query = "DELETE FROM " + table + " WHERE hostname LIKE '%" + \
                hostname + "%'"
            self.cursor.execute(sql_query)
            grs = self.cursor.fetchall()
        except Warning as warn:
            print 'Warning: %s ' % warn + '\nStop.\n'
            sys.exit()

    def __del__(self):
        print '\nFinishing operations...'
        self.cursor.close()
        self.db.close()
        print 'Done.\n'

mySQL_new = mysqlUserDb()
# mySQL_new.insert('example', 'R112', 'conected to R2')
mySQL_new.query('example', '', '')
# mySQL_new.createtable('example')
del mySQL_new


from easysnmp import Session
class Simplesnmp:

    def __init__(self, hostname, community, version):
        self.hostname = hostname
        self.community = community
        self.version = version
        self.session = Session(hostname=self.hostname, community=self.community, version=self.version)

    def snmpwalk(self, oid):
        self.items = self.session.walk(oid)
        return self.items

manager = Simplesnmp('192.168.40.1', 'cisco', 2)
manager.snmpwalk('1.3.6.1.2.1.1.1')
for it in manager.items:
    print it.value

