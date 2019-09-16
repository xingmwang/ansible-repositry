#!/usr/bin/env  python
#coding:utf-8

import sys
import json
import os
import  argparse
try:
    import requests
except ImportError as e:
    print(e.args[0])


# environment = os.getenv("environment")

# if environment is None:
#     raise Exception("没有从系统中获取到environment变量， 请执行export environment=prod|test(001~005) 指定环境")

# host = "http://infra.spacebox.fun"
host = "http://127.0.0.1:8000"

ansible_ssh_user = "root"


class Hosts(object):
    """
    动态获取ansible Inventory
    """
    def __init__(self, host, timeout=5):
        """
        :param timeout： 调用接口超时时间
        """

        # self.environment = environment
        self.host = host.rstrip("/")
        self.timeout = timeout

        # if not self.host.startswith("https://"):
        #     self.host = "https://" + self.host

        self.api_url = self.host + "/api/ansible"

    def data(self):
        d = self.get_hosts_list()
        
        return self.json_format_dict(data=d, pretty=True)

    def get_hosts_list(self):
        """
        Get /api/ansible
        environment： 环境名称
        :return: 组ID列表
        """
        ret = None
        # data = {"environment": environment}
        data = {}
        request = requests.get("{0}".format(self.api_url),params=data, timeout=self.timeout)
        if request.status_code == 200:
            ret = request.json()
            return ret
        else:
            raise Exception("获取接口数据失败， 状态码： %s" %(request.status_code))


    def json_format_dict(self, data, pretty=False):
        ''' Converts a dict to a JSON object and dumps it as a formatted
        string '''
        if pretty:
            return json.dumps(data, sort_keys=True, indent=4, separators=(',',':'))
        else:
            return json.dumps(data)

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

if __name__ == "__main__":
    g = Hosts(host=host)
    print(g.data())
    # print(json.dumps(da, indent=4, separators=(',',':'))
