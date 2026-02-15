# Networking Between Namespace

1. Create two network namespaces with `ip netns`:

  ```bash
  $ sudo ip netns add ns1
  $ sudo ip netns add ns2
  ```

2. Create two veth pairs (`vethA:vethB` and `vethC:vethD`) with `ip link`:

  ```bash
  $ sudo ip link add vethA type veth peer name vethB
  $ sudo ip link add vethC type veth peer name vethD
  ```

3. Attach one end of each of the veth pairs (`vethB` and `vethD`) to a network namespace and assign IP addresses to them:

  ```bash
  $ sudo ip link set vethB netns ns1
  $ sudo ip link set vethD netns ns2
  $ sudo ip netns exec ns1 ip addr add 10.0.0.1/24 dev vethB
  $ sudo ip netns exec ns2 ip addr add 10.0.0.2/24 dev vethD
  ```

4. Create a bridge (`mybridge`) and bring it up:

  ```bash
  $ sudo ip link add mybridge type bridge
  $ sudo ip link set dev mybridge up
  ```

5. Attach the other end of each of the veth pairs (`vethA` and `vethC`) to the bridge:

  ```bash
  $ sudo ip link set vethA master mybridge
  $ sudo ip link set vethC master mybridge
  ```

6. Bring veths up:

    ```bash
    $ sudo ip link set dev vethA up
    $ sudo ip netns exec ns1 ip link set dev vethB up
    $ sudo ip link set dev vethC up
    $ sudo ip netns exec ns2 ip link set dev vethD up
    ```

7. Verify connections with `ping`:

  ```bash
  # vethB -> vethD
  $ sudo ip netns exec ns1 ping -c 4 10.0.0.2
  PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
  64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=0.026 ms
  64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.083 ms
  64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.067 ms
  64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.075 ms

  --- 10.0.0.2 ping statistics ---
  4 packets transmitted, 4 received, 0% packet loss, time 3078ms

  # vethD -> vethB
  $ sudo ip netns exec ns2 ping -c 4 10.0.0.1
  PING 10.0.0.1 (10.0.0.1) 56(84) bytes of data.
  64 bytes from 10.0.0.1: icmp_seq=1 ttl=64 time=0.082 ms
  64 bytes from 10.0.0.1: icmp_seq=2 ttl=64 time=0.118 ms
  64 bytes from 10.0.0.1: icmp_seq=3 ttl=64 time=0.078 ms
  64 bytes from 10.0.0.1: icmp_seq=4 ttl=64 time=0.094 ms

  --- 10.0.0.1 ping statistics ---
  4 packets transmitted, 4 received, 0% packet loss, time 3077ms
  ```

Logic view:

```
[ns1]                           [ns2]
  |                               |
 vethB                          vethD
  |                               |
  +-------+             +---------+
          |             |
        vethA         vethC
          \             /
           +-----------+
           |  mybridge |
           +-----------+
```
