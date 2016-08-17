from . import salary
from flask import url_for, render_template, current_app, abort
import json

@salary.route('/<salary_name>')
def index(salary_name):
	try:
		sql = 'select city,count(*) from job_info  where salary="%s" group by city order by count(*) DESC limit 30' % salary_name
		current_app.cur.execute(sql)
		results = current_app.cur.fetchall()
		if not results:
			abort(404)
		job_category_counts = [int(x[1]) for x in results]
		keyword = [x[0].encode('utf-8') for x in results]
		keyword = json.dumps(keyword)

		sql = 'select keyword,count(*) from job_info  where salary="%s" group by keyword order by count(*) DESC limit 30' % salary_name
		current_app.cur.execute(sql)
		results = current_app.cur.fetchall()
		if not results:
			abort(404)
		salary_json = {key[0].encode('utf-8'):int(key[1]) for key in results}
		salary_json = json.dumps(salary_json)
		return render_template('salary/salary.html', job_category_counts=job_category_counts, keyword=keyword, salary_name=salary_name, salary_json=salary_json)
	except Exception as e:
		print e 
		return abort(404)