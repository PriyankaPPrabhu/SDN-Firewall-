# SDN-Firewall-
Implementation of SDN controlled and managed dynamic Firewall functions in an application-/service-specific manner 

# Problem statement
To defend the network from Internet-based attacks that can interrupt the service operating on the internal network.

# Importance
Software-defined networking (SDN) is a means of controlling networks that separates the control plane from the forwarding plane. This is done by using software to administer network functions from a centralized control point. With two types of equipment, SDN specifically advocates: (1) controllers implementing the control plane and (2) switches performing data plane operations. The existing standard by which controllers and switches can communicate with one another is the OpenFlow protocol (OFP). Using OpenFlow, by handling Flow Table entries, SDN controllers can handle SDN turn forwarding behaviors. To forward packets to suitable hosts, switches use these low-level Flow Table entries. But the main concern today is privacy and security and to secure the network from unauthorized access. A firewall is a mechanism that secures incoming network packets coming from different sources as well as outgoing network packets. It can track and manage the flow of data coming from various sources to the network and operates based on predefined laws.

# Firewall
In this repository I have creating an SDN topology using VirtualBox and Mininet that would be consisting of an RYU controller, OpenvSwitch, and 4 hosts. Firewall Application will be installed at the controller level the Firewall Application is used for blocking the ICMP and TCP firewall rules.

The project main focus would be to implement an Inefficient Stateless Firewall, Efficient Stateless Firewall, Inefficient Stateful Firewall and Efficient Stateful Firewall.

Stateful:-The Stateful Firewall uses attributes to monitor the packets that pass through it. These attributes include IP addresses, port numbers and sequence numbers for the source and destination.

Stateless:-Stateless Firewall, simply tests each packet with Firewall rules and decides whether the packet is permitted to pass through. Stateless Firewall implements traditional firewalls that only search each arriving packet. No states, such as Stateful Firewall, are maintained. That is, the ongoing connection is not monitored. Instead, it simply takes each packet as an entity and attempts to verify the packet with the firewall rules provided.

Efficient Application:- In Efficient Firewall it stores the flow table entries on the switch, this application uses flow tables so that packets from that flow will not be forwarded to the controller next time. Based on Flow table entries, the switch will make decisions to forward or reject the packet to the appropriate port. 

Inefficient Application:- In Inefficient Firewall, there is no comprehensive storage of flow table entries on the switch. Instead, the switch is simply made to forward everything to the controller. 

# Architecture
<img width="915" alt="Project Image" src="https://user-images.githubusercontent.com/57679558/101070620-93a78680-3569-11eb-928b-89e922914301.png">

# Prerequisites
You have to first install mininet http://mininet.org/download/ and RYU controller https://ryu-sdn.org/ package

# 
