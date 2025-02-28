# Kubernetes Cost Optimisation Report for CenturyWorks

## Application Summary

The aim of this report is to show areas within the CenturyWorks application which can use cost optimisations 
 TODO Add more stuff here

## Total proposed savings for CenturyWorks: $272.5422

- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.

- **Business Criticality**: mid

- **Business Owner**: Richard Smith

- **Technical Owner**: Laurie Wright

- **Server ID**: eusdev39

- **Environments**: 
	 - dev
	- qa
	- prod

## Kubernetes Information
- **Cluster ID**: kc-CenturyWorks

- **Namespace ID**: ns-near

- **Node ID**: b0:03:89:50:20:f9

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: 72:e1:04:bd:fb:be
- **Ingress**: 41.424317 Bytes/Sec
- **Egress**: 102.243359 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.251238 Bytes
- **Requested RAM**: 270144679 Bytes
- **Allocation CPU**: 0.534001 Bytes
- **Allocation RAM**: 845767914 Bytes
- **Usage CPU**: 0.045944 Bytes
- **Usage RAM**: 40501668 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $41.30057**

### Pod 1
- **Pod ID**: 12:66:af:00:b1:4d
- **Ingress**: 13.579332 Bytes/Sec
- **Egress**: 27.408627 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.635121 Bytes
- **Requested RAM**: 908553756 Bytes
- **Allocation CPU**: 0.688439 Bytes
- **Allocation RAM**: 272221639 Bytes
- **Usage CPU**: 0.006751 Bytes
- **Usage RAM**: 47253745 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $82.24976**

### Pod 2
- **Pod ID**: 74:b1:4c:d5:d8:e0
- **Ingress**: 117.025792 Bytes/Sec
- **Egress**: 196.815894 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.470184 Bytes
- **Requested RAM**: 997823951 Bytes
- **Allocation CPU**: 0.121383 Bytes
- **Allocation RAM**: 996101065 Bytes
- **Usage CPU**: 0.017552 Bytes
- **Usage RAM**: 48862500 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $81.71524**

### Pod 3
- **Pod ID**: 54:dd:21:8c:83:1c
- **Ingress**: 33.707636 Bytes/Sec
- **Egress**: 102.186274 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.851284 Bytes
- **Requested RAM**: 737865721 Bytes
- **Allocation CPU**: 0.660731 Bytes
- **Allocation RAM**: 949388422 Bytes
- **Usage CPU**: 0.080068 Bytes
- **Usage RAM**: 64090154 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $67.27663**


---
