from requests import get, post, put, delete, patch
from datetime import datetime
from time import sleep
#from . import exceptions

"""Honeygain APIs

This tool is designed to integrate Honeygain's
web hook APIs with Python.

With this API, we hope to improve code-writing
efficiency.

The main difference between this API and the
web hooks is that the returned results are
parsed for Python use.

If you have any tips, suggestions, comments,
or questions, please DM me on Discord
@idontknow#4073.

"""

def gen_authcode(email:str, password:str):
    """Requests an authorization token used in the header from Honeygain"""
    requestdata = post(
        "https://dashboard.honeygain.com/api/v1/users/tokens",
        json={
            'email': email,
            'password': password
        }
    ).json()['data']
    return requestdata


def fetch_aboutme(authtoken:str):
    """Fetches information about the current user."""
    requestdata = get(
        "https://dashboard.honeygain.com/api/v1/users/me",
        headers={'authorization': ("Bearer " + authtoken)}
    ).json()['data']
    requestdata['created_at'] = datetime.strptime(requestdata['created_at'].replace('+00:00', 'Z'), "%Y-%m-%dT%H:%M:%SZ")
    return requestdata


def fetch_tosstatus(authtoken:str):
    """Fetches information about the current user's terms of service status."""
    requestdata = get(
        "https://dashboard.honeygain.com/api/v1/users/tos",
        headers={'authorization': ("Bearer " + authtoken)}
    ).json()['data']
    return requestdata


def fetch_trafficstats(authtoken:str):
    """Fetches information about traffic."""
    requestdata = get(
        "https://dashboard.honeygain.com/api/v1/dashboards/traffic_stats",
        headers={'authorization': ("Bearer " + authtoken)}
    ).json()['data']
    for entry in requestdata['traffic_stats']:
        entry['date'] = datetime.strptime(entry['date'], "%Y-%m-%d")
    return requestdata


def fetch_balances(authtoken:str):
    """Fetches information about the current user's balances."""
    requestdata = get(
        "https://dashboard.honeygain.com/api/v1/users/balances",
        headers={'authorization': ("Bearer " + authtoken)}
    ).json()['data']
    return requestdata


def fetch_devices(authtoken:str, deleted:bool=False):
    """Fetches information about the devices and their respective traffic."""
    if deleted == False:
        appendix = '?'
    elif deleted == True:
        appendix = '?deleted=true&'
    devicelist=[]
    request = get(
        "https://dashboard.honeygain.com/api/v1/devices%s" % appendix,
        headers={'authorization': ("Bearer " + authtoken)}
    ).json()
    for device in request['data']:
        devicelist.append(device)
    while request['meta']['pagination']['current_page'] < request['meta']['pagination']['total_pages']:
        request = get(
            "https://dashboard.honeygain.com/api/v1/devices%spage=%i" % (appendix, (request['meta']['pagination']['current_page'] + 1)), 
            headers={'authorization': ("Bearer " + authtoken)}
        ).json()
        for device in request['data']:
            devicelist.append(device)
    return devicelist


def fetch_referrals(authtoken:str):
    """Fetches information about the user's referrals."""
    referrallist=[]
    request = get(
        "https://dashboard.honeygain.com/api/v1/referrals?page=1",
        headers={'authorization': ("Bearer " + authtoken)}
    ).json()
    for referral in request['data']:
        referrallist.append(referral)
    while request['meta']['pagination']['current_page'] < request['meta']['pagination']['total_pages']:
        request = get(
            "https://dashboard.honeygain.com/api/v1/referrals?page=%i" % ((request['meta']['pagination']['current_page'] + 1)), 
            headers={'authorization': ("Bearer " + authtoken)}
        ).json()
        for referral in request['data']:
            referrallist.append(referral)
    return referrallist


def fetch_transactions(authtoken:str):
    """Fetches information about the user's transactions."""
    transactionlist=[]
    request = get(
        "https://dashboard.honeygain.com/api/v1/transactions?page=1",
        headers={'authorization': ("Bearer " + authtoken)}
    ).json()
    for transaction in request['data']:
        transaction['booked_at'] = datetime.strptime(transaction['booked_at'], "%Y-%m-%d %H:%M:%S")
        transaction['created_at'] = datetime.strptime(transaction['created_at'], "%Y-%m-%d %H:%M:%S")
        transactionlist.append(transaction)
    while request['meta']['pagination']['current_page'] < request['meta']['pagination']['total_pages']:
        request = get(
            "https://dashboard.honeygain.com/api/v1/transactions?page=%i" % ((request['meta']['pagination']['current_page'] + 1)), 
            headers={'authorization': ("Bearer " + authtoken)}
        ).json()
        for transaction in request['data']:
            transaction['booked_at'] = datetime.strptime(transaction['booked_at'], "%Y-%m-%d %H:%M:%S")
            transaction['created_at'] = datetime.strptime(transaction['created_at'], "%Y-%m-%d %H:%M:%S")
            transactionlist.append(transaction)
    return transactionlist


def chg_password(authtoken:str, currentPassword:str, newPassword:str):
    """Changes the password of the current user."""
    request = put(
        "https://dashboard.honeygain.com/api/v1/users/passwords",
        headers={'authorization': ("Bearer " + authtoken)},
        json={
            'current_password': currentPassword,
            'new_password': newPassword
        }
    )
    return request.status_code


def chg_devicename(authtoken:str, deviceID:str, newname:str):
    """Changes a device's name as recognized by Honeygain."""
    request = put(
        "https://dashboard.honeygain.com/api/v1/devices/%s/titles" % deviceID,
        headers={'authorization': ("Bearer " + authtoken)},
        json={
            'title': newname
        }
    )
    return request.status_code


def del_device(authtoken:str, deviceID:str):
    """Deletes a device (ie. move it into Removed Devices)."""
    request = delete(
        "https://dashboard.honeygain.com/api/v1/devices/%s" % deviceID,
        headers={'authorization': ("Bearer " + authtoken)}
    )
    return request.status_code


def res_device(authtoken:str, deviceID:str):
    """Restores a device from Removed Devices."""
    request = patch(
        "https://dashboard.honeygain.com/api/v1/devices/%s" % deviceID,
        headers={'authorization': ("Bearer " + authtoken)},
        json={
            'deleted': False
        }
    )
    return request.status_code

