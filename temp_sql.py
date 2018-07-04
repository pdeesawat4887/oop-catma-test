# import sys
# import MySQLdb


# class mysqlUserDb:
#     # warnings.filterwarnings('error')

#     def __init__(self):
#         self.root = 'root'
#         self.host = '127.0.0.1'
#         self.rootpw = 'root'
#         self.db = 'test_python'

#         try:
#             print '\nChecking MySQL connection...'
#             self.db = MySQLdb.connect(
#                 self.host, self.root, self.rootpw, self.db)
#             self.cursor = self.db.cursor()
#             self.cursor.execute('select version()')
#             print 'Connection OK, proceeding.'
#         except MySQLdb.Error as error:
#             print 'Error: %s ' % error + '\nStop.\n'
#             sys.exit()

#     def createtable(self, table):
#         print '\nCreating table...'
#         try:
#             sql = 'CREATE TABLE IF NOT EXISTS ' + table + \
#                 ' (id int(11) NOT NULL AUTO_INCREMENT, hostname varchar(200), description varchar(1000), PRIMARY KEY (id))'
#             self.cursor.execute(sql)
#             tbs = self.cursor.fetchone()
#             print 'table created: %s' % tbs
#         except Warning as warn:
#             print 'Warning: %s ' % warn + '\nStop.\n'
#             sys.exit()

#     def insert(self, table, hostname, description):
#         try:
#             sql_insert = "INSERT INTO example (id, hostname, description) VALUES (NULL, '" + \
#                 hostname + "', '" + description + "')"
#             print sql_insert
#             self.cursor.execute(sql_insert)
#             self.db.commit()
#         except Warning as warn:
#             print 'Warning: %s ' % warn + '\nStop.\n'
#             self.db.rollback()
#             sys.exit()

#     def query(self, table, hostname, description):
#         try:
#             sql_query = "SELECT * FROM " + table + " WHERE hostname LIKE '%" + \
#                 hostname + "%' or description LIKE '%" + description + "%' "
#             result_query = self.cursor.execute(sql_query)
#             qur = self.cursor.fetchall()
#             for (id, hostname, description) in qur:
#                 print 'ID: {} \thostname: {} \tdescription: {}'.format(id, hostname, description)
#         except Warning as warn:
#             print 'Warning: %s ' % warn + '\nStop.\n'
#             sys.exit()

#     def delete(self, table, hostname):
#         try:
#             sql_query = "DELETE FROM " + table + " WHERE hostname LIKE '%" + \
#                 hostname + "%'"
#             self.cursor.execute(sql_query)
#             grs = self.cursor.fetchall()
#         except Warning as warn:
#             print 'Warning: %s ' % warn + '\nStop.\n'
#             sys.exit()

#     def __del__(self):
#         print '\nFinishing operations...'
#         self.cursor.close()
#         self.db.close()
#         print 'Done.\n'


from easysnmp import Session


class Simplesnmp:

    def __init__(self, hostname, community, version, temp_sysDesc=None, temp_hostname=None, temp_totalInt=None,
                 temp_MemUse=None, temp_MemFree=None, temp_NvramSize=None, temp_NvramUse=None, temp_Power=None,
                 temp_Vol=None):
        self.temp = [temp_sysDesc, temp_hostname, temp_totalInt, temp_MemUse, temp_MemFree, temp_NvramSize, temp_NvramUse, temp_Power, temp_Vol]
        self.hostname = hostname
        self.community = community
        self.version = version
        self.session = Session(hostname=self.hostname,
                               community=self.community, version=self.version)

    def snmpwalk(self, oid):
        items = self.session.walk(oid)
        return items


class FileOperation:

    def __init__(self):
        self.oid_list = []

    def readFile(self, filename):
        with open(filename, 'r+') as file:
            temp_file = file.read()
            self.oid_list = temp_file.split()
            file.close()
            return self.oid_list

oid_item = FileOperation()
oid_item.readFile('oid_list.txt')

print oid_item.oid_list
print len(oid_item.oid_list)

walker = Simplesnmp('10.10.10.1', 'test', 2)

# for it in range(len(oid_item.oid_list)):
#     print oid_item.oid_list[it]

for unit in range(len(walker.temp)):
    # print walker.temp[unit] = walker.snmpwalk()
    walker.temp[unit] = walker.snmpwalk(oid_item.oid_list[unit])

for it in walker.temp:
    print it

# mySQL_new = mysqlUserDb()
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
