from cassandra.cluster import Cluster

if __name__ == '__main__':
  cluster = Cluster()
  session = cluster.connect()
  session.set_keyspace('mykeyspace')
  session.execute('USE mykeyspace')

#  c_sql = """ CREATE TABLE IF NOT EXISTS employee (id int PRIMARY KEY, name varchar, city varchar); """
#  session.execute(c_sql)


#  c_sql1 = """ INSERT INTO employee (id, name, city) VALUES (1, 'Sivaraj', 'Bangalore');"""
#  session.execute(c_sql1)

#  c_sql2 = session.prepare("INSERT INTO employee (id,name,city) VALUES(2, 'Ramakanth', 'Hyderabad');")
#  session.execute(c_sql2)

#  c_sql3 = """INSERT INTO employee (id, name, city) VALUES(%s, %s, %s)"""
#  session.execute(c_sql3, (3, 'Nagaraj', 'Bangalore'))

#  c_sql4 = """INSERT INTO employee(id, name, city) VALUES(%(id)s, %(name)s, %(city)s)"""
#  session.execute(c_sql4, {'id':4, 'name':'Gopi', 'city':'Hyderabad'})

  rows1 = session.execute('SELECT id, name, city FROM employee;')

  print "using iteration"
  for row in rows1:
    print row.id, row.name, row.city

  rows2 = session.execute('SELECT id, name, city FROM employee;')
 
  print "using tuple"
  for (id,name,city) in rows2:
    print id, name, city

  rows3 = session.execute('SELECT id, name, city FROM employee;')
  for row in rows3:
    print row[0], row[1], row[2]









  



