# Kubernetes Cost Optimisation Report for FullWorks

## Application Summary

The aim of this report is to show areas within the FullWorks application which can use cost optimisations 
 TODO Add more stuff here

## Total proposed savings for FullWorks: $268.88432

- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.

- **Business Criticality**: high

- **Business Owner**: Jason Gonzalez

- **Technical Owner**: Jade Casey

- **Server ID**: eusdev14

- **Environments**: 
	 - dev
	- qa
	- prod

## Kubernetes Information
- **Cluster ID**: kc-FullWorks

- **Namespace ID**: ns-black

- **Node ID**: 98:65:e5:6c:82:97

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: bc:8b:d7:03:2b:b1
- **Ingress**: 106.450588 Bytes/Sec
- **Egress**: 72.591519 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.100303 Bytes
- **Requested RAM**: 440337329 Bytes
- **Allocation CPU**: 0.815429 Bytes
- **Allocation RAM**: 354976656 Bytes
- **Usage CPU**: 0.052953 Bytes
- **Usage RAM**: 83122552 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $94.35200999999999**

### Pod 1
- **Pod ID**: c2:c0:99:bf:f0:05
- **Ingress**: 38.390117 Bytes/Sec
- **Egress**: 137.42731 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.618409 Bytes
- **Requested RAM**: 376117305 Bytes
- **Allocation CPU**: 0.893149 Bytes
- **Allocation RAM**: 517386544 Bytes
- **Usage CPU**: 0.099525 Bytes
- **Usage RAM**: 60346112 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $25.34205**

### Pod 2
- **Pod ID**: be:09:ba:42:01:df
- **Ingress**: 72.716256 Bytes/Sec
- **Egress**: 0.434782 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.845742 Bytes
- **Requested RAM**: 196734842 Bytes
- **Allocation CPU**: 0.111083 Bytes
- **Allocation RAM**: 198998349 Bytes
- **Usage CPU**: 0.009802 Bytes
- **Usage RAM**: 67922285 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $97.78421**

### Pod 3
- **Pod ID**: 20:8f:84:63:7e:11
- **Ingress**: 151.770063 Bytes/Sec
- **Egress**: 88.852151 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.633658 Bytes
- **Requested RAM**: 154546325 Bytes
- **Allocation CPU**: 0.730112 Bytes
- **Allocation RAM**: 395050134 Bytes
- **Usage CPU**: 0.056077 Bytes
- **Usage RAM**: 79469610 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $0.19404000000000002**

### Pod 4
- **Pod ID**: ec:3c:53:24:4b:85
- **Ingress**: 159.247106 Bytes/Sec
- **Egress**: 38.48098 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.381048 Bytes
- **Requested RAM**: 251907094 Bytes
- **Allocation CPU**: 0.687591 Bytes
- **Allocation RAM**: 979299146 Bytes
- **Usage CPU**: 0.046542 Bytes
- **Usage RAM**: 67300691 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $51.21201**


---
