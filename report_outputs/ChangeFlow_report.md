# Kubernetes Cost Optimisation Report for ChangeFlow

## Application Summary

The aim of this report is to show areas within the ChangeFlow application which can use cost optimisations 
 TODO Add more stuff here

- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.

- **Business Criticality**: high

- **Business Owner**: Nicole Sanchez

- **Technical Owner**: Ricky Williams

- **Server ID**: eusdev11

- **Environments**: 

	 - dev
	- qa
	- prod
## Kubernetes Information
- **Cluster ID**: kc-ChangeFlow

- **Namespace ID**: few

- **Node ID**: 76:ad:a0:ba:e3:1b

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: 9a:1a:a5:05:88:e4
- **Ingress**: 35.257551 Bytes/Sec
- **Egress**: 12.54887 Bytes/Sec
- **Ram**: 12.54887 Bytes/Sec




 TODO Add the rest of the fields above


**TOTAL SAVINGS PER MONTH: $9.642054**

### Pod 1
- **Pod ID**: a2:74:b2:da:7c:2f
- **Ingress**: 7.745052 Bytes/Sec
- **Egress**: 103.890389 Bytes/Sec
- **Ram**: 103.890389 Bytes/Sec




 TODO Add the rest of the fields above


**TOTAL SAVINGS PER MONTH: $1.949138**

### Pod 2
- **Pod ID**: 0a:f4:08:69:6c:41
- **Ingress**: 77.713639 Bytes/Sec
- **Egress**: 54.439263 Bytes/Sec
- **Ram**: 54.439263 Bytes/Sec




 TODO Add the rest of the fields above


**TOTAL SAVINGS PER MONTH: $9.420945**


---
