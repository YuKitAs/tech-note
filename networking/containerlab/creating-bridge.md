# Creating Bridge

An example to connect two hosts through a Linux bridge node with [Containerlab](https://containerlab.dev), observe traffic with `tshark`, and inspect or manipulate packets with `scapy`.

1. Define topology with `bridge-lab.yml`:

  ```yaml
  name: bridge-lab

  topology:
    nodes:
      h1:
        kind: linux
        image: ghcr.io/srl-labs/network-multitool
        exec:
          - ip addr add 10.0.0.1/24 dev eth1 # assign IP to interface `eth1` in host 1
          - ip link set eth1 up

      h2:
        kind: linux
        image: ghcr.io/srl-labs/network-multitool
        exec:
          - ip addr add 10.0.0.2/24 dev eth1 # assign IP to interface `eth1` in host 2
          - ip link set eth1 up

      br:
        kind: linux
        image: ghcr.io/srl-labs/network-multitool
        exec:
          - apk add --no-cache bridge # install Linux bridge utilities with Alpine package manager
          - ip link add name br0 type bridge # create a Linux layer-2 bridge device called `br0`
          - ip link set br0 up
          - ip link set eth1 master br0 # add `eth1` to the bridge
          - ip link set eth2 master br0 # add `eth2` to the bridge
          - ip link set eth1 up
          - ip link set eth2 up

    links:
      # create veth (virtual Ethernet) pairs
      - endpoints: ["h1:eth1", "br:eth1"]
      - endpoints: ["h2:eth1", "br:eth2"]
  ```
  Logical view:

  ```
  h1 (10.0.0.1)
    |
  eth1
    |
  br (eth1) -- br0 -- (eth2)
    |
  eth1
    |
  h2 (10.0.0.2)
  ```

  Deploy:

  ```bash
  $ containerlab deploy -t bridge-lab.yml
  ```

  Three container will be running:

  ```
  IMAGE                                PORTS                                                    NAMES
  ghcr.io/srl-labs/network-multitool   22/tcp, 80/tcp, 443/tcp, 1180/tcp, 8080/tcp, 11443/tcp   clab-bridge-lab-h1
  ghcr.io/srl-labs/network-multitool   22/tcp, 80/tcp, 443/tcp, 1180/tcp, 8080/tcp, 11443/tcp   clab-bridge-lab-h2
  ghcr.io/srl-labs/network-multitool   22/tcp, 80/tcp, 443/tcp, 1180/tcp, 8080/tcp, 11443/tcp   clab-bridge-lab-br
  ```

  Note: the `network-multitool` image already includes `ping`, `tshark`, `python3` and `scapy`, so we don't need to install additional packages.

2. Test connectivity with `ping` from host 1 (10.0.0.1) to host 2 (10.0.0.2):

  ```bash
  $ docker exec -it clab-bridge-lab-h1 ping 10.0.0.2
  PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
  64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=0.106 ms
  64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.100 ms
  64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.121 ms
  64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.122 ms
  64 bytes from 10.0.0.2: icmp_seq=5 ttl=64 time=0.131 ms
  ...
  ```

3. Capture traffic with `tshark` from the bridge container while running `ping`:

  ```bash
  $ docker exec -it clab-bridge-lab-br tshark -i br0 [icmp]
  ```

  We should see something like:

  ```
  1 0.000000000     10.0.0.1 → 10.0.0.2     ICMP 98 Echo (ping) request  id=0x0003, seq=5/1280, ttl=64
  2 0.000030808     10.0.0.2 → 10.0.0.1     ICMP 98 Echo (ping) reply    id=0x0003, seq=5/1280, ttl=64 (request in 1)
  3 1.024007841     10.0.0.1 → 10.0.0.2     ICMP 98 Echo (ping) request  id=0x0003, seq=6/1536, ttl=64
  4 1.024076248     10.0.0.2 → 10.0.0.1     ICMP 98 Echo (ping) reply    id=0x0003, seq=6/1536, ttl=64 (request in 3)
  5 1.120168390 aa:c1:ab:f7:87:02 → aa:c1:ab:82:65:df ARP 42 Who has 10.0.0.1? Tell 10.0.0.2
  6 1.120256102 aa:c1:ab:82:65:df → aa:c1:ab:f7:87:02 ARP 42 10.0.0.1 is at aa:c1:ab:82:65:df
  ```

4. Inspect or manipulate packets with `scapy` from the bridge container:

  ```bash
  $ docker exec -it clab-bridge-lab-br python3
  ```

  ```python
  from scapy.all import *

  def handle(pkt):
      pkt.show()

  sniff(iface="br0", prn=handle)
  ```

  ```python
  from scapy.all import *

  send(IP(dst="10.0.0.2")/ICMP())
  ```

5. Cleanup:

  ```bash
  $ containerlab destroy -t bridge-lab.yml
  ```
