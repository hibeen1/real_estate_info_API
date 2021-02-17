import pymysql

conn = pymysql.connect(
    user = 'root',
    passwd = 'password',
    host = '127.0.0.1',
    db = 'test',
    charset = 'utf8'
)


#CREATE TABLE
try:
    with conn.cursor() as cursor:
        # CREATE DB
        # sql = 'CREATE DATABASE test'
        # cursor.execute(sql)


        # CREATE TABLE
        # sql = '''
        #     CREATE TABLE users (
        #         id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        #         email varchar(255) NOT NULL,
        #         password varchar(255) NOT NULL
        #     ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        #     '''
        # cursor.execute(sql)


        # INSERT
        # sql = 'INSERT INTO users (email, password) VALUES (%s, %s)'
        # cursor.execute(sql, ('test@test.com', 'my-passwd'))


        # SELECT
        # sql = 'SELECT * FROM users WHERE email = %s'
        # cursor.execute(sql, ('test@test.com',))
        # result = cursor.fetchone()
        # print(result)
        # # (1, 'test@test.com', 'my-passwd')


        # UPDATE
        # sql = 'UPDATE users SET email = %s WHERE email = %s'
        # cursor.execute(sql, ('my@test.com', 'test@test.com'))


        # DELETE
        # sql = 'DELETE FROM users WHERE email = %s'
        # cursor.execute(sql, ('my@test.com',))


        
        # sql = 'INSERT INTO users (email, password) VALUES (%s, %s)'
        # cursor.execute(sql, ('your@test.com', 'your-passwd'))
        cursor.execute('SELECT * FROM users')
        result = cursor.fetchall()
        print(result)
    conn.commit()

finally:
    conn.close()


