# DNS Performance Test Script

## About
This Python script evaluates the performance of different public DNS servers by measuring the response times for DNS queries to a pre-defined list of websites.

## Requirements

- Python 3.x
- dns.resolver module

To install the required dns.resolver module, run:

```pip install dnspython```

## Usage

Ensure Python 3 and the dnspython module are installed on your system.

Save the script to a file, for example, main.py.

Run the script using Python:

```python main.py```

The script will test each DNS server in the list with each website and output the average response time.

## How It Works

The script contains a list of websites and a list of public DNS servers.
It measures how long each DNS server takes to resolve each website's domain name.
Finally, it prints the average response time for each DNS server and compares it to the system's default DNS resolver.

## Note

This is a simple script for testing DNS server performance. It might not account for all aspects of DNS server evaluation, such as reliability or security features.
