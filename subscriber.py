import boto3
import json
import os


LOG_GROUP_FILTER = os.environ['LOG_GROUP_FILTER']
FILTER_NAME = os.environ['FILTER_NAME']
FILTER_PATTERN = os.environ.get('FILTER_PATTERN', ' ')
DESTINATION_ARN = os.environ['DESTINATION_ARN']


def handler(event, context):
    if event['detail']['eventName'] != 'CreateLogGroup':
        print(f"No action on event: {event['detail']['eventName']}")
        return
    print(json.dumps(event))

    log_group_name = event['detail']['requestParameters']['logGroupName']

    if LOG_GROUP_FILTER in log_group_name:
        print(f'Subscribing {log_group_name} to {DESTINATION_ARN}')
        put_subscription_filter(log_group_name)
    else:
        print(f'Skipping subscription for {log_group_name}. ' +
              f'LOG_GROUP_FILTER is {LOG_GROUP_FILTER}')


def put_subscription_filter(log_group_name):
    client = boto3.client('logs')

    response = client.put_subscription_filter(
        logGroupName=log_group_name,
        filterName=FILTER_NAME,
        filterPattern=FILTER_PATTERN,
        destinationArn=DESTINATION_ARN,
        distribution='ByLogStream'
    )
    print(response)
