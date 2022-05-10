#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from Devops.Netapp.rest_api.netapp_storage_info import username, password, mgmt_ip
import requests
import re


def status_job(job_uuid, type_name):
    job_url = f"https://{mgmt_ip}/api/cluster/jobs/{job_uuid}"
    job_response = requests.get(job_url, auth=(username, password), verify=False)
    job_status = job_response.json()['state']
    print(f'{type_name} execute {job_status}.')
    # print(job_response.json()['message'])
    # print(job_response.json()['description'])

    start_time = re.match(r'(\d{4}-\d{2}-\d{2})\w(\d{2}:\d{2}:\d{2})', str(job_response.json()['start_time']))
    end_time = re.match(r'(\d{4}-\d{2}-\d{2})\w(\d{2}:\d{2}:\d{2})', str(job_response.json()['end_time']))
    print(f'start: {start_time.group(1)}-{start_time.group(2)}')
    print(f'end  : {end_time.group(1)}-{end_time.group(2)}')

