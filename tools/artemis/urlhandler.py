import os
import six
import subprocess

#!/usr/bin/env python
#
# urlhandler.py
#
# This class accepts URLs from the URLReceiver and starts thug
# jobs to investigate

class UrlHandler():
    def __init__(self, url):
        self.url = url
        self._chdir()


    def _chdir(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                              os.pardir,
                                              os.pardir,
                                              'src')))

    def print_url(self):
        print "URL - %s" % self.url

    def runProcess(self, exe):
        p = subprocess.Popen(exe, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        while(True):
            retcode = p.poll()
            line = p.stdout.readline()
            yield line
            if(retcode is not None):
                break

    def process(self):
        """
        Execute thug to process url
        """

        print("Processing: %s" % str(self.url))

        command = ["python", "thug.py", "-F", "-M", str(self.url)]

        print(command)

        pathname = None

        for line in self.runProcess(command):
            if line.startswith("["):
                six.print_(line, end = " ")

            if line.find("] Saving log analysis at ") >= 0:
                pathname = line.split(" ")[-1].strip()
                print "Finished Analysis"

