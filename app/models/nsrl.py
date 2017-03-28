import sqlite3
from flask import jsonify

DB = '/db/NSRL.db'

def hash_lookup(hash, type):
	result = {}

	query = "SELECT * FROM nsrl WHERE \"{}\"='{}'".format(type, hash)

	try:
		conn = sqlite3.connect(DB)
		cursor = conn.execute(query)
		for row in cursor:
			result['SHA1'] = row[0]
			result['MD5'] = row[1]
			result['CRC32'] = row[2]
			result['FileName'] = row[3]
			result['FileSize'] = row[4]
			result['ProductCode'] = row[5]
			result['OpSystemCode'] = row[6]
			result['SpecialCode'] = row[7]
	except sqlite3.Error as error:
		return jsonify({'response_code': 3, 'message': 'DB problems', 'info': error.args})
	finally:
		conn.close()

	if len(result) > 0:
		return jsonify({'response_code': 0, 'message': 'A match was found in the NSRL DB', 'info': result})
	else:
		return jsonify({'response_code': 1, 'message': 'No matches found in the NSRL DB', 'info': hash})
