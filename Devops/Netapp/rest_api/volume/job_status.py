#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from netapp_storage_info import username, password, mgmt_ip
import requests


def status_job(mgmtip, username, password, job_uuid, type_name):
    job_url = f"https://{mgmt_ip}/api/cluster/jobs/{job_uuid}"
    job_response = requests.get(job_url, auth=(username, password), verify=False)
    job_status = job_response.json()['state']
    print(f'{type_name} modify {job_status}.')

