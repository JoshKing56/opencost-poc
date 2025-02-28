# Kubernetes Cost Optimisation Report for DemocraticLink

## Application Summary

The aim of this report is to show areas within the DemocraticLink application which can use cost optimisations 
 TODO Add more stuff here

## Total proposed savings for DemocraticLink: $16.64696

- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.

- **Business Criticality**: mid

- **Business Owner**: Jennifer Martinez

- **Technical Owner**: Mrs. Kristin Peterson DVM

- **Server ID**: eusdev38

- **Environments**: 
	 - dev
	- qa
	- prod

## Kubernetes Information
- **Cluster ID**: kc-DemocraticLink

- **Namespace ID**: ns-similar

- **Node ID**: 6e:ac:99:b4:36:80

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: 64:43:ef:29:f7:a0
- **Ingress**: 55.050777 Bytes/Sec
- **Egress**: 40.955735 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.964384 Bytes
- **Requested RAM**: 521952647 Bytes
- **Allocation CPU**: 0.09052 Bytes
- **Allocation RAM**: 953302335 Bytes
- **Usage CPU**: 0.088778 Bytes
- **Usage RAM**: 75451702 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $16.64696**


---
