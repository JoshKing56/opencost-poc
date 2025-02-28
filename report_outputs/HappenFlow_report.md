# Kubernetes Cost Optimisation Report for HappenFlow

## Application Summary

The aim of this report is to show areas within the HappenFlow application which can use cost optimisations 
 TODO Add more stuff here

## Total proposed savings for HappenFlow: $264.64529

- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.

- **Business Criticality**: low

- **Business Owner**: John Johnson

- **Technical Owner**: Melissa Brown

- **Server ID**: eusdev18

- **Environments**: 
	 - dev
	- qa
	- prod

## Kubernetes Information
- **Cluster ID**: kc-HappenFlow

- **Namespace ID**: ns-foot

- **Node ID**: cc:bf:c7:ce:aa:83

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: a4:c2:42:e7:70:df
- **Ingress**: 95.246934 Bytes/Sec
- **Egress**: 95.667557 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.103158 Bytes
- **Requested RAM**: 782938288 Bytes
- **Allocation CPU**: 0.703098 Bytes
- **Allocation RAM**: 867881832 Bytes
- **Usage CPU**: 0.078739 Bytes
- **Usage RAM**: 23121956 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $66.52392**

### Pod 1
- **Pod ID**: 1c:31:67:a9:ff:ed
- **Ingress**: 61.893575 Bytes/Sec
- **Egress**: 9.155309 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.233115 Bytes
- **Requested RAM**: 358807409 Bytes
- **Allocation CPU**: 0.052214 Bytes
- **Allocation RAM**: 496152570 Bytes
- **Usage CPU**: 0.079143 Bytes
- **Usage RAM**: 29233933 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $80.89621**

### Pod 2
- **Pod ID**: 62:be:4b:20:d3:a7
- **Ingress**: 113.151855 Bytes/Sec
- **Egress**: 181.31668 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.789425 Bytes
- **Requested RAM**: 957181065 Bytes
- **Allocation CPU**: 0.990132 Bytes
- **Allocation RAM**: 651651507 Bytes
- **Usage CPU**: 0.04553 Bytes
- **Usage RAM**: 49454232 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $83.25229**

### Pod 3
- **Pod ID**: 4c:c2:cd:72:fc:c4
- **Ingress**: 78.338311 Bytes/Sec
- **Egress**: 156.338687 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.883877 Bytes
- **Requested RAM**: 458038209 Bytes
- **Allocation CPU**: 0.09773 Bytes
- **Allocation RAM**: 759912106 Bytes
- **Usage CPU**: 0.05914 Bytes
- **Usage RAM**: 51677170 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $20.136319999999998**

### Pod 4
- **Pod ID**: 14:da:e1:35:5b:de
- **Ingress**: 52.227029 Bytes/Sec
- **Egress**: 11.726638 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.186895 Bytes
- **Requested RAM**: 859829437 Bytes
- **Allocation CPU**: 0.574714 Bytes
- **Allocation RAM**: 214841606 Bytes
- **Usage CPU**: 0.009631 Bytes
- **Usage RAM**: 48055374 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $13.83655**


---
