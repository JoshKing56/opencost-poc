# Kubernetes Cost Optimisation Report for SellHub

## Application Summary

The aim of this report is to show areas within the SellHub application which can use cost optimisations 
 TODO Add more stuff here

## Total proposed savings for SellHub: $8.687190000000001

- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.

- **Business Criticality**: high

- **Business Owner**: Theresa Martin

- **Technical Owner**: Brandon Mcbride Jr.

- **Server ID**: eusdev39

- **Environments**: 
	 - dev
	- qa
	- prod

## Kubernetes Information
- **Cluster ID**: kc-SellHub

- **Namespace ID**: ns-many

- **Node ID**: ba:b6:4b:69:85:02

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: 56:bd:33:6b:3d:b9
- **Ingress**: 2.085566 Bytes/Sec
- **Egress**: 162.621955 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.98549 Bytes
- **Requested RAM**: 136793341 Bytes
- **Allocation CPU**: 0.608403 Bytes
- **Allocation RAM**: 212585040 Bytes
- **Usage CPU**: 0.030645 Bytes
- **Usage RAM**: 76368457 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $8.687190000000001**


---
