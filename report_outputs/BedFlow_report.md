# Kubernetes Cost Optimisation Report for BedFlow

## Application Summary

The aim of this report is to show areas within the BedFlow application which can use cost optimisations 
 TODO Add more stuff here

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

- **Namespace ID**: make

- **Node ID**: 12:1c:bc:26:03:01

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: bc:72:2f:90:ac:35
- **Ingress**: 105.996939 Bytes/Sec
- **Egress**: 55.345274 Bytes/Sec
- **Ram**: 55.345274 Bytes/Sec




 TODO Add the rest of the fields above


**TOTAL SAVINGS PER MONTH: $8.59934**

### Pod 1
- **Pod ID**: 06:64:e2:83:4d:a6
- **Ingress**: 152.509431 Bytes/Sec
- **Egress**: 121.646579 Bytes/Sec
- **Ram**: 121.646579 Bytes/Sec




 TODO Add the rest of the fields above


**TOTAL SAVINGS PER MONTH: $7.577285**


---
