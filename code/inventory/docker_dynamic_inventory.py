#!/usr/bin/python3
# Python3 file for detecting the docker container dynamically and putting them all in a single webserver grop
import subprocess
import json
from os.path import expanduser



def executeDockerCommand(*args):
    return subprocess.check_output(["docker"] + list(args)).strip()



def docker_inspect(fmt, mcn):
    published_host = executeDockerCommand("inspect", "-f", fmt, mcn).split()
    return published_host[0].decode('utf-8')



def get_host_vars(m):
    home = expanduser("~")
    ip = [docker_inspect("{{.NetworkSettings.IPAddress}}", m)]
    hostConnectionDetails = {"hosts": ip}
    return hostConnectionDetails

class DockerInventory():
      def __init__(self):
          self.inventory = {} # Ansible Inventory
          machines = executeDockerCommand("ps", "-q").splitlines()
          json_data = {'webserver':{'hosts':[] }} # putting all in webserver group
          for m in machines :
              json_data['webserver']['hosts'].append(get_host_vars(m.decode("utf-8"))['hosts'][0])
          print ( json.dumps(json_data,indent=4,sort_keys=True) )
          
        
DockerInventory()
