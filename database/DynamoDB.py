#!/usr/bin/env python

import os
import boto3
import requests


class DynamoDBDao:
    def __init__(self, table):
        self.ddb = boto3.resource('dynamodb', )
        self.table = table

    def listTables(self):
        pass


if __name__ == '__main__':
    cwd = os.path.dirname(__file__)
    print(cwd)
    profile = 'debug' if True else 'default'
    print("profile is %s" % profile)

    resps = requests.get('https://www.google.com')
    print(resps.status_code)