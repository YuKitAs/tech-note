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

* **Prerouting and postrouting with NAT (Network Address Translation)**

  ```bash
  # change destination IP from 111.111.0.1 (e.g. gateway public IP) to 10.0.0.2 (e.g. internal IP) before routing (from external)
  $ iptables -t nat -A PREROUTING -p tcp -d 111.111.0.1 --dport 80 -j DNAT --to-destination 10.0.0.2
  # change source IP from 10.0.0.2 to 111.111.0.1 after routing decision has been made (from internal)
  $ iptables -t nat -A POSTROUTING -p tcp -s 10.0.0.2 --sport 80 -j SNAT --to-source 111.111.0.1
  ```

* **Flush existing rules (not default policies)**

  ```bash
  $ iptables -F
  ```

More examples can be found in [Linux iptables command examples for new sysadmins](https://www.cyberciti.biz/tips/linux-iptables-examples.html).
