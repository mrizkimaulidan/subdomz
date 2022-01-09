#!/usr/bin/env python3
import requests
import sys


def check_arguments(arguments):
    if arguments[1] == '-o':
        return arguments[2], True
    else:
        return arguments[1], False


class Subdomz:
    URL = "https://crt.sh/?Identity={}&output=json"
    RESULT = []

    def __init__(self, url, output_name):
        self.url = url
        self.output_name = output_name

    def fetch(self):
        return requests.get(self.URL.format(self.url)).json()

    def check_duplicate_values(self, response):
        for r in response:
            if r['common_name'] not in self.RESULT:
                self.RESULT.append(r['common_name'])

        return

    def print(self):
        for r in self.RESULT:
            if self.output_name != False:
                self.save_file()

            print(r)

        return

    def save_file(self):
        with open(f'{self.url}.txt', 'w+') as f:
            for r in self.RESULT:
                f.write(f'{r}\n')

        return


if __name__ == '__main__':
    arguments = sys.argv

    if len(arguments) <= 1:
        print('Normal Usage : script.py <domain_url>')
        print('Saving Output : script.py -o <domain_url>')
    else:
        url, is_output = check_arguments(arguments)

        application = Subdomz(url, is_output)
        response = application.fetch()
        application.check_duplicate_values(response)
        application.print()
