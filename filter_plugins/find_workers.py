#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'find_buildbot_workers': self.find_buildbot_workers,
        }

    def find_buildbot_workers(self, hostvars, master_name):
        result = []
        for i in hostvars:
          for j in i.get('value').get('apps').items():
            if j[1].get('buildbot_worker',{}).get('configs',{}).get('master',{}).get('app_name') == master_name:
                result.append(i.get('key') + '-' + j[0])
        return result
