from urllib2 import Request, urlopen, URLError
import yaml
import os


class linodeClient:

    key = None

    def __init__(self, configFile):
        f = open (configFile)
        config = yaml.load(f)
        self.key = config['key']

    def call(self, url):
        request = Request(url)
        try:
            response = urlopen(request)
            data = response.read()
            return data
        except URLError, e:
            print("Uh oh, something went horribly wrong...")
            return None

    def createLinode(self, DatacenterID, plan):
        request = self.call('https://api.linode.com/?api_key=' + self.key + '&api_action=linode.create&DatacenterID=' + DatacenterID + '&PlanID=' + plan)

    def destroyLinode(self, linode):
        request = self.call('https://api.linode.com/?api_key=' + self.key + '&api_action=linode.delete&LinodeID=' + linode)
