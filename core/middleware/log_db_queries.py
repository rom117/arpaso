#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import connection
from django.http import HttpResponse


#Q3: store all the queries made upon the database in a sql log file
class SaveSQLQueriesToLogFile(object):
    def process_response(self, request, response):
		fileName="logs/sql_queries.sql"
		with open(fileName, 'a+') as logging:
			for query in connection.queries:
				logging.write(query['sql']+"\n")
		return response
