# Traffic Control with `qdisc`

QDisc (Queueing Discipline) is the packet scheduler attached to a network interface, which determines traffic shaping (the rate at which packets are transmitted) and scheduling (the order and timing of packet transmission). It primarily works on egress (outgoing traffic from the host to the NIC), because on ingress (incoming traffic to the host) packets have already arrived and can only be dropped, marked or redirected to an intermediate queue for further processing.

Rate limit traffic with `tc qdisc`:

```bash
$ tc qdisc add dev eth0 root handle 1: tbf rate 1mbit burst 32kbit latency 400ms
```

This queue discipline is added as the root qdisc (`handle 1:` is the identifier). It attaches a Token Bucket Filter (TBF) to `eth0` with the following TBF parameters:

* `rate`: average allowed transmission rate
* `burst`: maximum amount of data that can be sent at once before rate limiting kicks in
* `latency`: maximum time a packet is allowed to wait in the queue before it gets dropped
