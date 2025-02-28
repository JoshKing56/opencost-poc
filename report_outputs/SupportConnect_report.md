# Kubernetes Cost Optimisation Report for SupportConnect

## Application Summary

The aim of this report is to show areas within the SupportConnect application which can use cost optimisations 
 TODO Add more stuff here

## Total proposed savings for SupportConnect: $151.42119

- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.

- **Business Criticality**: mid

- **Business Owner**: Brittany Phillips

- **Technical Owner**: Joseph Hughes

- **Server ID**: eusdev38

- **Environments**: 
	 - dev
	- qa
	- prod

## Kubernetes Information
- **Cluster ID**: kc-SupportConnect

- **Namespace ID**: ns-always

- **Node ID**: 04:0a:30:18:7a:32

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: 16:2d:87:ff:5a:a0
- **Ingress**: 119.789467 Bytes/Sec
- **Egress**: 36.037515 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.982102 Bytes
- **Requested RAM**: 365440667 Bytes
- **Allocation CPU**: 0.609677 Bytes
- **Allocation RAM**: 442955869 Bytes
- **Usage CPU**: 0.009389 Bytes
- **Usage RAM**: 60756481 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $45.493880000000004**

### Pod 1
- **Pod ID**: 2e:f1:1e:44:7c:94
- **Ingress**: 125.060529 Bytes/Sec
- **Egress**: 145.613689 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.746799 Bytes
- **Requested RAM**: 802991592 Bytes
- **Allocation CPU**: 0.27472 Bytes
- **Allocation RAM**: 511585114 Bytes
- **Usage CPU**: 0.088165 Bytes
- **Usage RAM**: 17230550 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $70.83779**

### Pod 2
- **Pod ID**: 16:8e:76:68:5f:20
- **Ingress**: 186.122023 Bytes/Sec
- **Egress**: 7.330917 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.469311 Bytes
- **Requested RAM**: 700167971 Bytes
- **Allocation CPU**: 0.282522 Bytes
- **Allocation RAM**: 563583052 Bytes
- **Usage CPU**: 0.007697 Bytes
- **Usage RAM**: 49473109 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $35.08952**


---
