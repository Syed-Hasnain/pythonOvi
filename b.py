#!/usr/bin/python
import commands
import os

fcportcCHeckPath = '/usr/local/libexec/fcportcheck.pl -n -v'
whitelistPath    = '/usr/local/etc/'
cmd = commands.getoutput

pod = raw_input('please enter the pod name: ')
dc = os.environ.get('HOSTNAME').split('-')[3].split('.')[0]
#dc  = 'ops-bastion1-1-tyo.ops.sfdc.net'

#def serverList(podName):
#       serverNames = []
#       for i in range(1,15):
#               serverNames.append( pod +'-db1-'+ str(i) +'-' + dc ) 
#       return serverNames


def getports(server):
        ports = []
        a = cmd('ssh -t ' + server + " ' " 'sudo /usr/local/libexec/fcportcheck.pl -n -v ' " '")
        for i in sorted(a.split()):
                if i.startswith('VMAX'):
                        ports.append(i[:-1])
        		with open('fcportcheck.whitelist', 'w') as f:
        			for items in ports:
                		f.write('\n' + items)
                	f.close()
        		print "file creating in ", server , 'done'

serverList = 'ops-stgmgt1-1-sfm'
getports(serverList)







