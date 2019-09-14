from datastore import operations
import logging
import threading
import json  

logging.basicConfig(filename='datastore_app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

lock = threading.RLock()

def create(client, key, value, **kwargs):
	ttl_value = kwargs.get('ttl', None)
	with lock:
		if isinstance(value, str):
			try:
				value = json.loads(value)
			except:
				value = value
		status = operations.create_operation(client, key, value, ttl = ttl_value)
		if 'successfull' in status:
			return "Create Operation Done"
		elif 'denied' in status:
			logging.error(status)
			return "Error occurred while creating : " + status
		else:
			logging.error(status)
			return "Error Status : " + status


def delete(client, key):
	with lock:
		status = operations.delete_operation(client, key)
		if 'Deleted' in status:
			return status
		elif 'not found' in status:
			logging.error(status)
			return status
		else:
			logging.error(status)
			return "Error Status : " + status


def read(client, key):
	with lock:
		status = operations.read_operation(client, key)
		if 'not found' in status:
			logging.error(status)
			return status
		elif 'value' in status:
			return status
		else:
			logging.error(status)
			return "Error Status : " + status


def reset(client):
	with lock:
		status = operations.reset_operation(client)
		logging.info(status)
		return status

