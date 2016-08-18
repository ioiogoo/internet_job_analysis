from . import city
from flask import render_template, current_app, abort, request
import json
from app import logger

@city.route('/<cityname>')
def index(cityname):
	try:
		sql = 'select keyword,count(*) from job_info where city="%s" group by keyword  order by count(*) DESC limit 20' % cityname
		current_app.cur.execute(sql)
		results = current_app.cur.fetchall()
		if not results:
			logger.warning('mysqldb has no %s' % cityname)
			abort(404)
		job_category_counts = [int(x[1]) for x in results]
		job_name = [x[0].encode('utf-8') for x in results]
		job_name = json.dumps(job_name)
		sql = 'select salary,count(*) from job_info where city="%s" group by salary order by count(*) DESC limit 30' % cityname
		current_app.cur.execute(sql)
		results = current_app.cur.fetchall()
		if not results:
			logger.warning('mysqldb has no %s' % cityname)
			abort(404)
		salary_json = {key[0].encode('utf-8'):int(key[1]) for key in results}
		salary_json = json.dumps(salary_json)
		logger.info('success city.index     url: %s    ip: %s' % (request.url, request.remote_addr))
		return render_template('/city/city.html', cityname=cityname, job_name=job_name, job_category_counts=job_category_counts, salary_json=salary_json)
	except Exception as e:
		logger.warning('city.index error: %s    url: %s    ip: %s' % (e, request.url, request.remote_addr))
		abort(404)