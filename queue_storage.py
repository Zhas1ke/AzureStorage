from azure.storage.queue import QueueService

queue_service = QueueService(account_name='shakenov', account_key='1/cjKM7g2rMMy2mf1r2XK4LXvbS5vFG7cXJjUDNbA8KVZbEBbi3zIMeAexwbl99M7CoKFYJhUqtuIEM+ypn9Zg==')

# queue_service.create_queue('taskqueue')

# Put messages
# for i in range(10):
# 	queue_service.put_message('taskqueue', u'Hello World ' + unicode(str(i)))

# Print messages
# messages = queue_service.peek_messages('taskqueue', num_messages=16)
# for message in messages:
# 	print(message.content)

# Print messages and delete them - only 1
# messages = queue_service.get_messages('taskqueue')
# for message in messages:
#     print(message.content)
#     queue_service.delete_message('taskqueue', message.id, message.pop_receipt)

# Print messages and delete them - batch of messages
# messages = queue_service.get_messages('taskqueue', num_messages=16, visibility_timeout=5*60)
# for message in messages:
#     print(message.content)
#     queue_service.delete_message('taskqueue', message.id, message.pop_receipt)

# Change the message
# messages = queue_service.get_messages('taskqueue', visibility_timeout=5)
# for message in messages:
#     queue_service.update_message('taskqueue', message.id, message.pop_receipt, 0, u'Hello World Again')

# Get the Queue Length
metadata = queue_service.get_queue_metadata('taskqueue')
count = metadata.approximate_message_count
print (count)

# Delete queue
queue_service.delete_queue('taskqueue')