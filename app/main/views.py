# *-* coding: utf-8 *-*
from . import main
from flask import url_for, render_template, current_app
import MySQLdb
import json


@main.route('/')
def index():
	# 从数据库查询第一个图表需要的信息
	sql = '''select city,count(*) from job_info group by city order by count(*) DESC limit 30 '''
	current_app.cur.execute(sql)
	results = current_app.cur.fetchall()
	# 岗位数量
	job_category_counts = [int(x[1]) for x in results]
	# 不同城市名称
	city_category = [x[0].encode('utf-8') for x in results]
	city_category = json.dumps(city_category)
	# 从数据库查询第二个图表需要的信息
	sql = '''select keyword,count(*) from job_info group by keyword order by count(*) DESC limit 20'''
	current_app.cur.execute(sql)
	results = current_app.cur.fetchall()
	# 职业饼形图需要json格式
	keyword_json = {key[0].encode('utf-8'):int(key[1]) for key in results}
	keyword_json = json.dumps(keyword_json)
	# 从数据库查询第三个图表需要的信息
	sql = 'select salary,count(*) from job_info group by salary order by count(*) DESC limit 30'
	current_app.cur.execute(sql)
	results = current_app.cur.fetchall()
	# 薪资饼形图需要json格式
	salary_json = {key[0].encode('utf-8'):int(key[1]) for key in results}
	salary_json = json.dumps(salary_json)
	return render_template('main/index.html', job_category_counts=job_category_counts, city_category=city_category, keyword_json=keyword_json, salary_json=salary_json)


@main.before_app_first_request
def mysql_conn():
	current_app.conn = MySQLdb.connect(host='localhost', user='root', passwd='qwer', charset='utf8', db='lagou')
	current_app.cur = current_app.conn.cursor()