from azure.storage.blob import BlockBlobService, PublicAccess

block_blob_service = BlockBlobService(account_name='shakenov', account_key='1/cjKM7g2rMMy2mf1r2XK4LXvbS5vFG7cXJjUDNbA8KVZbEBbi3zIMeAexwbl99M7CoKFYJhUqtuIEM+ypn9Zg==')

# Create public container
# block_blob_service.create_container('mycontainer', public_access=PublicAccess.Container)

# Create container and make it public
# block_blob_service.create_container('mycontainer')
# block_blob_service.set_container_acl('mycontainer', public_access=PublicAccess.Container)

# Upload blob
# from azure.storage.blob import ContentSettings
# block_blob_service.create_blob_from_path(
#     'mycontainer',
#     'myblockblob',
#     'sunset.png',
#     content_settings=ContentSettings(content_type='image/png')
#             )

# List of blobs in container
# generator = block_blob_service.list_blobs('mycontainer')
# for blob in generator:
#     print(blob.name)

# Download blob
# block_blob_service.get_blob_to_path('mycontainer', 'myblockblob', 'out-sunset.png')

from azure.storage.blob import AppendBlobService
append_blob_service = AppendBlobService(account_name='shakenov', account_key='1/cjKM7g2rMMy2mf1r2XK4LXvbS5vFG7cXJjUDNbA8KVZbEBbi3zIMeAexwbl99M7CoKFYJhUqtuIEM+ypn9Zg==')

# The same containers can hold all types of blobs
append_blob_service.create_container('mycontainer')

# Append blobs must be created before they are appended to
append_blob_service.create_blob('mycontainer', 'myappendblob')
append_blob_service.append_blob_from_text('mycontainer', 'myappendblob', u'Hello, world!')

append_blob = append_blob_service.get_blob_to_text('mycontainer', 'myappendblob')