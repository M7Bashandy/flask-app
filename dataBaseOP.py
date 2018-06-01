import MySQLdb
import psycopg2
def parent(nodeName):
    result=[]
    while (True):
        id, node_name, PID = Query(nodeName)
        if PID is None:
            break;
        else:
            id,node_name,PID= Query(PID)
            result.append(str(node_name))
            nodeName = node_name
    return result


def child(nodeName):
    result = []
    db = MySQLdb.connect("localhost", "root", "root", "nodes")
    cursor = db.cursor()

    sql = "SELECT B.node_name AS nodes FROM info A, info B " \
          "WHERE A.id = B.parent_id " \
          "AND A.node_name ='%s';" % (nodeName)
    print sql

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            Parent_name = row[0]
            result.append(Parent_name)

    except:
        print "Error: unable to fecth data"

    db.close()
    return result


def Table():
    result=[]
    node=[""]
    db = MySQLdb.connect("localhost", "root", "root", "nodes")
    cursor = db.cursor()

    sql = "SELECT P.node_name AS nodes , P.parent_id AS Parent " \
          "FROM info P WHERE P.parent_id is NULL " \
          "UNION " \
          "SELECT B.node_name AS nodes ,A.node_name AS Parent " \
          "FROM info A, info B " \
          "WHERE  A.id = B.parent_id;"
    print sql
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            node_name = row[0]
            Parent_name = row[1]
            obj = {
                'node': str(node_name),
                'parents': str(Parent_name)
            }
            result.append(obj)
            node.append(node_name)
    except:
        print "Error: unable to fecth data"
    db.close()
    return node,result


def Query(search):

    if isinstance(search, str):
        print search
        sql = "SELECT * FROM info WHERE node_name = '%s'" % (str(search))
    elif isinstance(search, long):
        print search
        sql = "SELECT * FROM info WHERE id= '%d'" % (int(search))
    db = MySQLdb.connect("localhost", "root", "root", "nodes")
    cursor = db.cursor()

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            node_name = row[1]
            parent_id = row[2]

    except:
        db.rollback()
    db.close()
    return id,node_name,parent_id



def register(name ,parentid):
    import MySQLdb

    db = MySQLdb.connect("localhost", "root", "root", "nodes")
    cursor = db.cursor()
    if parentid=="":
        sql = "INSERT INTO info( node_name)VALUES ('%s')" % (name)
    else:
        sql = "INSERT INTO info( node_name,parent_id )VALUES ('%s', '%d' )" % (name ,parentid)
    print sql
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def update(name ,parentid):
    import MySQLdb
    data=(parentid,name)
    db = MySQLdb.connect("localhost", "root", "root", "nodes")
    cursor = db.cursor()
    sql=""" UPDATE info
                SET parent_id = %s
                WHERE node_name = %s """
    print sql
    try:
        cursor.execute(sql,data)
        db.commit()
    except:
        db.rollback()
    db.close()
