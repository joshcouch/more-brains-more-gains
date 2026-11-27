import boto3

class DynamodbWriter():
    def __init__(self, table_name: str, region_name: str ='eu-north-1'):
        self.service_name = 'dynamodb'
        self.table_name = table_name
        self.region_name = region_name
        self.dynamodb = None #boto3.resource(self.service_name, region_name=self.region_name)
        self.table = None #self.dynamodb.Table(self.table_name)
        
    def write_single_item(self, item: dict):
        response = True #self.table.put_item(Item=item)
        return response
    
    # todo: implement duplicate checking and handling when writing


