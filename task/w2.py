from azure.storage.queue import QueueService
from azure.storage.table import TableService, Entity
from azure.storage.blob import BlockBlobService

from settings import *
import pandas as pd
import os

queue_service = QueueService(account_name, account_key)
table_service = TableService(account_name, account_key)
block_blob_service = BlockBlobService(account_name, account_key)

generator = block_blob_service.list_blobs(blob_container_name)

while (1):
	messages = queue_service.get_messages(queue_name, num_messages=32, visibility_timeout=5*60)
	for message in messages:
		print(message.content)
		blob_name = message.content.split('/')[1]
		filename = blob_name
		print (blob_name)
		block_blob_service.get_blob_to_path(blob_container_name, blob_name, 'file.tmp')
		df = pd.read_csv('file.tmp', header = None)
		print (df.head())

		fsum = df.sum()[0].item()
		print (fsum)

		# Update record
		result = '<?xml version="1.0" encoding="UTF-8"?><result><sum>' + str(fsum) + '</sum></result>'
		task = {'PartitionKey': filename.split('_')[1], 'Filename': filename, 'RowKey': filename.split('_')[2], 'Status' : 'Completed', 'Sum': result}
		table_service.update_entity(table_name, task)

		try:
			partition_key = filename.split('_')[1]
			row_key = filename.split('_')[2]
			task2 = {'PartitionKey': partition_key, 'RowKey': row_key, 'Status' : 'Completed', 'Sum': result}
			table_service.merge_entity(table_name, partition_key, row_key, task2, content_type='application/atom+xml')
		except:
			print ('merge error')

		block_blob_service.delete_blob(blob_container_name, blob_name)
		os.remove('file.tmp')
		queue_service.delete_message(queue_name, message.id, message.pop_receipt)