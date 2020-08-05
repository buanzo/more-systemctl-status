# More-Systemctl-Status

This simple script takes the output of "systemctl status", and when it gets
a PID it runs pstree and get's its children.  Finally, it merges both
outputs into one concise, pstree-like output based on systemd-initiated
processes.

