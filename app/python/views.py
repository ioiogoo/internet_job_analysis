from flask import render_template, current_app
from . import python
from .geo_info import geo_info
import json

@python.route('/')
def index():
    # sql = '''select city,count(*) from job_info  where keyword='python' group by city order by count(*) DESC'''
    sql = ''' select city,count(*) from job_info  group by city order by count(*) DESC limit 100'''
    current_app.cur.execute(sql)
    results = current_app.cur.fetchall()
    data = [dict(name=x[0].encode('utf-8'), value=int(x[1])) for x in results]
    data = json.dumps(data)
    geoCoordMap = json.dumps(geo_info)
    return render_template('python/index.html', data=data, geoCoordMap=geoCoordMap)

