from azure.storage.blob import BlockBlobService, ContentSettings
from azure.storage.queue import QueueService
from azure.storage.table import TableService, Entity
from datetime import date, timedelta
from settings import *

block_blob_service = BlockBlobService(account_name, account_key)
queue_service = QueueService(account_name, account_key)
table_service = TableService(account_name, account_key)

block_blob_service.create_container(blob_container_name)
queue_service.create_queue(queue_name)
table_service.create_table(table_name)

'''
for i in range(10):
	
	file_name = 'files/file_' + str(i) + '.csv'
	file_id = i

	print (file_id, file_name)
	
	# Add to blob
	block_blob_service.create_blob_from_path(
	    blob_container_name,
	    file_name[6:],
	    file_name,
	    content_settings=ContentSettings(content_type='text/plain')
	            )

	# Add to queue
	queue_service.put_message(queue_name, unicode(file_name))

	# Add to table
	task = {'PartitionKey': str(i), 'Filename': file_name,'RowKey': '20172005', 'status' : 'Uploaded'}
	table_service.insert_entity(table_name, task)
'''

start_date = date.today().replace(day=1, month=1)
day = start_date
for i in range(10):
	for j in range(7):
		filename = 'files/file_' + str(i)  + '_' + str(day) + '.csv'
		print (filename)
		
		# Add to blob
		block_blob_service.create_blob_from_path(
		    blob_container_name,
		    filename.split('/')[1],
		    filename,
		    content_settings=ContentSettings(content_type='text/plain')
	            )
		print ('Added to blob')

		# Add to queue
		queue_service.put_message(queue_name, unicode(filename))
		print ('Added to queue')

		# Add to table
		print (filename.split('_')[1], filename.split('_')[2])
		task = {'PartitionKey': filename.split('_')[1], 'Filename': filename,'RowKey': filename.split('_')[2], 'Status' : 'Uploaded'}
		table_service.insert_entity(table_name, task)
		day = day + timedelta(days = 1)
		print ('Added to table')