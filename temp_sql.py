import sys
import MySQLdb


class mysqlUserDb:
    # warnings.filterwarnings('error')

    def __init__(self):
        self.root = 'root'
        self.host = '127.0.0.1'
        self.rootpw = 'root'
        self.db = 'test-catma'

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

    def r_insert(self, table, sysDesc, hostname, totalInt, MemUse, MemFree, NvramSize, NvramUse, power, vol, location):
        try:
            sql_insert_r = "INSERT INTO " + table + " VALUES (NULL, '" + sysDesc + "', '" + hostname + "', '" + totalInt + "', '" + \
                MemUse + "', '" + MemFree + "', '" + NvramSize + "', '" + NvramUse + \
                "', '" + power + "', '" + vol + "', '" + location + "')"
            print sql_insert_r
            self.cursor.execute(sql_insert_r)
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


from easysnmp import Session


class Simplesnmp:

    sysDesc = None
    hostname_r = None
    totalInt = None
    MemUsed = None
    MemFree = None
    NvramSize = None
    NvramUsed = None
    powerSup = None
    voltage = None
    location = None

    def __init__(self, hostname, community, version):
        # self.temp = [temp_sysDesc, temp_hostname, temp_totalInt, temp_MemUse, temp_MemFree, temp_NvramSize, temp_NvramUse, temp_Power, temp_Vol, temp_Location]
        self.hostname = hostname
        self.community = community
        self.version = version
        self.session = Session(hostname=self.hostname,
                               community=self.community, version=self.version)

    def snmpwalk(self, oid):
        items = self.session.walk(oid)
        return items

    def set_system(self, item):
        self.sysDesc = item[0].value
        self.hostname_r = item[4].value
        self.location = item[5].value

    def update_first(self):
        self.sysDesc = self.session.walk('1.3.6.1.2.1.1.1')[0].value
        self.hostname_r = self.session.walk('1.3.6.1.2.1.1.5')[0].value
        self.totalInt = self.session.walk('1.3.6.1.2.1.2.1')[0].value
        self.MemUsed = self.session.walk('1.3.6.1.4.1.9.9.48.1.1.1.5')[0].value
        self.MemFree = self.session.walk('1.3.6.1.4.1.9.9.48.1.1.1.6')[0].value
        self.NvramSize = self.session.walk('1.3.6.1.4.1.9.9.195.1.1.1.2')[0].value
        self.NvramUsed = self.session.walk('1.3.6.1.4.1.9.9.195.1.1.1.3')[0].value
        self.powerSup = self.session.walk('1.3.6.1.4.1.9.9.13.1.5.1.2')[0].value
        self.voltage = self.session.walk('1.3.6.1.4.1.9.9.13.1.2.1.3')[0].value
        self.location = self.session.walk('1.3.6.1.2.1.1.6')[0].value

    # def separate(self, list):
    #     for i in xrange(0,len(list),2):
    #         x = list[i]
    #         # print "X:", x
    #         print self.session.walk(list[i+1])[0].value
    #         vars()[x] = self.session.walk(list[i+1])[0].value
        # print dir(list[i])
        # print "---->", my_dict[x],"\n"
        # print my_dict
        # print voltage


class FileOperation:

    def __init__(self):
        self.oid_list = []

    def readFile(self, filename):
        with open(filename, 'r+') as file:
            temp_file = file.read()
            self.oid_list = temp_file.split()
            file.close()
            return self.oid_list


walker_r1 = Simplesnmp('192.168.40.1', 'cisco', 2)
walker_r1.update_first()

walker_r2 = Simplesnmp('192.168.10.2', 'cisco', 2)
walker_r2.update_first()

walker_r3 = Simplesnmp('192.168.20.2', 'cisco', 2)
walker_r3.update_first()

# mySQL_connection = mysqlUserDb()
# mySQL_connection.r_insert('Router', walker_r1.sysDesc, walker_r1.hostname_r, walker_r1.totalInt, walker_r1.MemUsed,
#                    walker_r1.MemFree, walker_r1.NvramSize, walker_r1.NvramUsed, walker_r1.powerSup, walker_r1.voltage, walker_r1.location)

# mySQL_connection.r_insert('Router', walker_r2.sysDesc, walker_r2.hostname_r, walker_r2.totalInt, walker_r2.MemUsed,
#                    walker_r2.MemFree, walker_r2.NvramSize, walker_r2.NvramUsed, walker_r2.powerSup, walker_r2.voltage, walker_r2.location)

