# Kubernetes Cost Optimisation Report for PastConnect

## Application Summary

The aim of this report is to show areas within the PastConnect application which can use cost optimisations 
 TODO Add more stuff here

## Total proposed savings for PastConnect: $66.78139

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

- **Namespace ID**: ns-have

- **Node ID**: 12:07:88:bb:b6:b9

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: 00:54:16:28:08:21
- **Ingress**: 17.378058 Bytes/Sec
- **Egress**: 53.42475 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.856156 Bytes
- **Requested RAM**: 957336298 Bytes
- **Allocation CPU**: 0.534944 Bytes
- **Allocation RAM**: 320258455 Bytes
- **Usage CPU**: 0.006903 Bytes
- **Usage RAM**: 73465817 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $39.63832**

### Pod 1
- **Pod ID**: be:38:4d:18:58:73
- **Ingress**: 141.772424 Bytes/Sec
- **Egress**: 112.960199 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.119231 Bytes
- **Requested RAM**: 275324500 Bytes
- **Allocation CPU**: 0.131221 Bytes
- **Allocation RAM**: 251493656 Bytes
- **Usage CPU**: 0.058812 Bytes
- **Usage RAM**: 39457769 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $27.143069999999998**


---
