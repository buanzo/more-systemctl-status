#!/usr/bin/env python3
# Author: Arturo 'Buanzo' Busleiman
# This script takes the output from "systemctl status"
# and for each PID it finds, it recursively adds its children, if any
#
# BTW, I did not find any special output-format args for systemctl
# status. I know this works on Ubuntu 18.x and 20.x and that's it.
# YMMV
import subprocess

__version__ = '0.1.0'

class MoreSystemctlStatus():
    def __init__(self,split=True,
                 systemctl="systemctl"):
        self.systemctl = systemctl
        self.split = split
        self.status = self.get_status()
        self.output = self.enhance_status()

    def get_status(self):
        s = subprocess.check_output([self.systemctl, "status"],
                                    universal_newlines=True).split('\n')
        return(s)

    def enhance_status(self):
        new_output = []
        for item in self.status:
            pid = self.get_pid(item)
            if pid is None:
                new_output.append(item)
            else:
                # More data needs the line before its shown
                new_output.append(item)
                # We use the PID in the line to calculate padding
                padding = item.index(str(pid)) 
                new_output.extend(self.get_pstree(pid, padding))
        if self.split:
            return(new_output)
        else:
            return('\n'.join(new_output))

    def get_pstree(self,pid,padding):
        # pstree -haltp PID
        r = []
        s = subprocess.check_output(['pstree', '-haltp', str(pid)],
                                    universal_newlines=True).split('\n')[1:]
        for item in s:
            if item == '':
                continue
            x = f'{" ":>{padding}}{item}'
            r.append(x)
        return(r)

    def get_pid(self,item):
        for mark in ['├─', '└─']:
            try:
                a = item.split(mark)[1]
                s = a.split(' ')[0].strip()
            except IndexError:
                continue
            if s.isnumeric():
                return(int(s))
        return(None)

def run():
    # by default MoreSystemctlStatus returns a list with no \n
    # except when run from cli directly:
    mss = MoreSystemctlStatus(split=False).output
    print(mss)

if __name__ == '__main__':
    run()
