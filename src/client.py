from urllib2 import Request, urlopen, URLError
import yaml
import os
import json

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
        return request

    def destroyLinode(self, linode):
        request = self.call('https://api.linode.com/?api_key=' + self.key + '&api_action=linode.delete&LinodeID=' + linode)
        return request

    def createFromDistro(self, linode, distro, label, size, rootPass):
        request = self.call('https://api.linode.com/?api_key=' + self.key + '&api_action=linode.disk.createfromdistribution&LinodeID=' + linode + '&DistributionID=' + distro + '&Label=' + label + '&Size=' + size + '&rootPass=' + rootPass)
        return request

    def createDisk(self, linode, label, size, diskType):
        request = self.call('https://api.linode.com/?api_key=' + self.key + '&api_action=linode.disk.create&LinodeID=' + linode + '&Label=' + label + '&Type=' + diskType + '&Size=' + size)
        return request

    def createConfig(self, linode, label, diskList, kernelID='138', comments='', RAMLimit='0', virt_mode='paravirt', runLevel='default', rootDeviceNum='1', rootDeviceCustom='', rootDeviceRO='true', helper_disableUpdateDB='true', helper_distro='true', helper_xen='true', helper_depmod='true', helper_network='true', devtmpfs_automount='true'):

        diskList = ",".join(map(str, diskList))

        #this is fugly as deadpool
        request = self.call('https://api.linode.com/?api_key=' + self.key + '&api_action=linode.config.create&LinodeID=' + linode + '&Label=' + label + '&KernelID=' + kernelID + '&Comments=' + comments + '&RAMLimit=' + RAMLimit + '&DiskList=' + diskList + '&virt_mode=' + virt_mode + '&RunLevel=' + runLevel + '&RootDeviceNum=' + rootDeviceNum + '&RootDeviceCustom=' + rootDeviceCustom + '&RootDeviceRO=' + rootDeviceRO + '&helper_disableUpdateDB=' + helper_disableUpdateDB + '&helper_distro=' + helper_distro + '&helper_xen=' + helper_xen + '&helper_depmod=' + helper_depmod + '&helper_network=' + helper_network + '&devtmpfs_automount=' + devtmpfs_automount)

        return request

    def boot(self, linode):
        request = self.call('https://api.linode.com/?api_key=' + self.key + '&api_action=linode.boot&LinodeID=' + linode)
        return request

    def reboot(self, linode):
        request = self.call('https://api.linode.com/?api_key=' + self.key + '&api_action=linode.reboot&LinodeID=' + linode)
        return request

    def shutdown(self, linode):
        request = self.call('https://api.linode.com/?api_key=' + self.key + '&api_action=linode.shutdown&LinodeID=' + linode)
        return request

    def listDisks(self, linode):
        request = self.call('https://api.linode.com/?api_key=' + self.key + '&api_action=linode.disk.list&LinodeID=' + linode)
        dump = json.loads(request)
        return dump

    def deleteDisk(self, linode, diskid):
        request = self.call('https://api.linode.com/?api_key=' + self.key + '&api_action=linode.disk.delete&LinodeID=' + linode + '&DiskID=' + diskid)
        return request
