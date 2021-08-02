import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter')

def lambda_handler(event, context):

    response = table.get_item(Key= {'id' : 'currentcount'} )

    count = response["Item"]["numberofvisits"]
    print("Get Response = ", response)
    print( "Count = ", count)

    # increment string version of visit count
    new_count = str(int(count)+1)
    response = table.update_item(
        Key={'id': 'currentcount'},
        UpdateExpression='set numberofvisits = :c',
        ExpressionAttributeValues={':c': new_count},
        ReturnValues='UPDATED_NEW'
        )

    return {
        'view count': new_count + ' views.'
    }
