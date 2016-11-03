# coding:utf-8
from flask import render_template, current_app
from . import python
from .geo_info import geo_info
import json


@python.route('/')
def index():
    # 查询全国分布图所需数据
    sql = '''select city,count(*) from job_info  where keyword='python' group by city order by count(*) DESC'''
    current_app.cur.execute(sql)
    results = current_app.cur.fetchall()
    data = [dict(name=x[0].encode('utf-8'), value=int(x[1])) for x in results]
    data = json.dumps(data)
    geoCoordMap = json.dumps(geo_info)
    # 查询岗位数量图数据
    job_category_counts = [int(x[1]) for x in results]
    city_category = [x[0].encode('utf-8') for x in results]
    city_category = json.dumps(city_category)
    # 查询工资情况分布图
    sql = 'select salary,count(*) from job_info where keyword="python" group by salary order by count(*) DESC limit 20'
    current_app.cur.execute(sql)
    results = current_app.cur.fetchall()
    salary_json = {key[0].encode('utf-8'): int(key[1]) for key in results}
    salary_json = json.dumps(salary_json)
    # 查询公司规模数据
    sql = 'select companySize,count(*) from job_info where keyword="python" group by companySize order by count(*) DESC limit 30'
    current_app.cur.execute(sql)
    results = current_app.cur.fetchall()
    companySize_json = {key[0].encode('utf-8'): int(key[1]) for key in results}
    companySize_json = json.dumps(companySize_json)
    # 查询工作年限数据
    sql = 'select workYear,count(*) from job_info where keyword="python" group by workYear order by count(*) DESC limit 30'
    current_app.cur.execute(sql)
    results = current_app.cur.fetchall()
    workYear_json = {key[0].encode('utf-8'): int(key[1]) for key in results}
    workYear_json = json.dumps(workYear_json)
    # 查询融资情况
    sql = 'select financeStage,count(*) from job_info where keyword="python" group by financeStage order by count(*) DESC limit 30'
    current_app.cur.execute(sql)
    results = current_app.cur.fetchall()
    financeStage_json = {key[0].encode('utf-8'): int(key[1]) for key in results}
    financeStage_json = json.dumps(financeStage_json)
    return render_template('python/index.html', data=data, geoCoordMap=geoCoordMap, job_category_counts=job_category_counts, city_category=city_category, salary_json=salary_json, companySize_json=companySize_json, workYear_json=workYear_json, financeStage_json=financeStage_json)
