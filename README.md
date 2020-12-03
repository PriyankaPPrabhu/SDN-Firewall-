# SDN-Firewall-
Implementation of SDN controlled and managed dynamic Firewall functions in an application-/service-specific manner 

# Problem statement
To defend the network from Internet-based attacks that can interrupt the service operating on the internal network.

# Importance
Software-defined networking (SDN) is a means of controlling networks that separates the control plane from the forwarding plane. This is done by using software to administer network functions from a centralized control point. With two types of equipment, SDN specifically advocates: (1) controllers implementing the control plane and (2) switches performing data plane operations. The existing standard by which controllers and switches can communicate with one another is the OpenFlow protocol (OFP). Using OpenFlow, by handling Flow Table entries, SDN controllers can handle SDN turn forwarding behaviors. To forward packets to suitable hosts, switches use these low-level Flow Table entries. But the main concern today is privacy and security and to secure the network from unauthorized access. A firewall is a mechanism that secures incoming network packets coming from different sources as well as outgoing network packets. It can track and manage the flow of data coming from various sources to the network and operates based on predefined laws.

