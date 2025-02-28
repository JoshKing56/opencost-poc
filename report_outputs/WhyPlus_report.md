# Kubernetes Cost Optimisation Report for WhyPlus

## Application Summary

The aim of this report is to show areas within the WhyPlus application which can use cost optimisations 
 TODO Add more stuff here

## Total proposed savings for WhyPlus: $134.05039

- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.

- **Business Criticality**: high

- **Business Owner**: Jennifer Turner

- **Technical Owner**: Tracy Bauer

- **Server ID**: eusdev25

- **Environments**: 
	 - dev
	- qa
	- prod

## Kubernetes Information
- **Cluster ID**: kc-WhyPlus

- **Namespace ID**: ns-though

- **Node ID**: 14:81:69:a8:ec:0b

## Abandoned Workloads
Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.

### Pod 0
- **Pod ID**: 2c:be:df:6b:7e:5d
- **Ingress**: 22.215455 Bytes/Sec
- **Egress**: 156.066239 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.91826 Bytes
- **Requested RAM**: 681025356 Bytes
- **Allocation CPU**: 0.48564 Bytes
- **Allocation RAM**: 819612571 Bytes
- **Usage CPU**: 0.099411 Bytes
- **Usage RAM**: 29077282 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $20.54532**

### Pod 1
- **Pod ID**: 90:99:69:75:17:3d
- **Ingress**: 37.932277 Bytes/Sec
- **Egress**: 125.618194 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.610045 Bytes
- **Requested RAM**: 636589745 Bytes
- **Allocation CPU**: 0.250098 Bytes
- **Allocation RAM**: 422298625 Bytes
- **Usage CPU**: 0.036462 Bytes
- **Usage RAM**: 21369941 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $8.20015**

### Pod 2
- **Pod ID**: 02:77:3b:ae:0b:9d
- **Ingress**: 166.106663 Bytes/Sec
- **Egress**: 25.827593 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.428891 Bytes
- **Requested RAM**: 801983985 Bytes
- **Allocation CPU**: 0.039304 Bytes
- **Allocation RAM**: 321431873 Bytes
- **Usage CPU**: 0.000427 Bytes
- **Usage RAM**: 67762251 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $43.680139999999994**

### Pod 3
- **Pod ID**: 02:7a:78:d1:57:61
- **Ingress**: 54.250123 Bytes/Sec
- **Egress**: 160.81843 Bytes/Sec
#### Pod Resources
- **Requested CPU**: 0.411601 Bytes
- **Requested RAM**: 192270571 Bytes
- **Allocation CPU**: 0.288548 Bytes
- **Allocation RAM**: 482107228 Bytes
- **Usage CPU**: 0.082003 Bytes
- **Usage RAM**: 55176326 Bytes




 TODO Add the rest of the fields above


**Total Savings Per Pod: $61.62478**


---
