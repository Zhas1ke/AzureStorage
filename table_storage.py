from azure.storage.table import TableService, Entity

table_service = TableService(account_name='shakenov', account_key='1/cjKM7g2rMMy2mf1r2XK4LXvbS5vFG7cXJjUDNbA8KVZbEBbi3zIMeAexwbl99M7CoKFYJhUqtuIEM+ypn9Zg==')

# Create table
# table_service.create_table('tasktable')

# Create record from json
# task = {'PartitionKey': 'tasksSeattle', 'RowKey': '001', 'description' : 'Take out the trash', 'priority' : 200}
# table_service.insert_entity('tasktable', task)

# Create record (method 2)
# task = Entity()
# task.PartitionKey = 'tasksSeattle'
# task.RowKey = '002'
# task.description = 'Wash the car'
# task.priority = 100
# table_service.insert_entity('tasktable', task)

# Update record
# task = {'PartitionKey': 'tasksSeattle', 'RowKey': '001', 'description' : 'Take out the garbage', 'priority' : 250}
# table_service.update_entity('tasktable', task)

# # Replace the entity created earlier
# task = {'PartitionKey': 'tasksSeattle', 'RowKey': '001', 'description' : 'Take out the garbage again', 'priority' : 250}
# table_service.insert_or_replace_entity('tasktable', task)

# # Insert a new entity
# task = {'PartitionKey': 'tasksSeattle', 'RowKey': '003', 'description' : 'Buy detergent', 'priority' : 300}
# table_service.insert_or_replace_entity('tasktable', task)

# # Batch load
# from azure.storage.table import TableBatch
# batch = TableBatch()
# task004 = {'PartitionKey': 'tasksSeattle', 'RowKey': '004', 'description' : 'Go grocery shopping', 'priority' : 400}
# task005 = {'PartitionKey': 'tasksSeattle', 'RowKey': '005', 'description' : 'Clean the bathroom', 'priority' : 100}
# batch.insert_entity(task004)
# batch.insert_entity(task005)
# table_service.commit_batch('tasktable', batch)

# # Batch load usin context manager
# task006 = {'PartitionKey': 'tasksSeattle', 'RowKey': '006', 'description' : 'Go grocery shopping', 'priority' : 400}
# task007 = {'PartitionKey': 'tasksSeattle', 'RowKey': '007', 'description' : 'Clean the bathroom', 'priority' : 100}

# with table_service.batch('tasktable') as batch:
#     batch.insert_entity(task006)
#     batch.insert_entity(task007)

# # Get by partition and row key
# task = table_service.get_entity('tasktable', 'tasksSeattle', '001')
# print(task.description)
# print(task.priority)

# # Get by partition key
# tasks = table_service.query_entities('tasktable', filter="PartitionKey eq 'tasksSeattle'")
# for task in tasks:
#     print(task.description)
#     print(task.priority)

# # Get only descriptions by partition key
# tasks = table_service.query_entities('tasktable', filter="PartitionKey eq 'tasksSeattle'", select='description')
# for task in tasks:
#     print(task.description)

# Delete an entity
#table_service.delete_entity('tasktable', 'tasksSeattle', '001')

# Delete table
# table_service.delete_table('tasktable')