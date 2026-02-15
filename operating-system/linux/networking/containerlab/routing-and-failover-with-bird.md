# Routing and Failover with BIRD

[BIRD](https://bird.network.cz/) is an internet routing daemon that implements dynamic routing protocols such as BGP (Border Gateway Protocol) and OSPF (Open Shortest Path First), and manages routing decisions on a system. It consists of `bird` which is a service process that runs the BIRD daemon and `birdc` which is a command-line control client used to monitor and configure a running BIRD instance.

Here is a minimal BGP example using Containerlab and BIRD to demonstrate routing and failover behavior between 3 routers.

1. Define topology with `bird-lab.yml`:

  ```yaml
  name: bird-lab

  topology:
    nodes:
      r1:
        kind: linux
        image: debian:12
        exec:
          - apt update
          - apt install -y bird2 iproute2
          - ip addr add 10.0.12.1/24 dev eth1
          - ip addr add 10.0.13.1/24 dev eth2
          - ip link set eth1 up
          - ip link set eth2 up
          - ip addr add 1.1.1.1/32 dev lo
        binds:
          - ./r1-bird.conf:/etc/bird/bird.conf

      r2:
        kind: linux
        image: debian:12
        exec:
          - apt update
          - apt install -y bird2 iproute2
          - ip addr add 10.0.12.2/24 dev eth1
          - ip addr add 10.0.23.2/24 dev eth2
          - ip link set eth1 up
          - ip link set eth2 up
          - ip addr add 2.2.2.2/32 dev lo
        binds:
          - ./r2-bird.conf:/etc/bird/bird.conf

      r3:
        kind: linux
        image: debian:12
        exec:
          - apt update
          - apt install -y bird2 iproute2
          - ip addr add 10.0.13.3/24 dev eth1
          - ip addr add 10.0.23.3/24 dev eth2
          - ip link set eth1 up
          - ip link set eth2 up
          - ip addr add 3.3.3.3/32 dev lo
        binds:
          - ./r3-bird.conf:/etc/bird/bird.conf

    links:
      - endpoints: ["r1:eth1", "r2:eth1"]
      - endpoints: ["r2:eth2", "r3:eth2"]
      - endpoints: ["r1:eth2", "r3:eth1"]
  ```

  Logical view (r1 can reach r3 either directly or via r2):

  ```
     r2
    /  \
  r1 — r3
  ```

  Configurations on the host:

  `r1-bird.conf` for r1:
  ```
  log syslog all;

  router id 1.1.1.1;

  protocol device {}

  protocol kernel {
    persist;
    scan time 20;
    ipv4 {
      export all;
    };
  }

  protocol static {
    ipv4;
    route 1.1.1.1/32 via "lo";
  }

  protocol bgp r2 {
    local as 65001;
    neighbor 10.0.12.2 as 65002;
    ipv4 {
      import all;
      export all;
    };
  }

  protocol bgp r3 {
    local as 65001;
    neighbor 10.0.13.3 as 65003;
    ipv4 {
      import all;
      export all;
    };
  }
  ```

  `r2-bird.conf` for r2:

  ```
  router id 2.2.2.2;

  protocol device {}

  protocol kernel {
    persist;
    scan time 20;
    ipv4 {
      export all;
    };
  }

  protocol static {
    ipv4;
    route 2.2.2.2/32 via "lo";
  }

  protocol bgp r1 {
    local as 65002;
    neighbor 10.0.12.1 as 65001;
    ipv4 {
      import all;
      export all;
    };
  }

  protocol bgp r3 {
    local as 65002;
    neighbor 10.0.23.3 as 65003;
    ipv4 {
      import all;
      export all;
    };
  }
  ```

  `r3-bird.conf` for r3:

  ```
  router id 3.3.3.3;

  protocol device {}

  protocol kernel {
    persist;
    scan time 20;
    ipv4 {
      export all;
    };
  }

  protocol static {
    ipv4;
    route 3.3.3.3/32 via "lo";
  }

  protocol bgp r1 {
    local as 65003;
    neighbor 10.0.13.1 as 65001;
    ipv4 {
      import all;
      export all;
    };
  }

  protocol bgp r2 {
    local as 65003;
    neighbor 10.0.23.2 as 65002;
    ipv4 {
      import all;
      export all;
    };
  }
  ```

  Deploy:

  ```bash
  $ containerlab deploy -t bird-lab.yml
  ```

  Three containers will be running for each router: `clab-bird-lab-r1`, `clab-bird-lab-r2` and `clab-bird-lab-r3`.

2. Start BIRD in all containers:

  ```bash
  docker exec -it clab-bird-lab-r1 service bird start
  docker exec -it clab-bird-lab-r2 service bird start
  docker exec -it clab-bird-lab-r3 service bird start
  ```

3. Show routes from r1 to r3, the direct route should be preferred:

  ```bash
  $ docker exec -it clab-bird-lab-r1 birdc show route 3.3.3.3/32
  BIRD 2.0.12 ready.
  Table master4:
  3.3.3.3/32           unicast [r3 17:33:54.539] * (100) [AS65003i]
  	via 10.0.13.3 on eth2
                       unicast [r2 17:33:54.539] (100) [AS65003i]
  	via 10.0.12.2 on eth1
  ```

4. Simulate link failure between r1 and r3:

  ```bash
  $ docker exec -it clab-bird-lab-r1 ip link set eth2 down
  ```

5. Verify route from r1 and r3 again, it should go via r2 now:

  ```bash
  $ docker exec -it clab-bird-lab-r1 birdc show route 3.3.3.3/32
  BIRD 2.0.12 ready.
  Table master4:
  3.3.3.3/32           unicast [r2 17:33:54.539] * (100) [AS65003i]
    via 10.0.12.2 on eth1
  ```
