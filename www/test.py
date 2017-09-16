import orm
from models import User, Blog, Comment
import asyncio

def test():
    loop = asyncio.get_event_loop()
    yield from orm.create_pool(loop=loop , user='root', password='1234', database='blog')

    u = User(name='yyk', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

# for x in test():
#     pass

import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306,
                                           user='root', password='1234',
                                           db='blog')
cur = conn.cursor()
cur.execute("SELECT * FROM users")
str = cur.fetchall()
print(str)


