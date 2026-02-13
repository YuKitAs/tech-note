# Load Balancing with IPVS

IPVS (IP Virtual Server) is a Linux kernel framework for layer-4 load balancing. `ipvsadm` is a command-line tool used to configure and manage IPVS rules.

Suppose a topology consisting of an external host, a gateway with IP address 111.111.0.1, and two internal hosts with IP addresses 10.10.0.2 and 10.10.0.3.

Add a TCP virtual service on the gateway as the public entry point with **round-robin** scheduler:

```bash
$ ipvsadm -A -t 111.111.0.1:80 -s rr
```

Then add two backend servers to the existing virtual service on the gateway using **masquerading** mode:

```bash
$ ipvsadm -a -t 111.111.0.1:80 -r 10.10.0.2:8000 -m
$ ipvsadm -a -t 111.111.0.1:80 -r 10.10.0.3:8000 -m
```

On the internal hosts, use netcat to listen on port 8000 and return a distinct response:

```bash
# on 10.10.0.2
$ while true; do echo "Backend 1" | nc -l -p 8000; done
# on 10.10.0.3
$ while true; do echo "Backend 2" | nc -l -p 8000; done
```

On the external host, verify that the connection alternates between the two internal hosts:

```bash
$ nc -v 111.111.0.1 80
```
