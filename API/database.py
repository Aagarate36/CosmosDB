

from azure.cosmos import CosmosClient, exceptions, PartitionKey

COSMOS_ENDPOINT ='https://acdbaagdev.documents.azure.com:443/'
COSMOS_KEY = '8oHOT32pws5RuGgix7lZVkqRAFhtHcw5SFUPJutJPXAfK70Vcc5LU1nxj0BpGE5OJh2uj0lmUtwBACDbquRdhg=='
DATABASE_NAME = 'test_db'
Container_NAME ='retail'

#INICIALIZANDO EL CLIENTE
client = CosmosClient(COSMOS_ENDPOINT,COSMOS_KEY)

#CREA U OBTIENE LA BASE DE DATO
database = client.create_database_if_not_exists(id=DATABASE_NAME)

#CREA U OBTIENE EL CONTAINER
container = database.create_container_if_not_exists (
    id = Container_NAME,
	partition_key=PartitionKey(path="/categoria"),
	offer_throughput=400)