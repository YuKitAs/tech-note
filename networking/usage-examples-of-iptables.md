# Usage Examples of `iptables`

* **Allow all traffic except from a source IP**

  ```bash
  # set default policy to accept all
  $ iptables -P FORWARD ACCEPT
  # append a rule to block traffic from 10.0.0.1
  $ iptables -A FORWARD -s 10.0.0.1 -j DROP
  ```

* **Block all traffic except to a destination port**

  ```bash
  # set default policy to drop all
  $ iptables -P FORWARD DROP
  # append a rule to allow TCP traffic to port 80
  $ iptables -A FORWARD -p tcp --dport 80 -j ACCEPT
  ```

* **Prerouting with NAT (Network Address Translation)**

  ```bash
  # change destination IP from 10.0.0.2 to 10.0.0.3 before routing
  $ iptables -t nat -A PREROUTING -p tcp -d 10.0.0.2 --dport 80 -j DNAT --to-destination 10.0.0.3
  ```

* **Flush existing rules (not default policies)**

  ```bash
  $ iptables -F
  ```
