# Kubernetes Cost Optimisation Report for TreePlus

## Application Summary

The aim of this report is to show areas within the TreePlus application which can use cost optimisations 
 TODO Add more stuff here

- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.

- **Business Criticality**: high

- **Business Owner**: David Page

- **Technical Owner**: Angel Ramos

- **Server ID**: eusdev15

- **Environments**: 

	 - dev
	- qa
	- prod
## Kubernetes Information
- **Cluster ID**: kc-TreePlus

- **Namespace ID**: hot

- **Node ID**: f6:4e:17:b3:00:55

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: 3a:66:96:00:b1:24
- **Ingress**: 117.195062 Bytes/Sec
- **Egress**: 68.785526 Bytes/Sec
- **Ram**: 68.785526 Bytes/Sec




 TODO Add the rest of the fields above


**TOTAL SAVINGS PER MONTH: $4.763338**


---
