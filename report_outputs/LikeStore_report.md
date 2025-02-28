# Kubernetes Cost Optimisation Report for LikeStore

## Application Summary

The aim of this report is to show areas within the LikeStore application which can use cost optimisations 
 TODO Add more stuff here

## Total proposed savings for LikeStore: $258.65345

- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.

- **Business Criticality**: high

- **Business Owner**: Barbara Knight

- **Technical Owner**: Sarah Edwards

- **Server ID**: eusdev11

- **Environments**: 
	 - dev
	- qa
	- prod

## Kubernetes Information
- **Cluster ID**: kc-LikeStore

- **Namespace ID**: ns-collection

- **Node ID**: 7c:f1:e6:ad:72:48

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: e0:03:4f:6b:74:4d
- **Ingress**: 188.004894 Bytes/Sec
- **Egress**: 54.159264 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.28916 Bytes
- **Requested RAM**: 242821260 Bytes
- **Allocation CPU**: 0.423311 Bytes
- **Allocation RAM**: 756269390 Bytes
- **Usage CPU**: 0.086547 Bytes
- **Usage RAM**: 56950385 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $81.3539**

### Pod 1
- **Pod ID**: aa:3d:43:80:f6:81
- **Ingress**: 68.772115 Bytes/Sec
- **Egress**: 8.700872 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.628789 Bytes
- **Requested RAM**: 143731758 Bytes
- **Allocation CPU**: 0.664341 Bytes
- **Allocation RAM**: 913781353 Bytes
- **Usage CPU**: 0.035859 Bytes
- **Usage RAM**: 92970181 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $65.33635000000001**

### Pod 2
- **Pod ID**: e8:31:2a:a1:9b:6b
- **Ingress**: 129.558335 Bytes/Sec
- **Egress**: 117.507265 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.334996 Bytes
- **Requested RAM**: 380641420 Bytes
- **Allocation CPU**: 0.783092 Bytes
- **Allocation RAM**: 188515256 Bytes
- **Usage CPU**: 0.09915 Bytes
- **Usage RAM**: 63760074 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $16.44312**

### Pod 3
- **Pod ID**: 32:40:40:2b:35:b7
- **Ingress**: 37.049279 Bytes/Sec
- **Egress**: 57.50861 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.107698 Bytes
- **Requested RAM**: 431161617 Bytes
- **Allocation CPU**: 0.82774 Bytes
- **Allocation RAM**: 427992638 Bytes
- **Usage CPU**: 0.065572 Bytes
- **Usage RAM**: 13165394 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $95.52008000000001**


---
