# IP Tools
A simple CLI program to help you with configuring your network devices.

## Features
* IP Excluder (_In Progress_)

## IP Excluder
This program can exclude an IP or a subnet from a larger network specified. The syntax for performing exclusion is as follows:
```
sudo python3 ip-tools.py -excluder -s [starting subnet] -e [IP or subnet to be excluded]
```
Note: _IP address or subnet should be in CIDR notation._
