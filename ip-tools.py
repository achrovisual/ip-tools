import argparse
from ipaddress import ip_network
from threading import Thread

def exclude_ips(start, exclude):
    result = [ip_network(start)]
    for x in exclude:
        n = ip_network(x)
        new = []
        for y in result:
            if y.overlaps(n):
                new.extend(y.address_exclude(n))
            else:
                new.append(y)
        result = new

    print(', '.join(str(x) for x in sorted(result)))

def main():
    parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)

    ip_excluder_group = parser.add_argument_group('IP Excluder')
    ip_excluder_group.add_argument('-excluder', '--excluder', action = 'store_true')
    ip_excluder_group.add_argument('-s', '--s', help = 'Starting IP or subnet in CIDR notation')
    ip_excluder_group.add_argument('-e', '--e', help = 'IP or subnet to be excluded in CIDR notation')

    args = parser.parse_args()

    if args.excluder:
        start = str(args.s)
        exclude = (args.e).split(',')

        exclude_ips(start, exclude)

if __name__ == "__main__":
    try:
        t = Thread(target = main)
        t.daemon = True
        t.start()
        t.join()
    except KeyboardInterrupt as e:
        sys.exit(0)
