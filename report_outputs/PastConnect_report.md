# Kubernetes Cost Optimisation Report for PastConnect

## Application Summary

The aim of this report is to show areas within the PastConnect application which can use cost optimisations 
 TODO Add more stuff here

- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.

- **Business Criticality**: high

- **Business Owner**: Todd Leach

- **Technical Owner**: Shane Sanders

- **Server ID**: eusdev1

- **Environments**: 

	 - dev
	- qa
	- prod
## Kubernetes Information
- **Cluster ID**: kc-PastConnect

- **Namespace ID**: have

- **Node ID**: 12:07:88:bb:b6:b9

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: 00:54:16:28:08:21
- **Ingress**: 17.378058 Bytes/Sec
- **Egress**: 53.42475 Bytes/Sec
- **Ram**: 53.42475 Bytes/Sec




 TODO Add the rest of the fields above


**TOTAL SAVINGS PER MONTH: $3.963832**

### Pod 1
- **Pod ID**: be:38:4d:18:58:73
- **Ingress**: 141.772424 Bytes/Sec
- **Egress**: 112.960199 Bytes/Sec
- **Ram**: 112.960199 Bytes/Sec




 TODO Add the rest of the fields above


**TOTAL SAVINGS PER MONTH: $2.714307**


---
