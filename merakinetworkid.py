#!/usr/bin/python

#imports
import requests
import json
import sys

#Import the CRED module from a separate directory
sys.path.insert(0,'../CRED')
import cred


#custom variables for the program imported from the cred.py file located in the same directory
organization = cred.organization
key = cred.key
hub = cred.hub

#Main URL for the Meraki Platform
dashboard = "https://dashboard.meraki.com"
#api token and other data that needs to be uploaded in the header
headers = {'X-Cisco-Meraki-API-Key': (key), 'Content-Type': 'application/json'}

#variables for testing ***** Need to switch to an argument or something else
store = input("What store do you want the network id for? ")

#pull back all of the networks for the organization
get_network_url = dashboard + '/api/v0/organizations/%s/networks' % organization

#request the network data
get_network_response = requests.get(get_network_url, headers=headers)

#puts the data into json format
get_network_json = get_network_response.json()

#pull back the network_id of the store that you are configuring
for i in get_network_json:
    if i["name"] == str(store):
        network_id=(i["id"])
print("\n")
print("The network id for store %s is %s") % (store, network_id)
print("\n")
