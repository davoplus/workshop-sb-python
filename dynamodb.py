from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_employee(cedula, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-west-2')

    table = dynamodb.Table('Employee')

    try:
        response = table.get_item(Key={'cedula': cedula})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']



employee = get_employee(123)
if employee:
    print("Get employee succeeded:")
    print(employee)
