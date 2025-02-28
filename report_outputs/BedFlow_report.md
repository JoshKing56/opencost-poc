# Kubernetes Cost Optimisation Report for BedFlow

## Total proposed savings for BedFlow: $161.76625

## Application Summary

- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.

- **Business Criticality**: mid

- **Business Owner**: Cassidy Bolton

- **Technical Owner**: Matthew Patterson

- **Server ID**: eusdev39

- **Environments**: 
	 - dev
	- qa
	- prod

## Kubernetes Information
- **Cluster ID**: kc-BedFlow

- **Namespace ID**: ns-make

- **Node ID**: 12:1c:bc:26:03:01

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: bc:72:2f:90:ac:35
- **Ingress**: 105.996939 Bytes/Sec
- **Egress**: 55.345274 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.51045 Bytes
- **Requested RAM**: 309419601 Bytes
- **Allocation CPU**: 0.467151 Bytes
- **Allocation RAM**: 306148356 Bytes
- **Usage CPU**: 0.097424 Bytes
- **Usage RAM**: 43222277 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $85.9934**

### Pod 1
- **Pod ID**: 06:64:e2:83:4d:a6
- **Ingress**: 152.509431 Bytes/Sec
- **Egress**: 121.646579 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.040112 Bytes
- **Requested RAM**: 700495668 Bytes
- **Allocation CPU**: 0.038391 Bytes
- **Allocation RAM**: 521804254 Bytes
- **Usage CPU**: 0.023453 Bytes
- **Usage RAM**: 95712537 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $75.77285**


---
