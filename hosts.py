#!/usr/bin/env python
# encoding: utf-8

"""
@author: gongxiude
@contact: gongxd
@file: hosts.py 
@time: 2019/9/16 11:10 AM
@description:
"""

import json
import argparse

try:
    from urllib.request import urlopen, Request  # Python 3
except ImportError:
    from urllib2 import urlopen, Request  # Python 2

host = "http://wefocus.example.net"

ansible_ssh_user = "root"


class Hosts(object):
    """
    动态获取ansible Inventory
    """

    def __init__(self, host):
        """
        :param host： 获取ansible资源的接口
        """

        self.host = host.rstrip("/")

        self.api_url = self.host + "/api/ansible"

    def _do_request(self, url, data=None, err_msg="Error", timeout=5):
        try:
            resp = urlopen(
                Request(url, data=data, headers={"Content-Type": "application/json", "User-Agent": "wefocus"}),
                timeout=timeout
            )
            resp_data, code, headers = resp.read().decode("utf8"), resp.getcode(), resp.headers
            resp_data = json.loads(resp_data)
        except Exception as e:
            raise e

        if code not in [200, 201, 204]:
            raise ValueError(
                "{0}:\nUrl: {1}\nData: {2}\nResponse Code: {3}\nResponse: {4}".format(err_msg, url, data, code,
                                                                                      resp_data))
        return resp_data, code, headers

    def data(self):

        d = self.get_hosts_list()

        return self.json_format_dict(data=d, pretty=True)

    def get_hosts_list(self):
        """
        Get /api/ansible
        environment： 环境名称
        :return: 组ID列表
        """
        resp_data, _, _ = self._do_request(self.api_url)
        return resp_data


    def json_format_dict(self, data, pretty=False):
        """
        格式化输出json
        :param data:
        :param pretty:
        :return:
        """
        if pretty:
            return json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
        else:
            return json.dumps(data)

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--host', action='store')
        self.args = parser.parse_args()


if __name__ == "__main__":
    g = Hosts(host=host)
    print(g.data())
