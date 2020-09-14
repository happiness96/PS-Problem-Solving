# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 14                             | #
# | 6324 URLs                          | #
# -------------------------------------- #


if __name__ == "__main__":
    n = int(r_input())

    for step in range(1, n + 1):
        URL = r_input().rstrip()

        ind = URL.index('://')
        protocol, host = URL[: ind], URL[ind + 3:]
        port = ''
        path = ''

        if '/' in host:
            ind = host.index('/')
            host, path = host[: ind], host[ind:]

            if len(path) == 1:
                path = ''
            
            else:
                path = path[1:]
        
        if ':' in host:
            host, port = map(str, host.split(':'))

        if not port:
            port = '<default>'
        
        if not path:
            path = '<default>'
        
        print('URL #' + str(step))
        print('Protocol =', protocol)
        print('Host     =', host)
        print('Port     =', port)
        print('Path     =', path)
        print()