# mySQL_connection.r_insert('Router', walker_r3.sysDesc, walker_r3.hostname_r, walker_r3.totalInt, walker_r3.MemUsed,
#                    walker_r3.MemFree, walker_r3.NvramSize, walker_r3.NvramUsed, walker_r3.powerSup, walker_r3.voltage, walker_r3.location)

# oid_item = FileOperation()
# oid_item.readFile('oid_list2.txt')

# print oid_item.oid_list
# print len(oid_item.oid_list)

# walker = Simplesnmp('192.168.40.1', 'cisco', 2)
# print dir(walker)

# list[i] = list[i+1]
# exec("%s = %s" % (list[i], list[i+1]))
# item = walker.snmpwalk('system')
# walker.set_system(item)
# walker.totalInt = walker.snmpwalk('1.3.6.1.2.1.2.1')[0].value
# walker.MemUsed = walker.snmpwalk('1.3.6.1.4.1.9.9.48.1.1.1.5')[0].value
# walker.MemFree = walker.snmpwalk('1.3.6.1.4.1.9.9.48.1.1.1.6')[0].value
# walker.NvramSize = walker.snmpwalk('1.3.6.1.4.1.9.9.195.1.1.1.2')[0].value
# walker.NvramUsed = walker.snmpwalk('1.3.6.1.4.1.9.9.195.1.1.1.3')[0].value
# walker.powerSup = walker.snmpwalk('1.3.6.1.4.1.9.9.13.1.5.1.2')[0].value
# walker.voltage = walker.snmpwalk('1.3.6.1.4.1.9.9.13.1.2.1.3')[0].value

# walker.update_first()

# walker_2 = Simplesnmp('192.168.20.2', 'cisco', 2)
# walker_2.update_first()

# # walker_3 = Simplesnmp('192.168.10.2', 'cisco', 2)
# # walker_3.update_first()

# # print walker.hostname_r

# mySQL_new = mysqlUserDb()
# mySQL_new.r_insert('Router', walker.sysDesc, walker.hostname_r, walker.totalInt, walker.MemUsed,
#                    walker.MemFree, walker.NvramSize, walker.NvramUsed, walker.powerSup, walker.voltage, walker.location)

# # for it in range(len(item)):
# print("Sys: {}\nHostname: {}\nTotalInterface: {}\nMemUsed: {}\nMemFree: {}\nNVRAMSize: {}\nNVRAMUsed: {}\nPower: {}\nVoltage: {}\nLocation: {}\n").format(
# walker.sysDesc, walker.hostname_r, walker.totalInt, walker.MemUsed,
# walker.MemFree, walker.NvramSize, walker.NvramUsed, walker.powerSup,
# walker.voltage, walker.location)

# walker_new = Simplesnmp('192.168.20.1', 'cisco', 2)
# print dir(walker)
# walker.sysDesc = walker.snmpwalk('1.3.6.1.2.1.1.1')
# print walker.sysDesc
# print dir(walker)

# print walker.temp_sysDesc

# for it in range(len(oid_item.oid_list)):
#     print oid_item.oid_list[it]

# for unit in range(len(walker.temp)):
#     # print walker.temp[unit] = walker.snmpwalk()
#     walker.temp[unit] = walker.snmpwalk(oid_item.oid_list[unit])
#     # print walker.snmpwalk(oid_item.oid_list[unit])

# for it in walker.temp:
#     # print '{} = {}'.format(it[0].oid, it[0].value)
#     print it[0].value

# mySQL_new = mysqlUserDb()
# mySQL_new
# # mySQL_new.insert('example', 'R112', 'conected to R2')
# # mySQL_new.query('example', '', '')
# # mySQL_new.createtable('example')
#
# manager = Simplesnmp('192.168.40.1', 'cisco', 2)
# temp_desc = manager.snmpwalk('1.3.6.1.2.1.1.1')
# temp_ho = manager.snmpwalk('1.3.6.1.4.1.9.2.1.3')
# temp_sys = manager.snmpwalk('system')
#
# temp_list =[]
#
# for it in temp_sys:
#     temp_list.append(it.value)
#
# print temp_list
#
# print len(temp_list)
# for i in temp_list:
#     print i
# # print len(temp_desc[0].value)
#
# # print (temp_des[0].value)
#
# # mySQL_new.insert('example', temp_ho[0].value, temp_desc[0].value)
#
# # mySQL_new.query('example', '', 'cisco')
#
# del mySQL_new
#
# # print manager.items.value()
#
# # for it in temp_desc:
# #     print it.value
