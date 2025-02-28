import json

# Function to generate markdown report for each application
def generate_markdown_report(application, kubecost_data):
    report = f"# Kubernetes Cost Optimisation Report for {application['app_name']}\n\n"
    report += f"## Application Summary\n\n"
    report += f"The aim of this report is to show areas within the {application['app_name']} application which can use cost optimisations \n TODO Add more stuff here\n\n"

    report += f"- **Description**: Cloud-based enterprise management platform designed to streamline operations, enhance productivity, and foster collaboration across diverse business environments. This robust application integrates advanced tools for project management, resource allocation, workflow automation, and data analytics, providing real-time insights to support informed decision-making.\n\n" 
    report += f"- **Business Criticality**: {application['business_criticality']}\n\n"
    report += f"- **Business Owner**: {application['business_owner']}\n\n"
    report += f"- **Technical Owner**: {application['technical_owner']}\n\n"
    report += f"- **Server ID**: {application['server_id']}\n\n"
    report += f"- **Environments**: \n\n\t - {'\n\t- '.join(application['environments'])}\n"

    report += f"## Kubernetes Information\n"
    report += f"- **Cluster ID**: {application['clusterId']}\n\n"
    report += f"- **Namespace ID**: {kubecost_data[0]['namespace']}\n\n"
    report += f"- **Node ID**: {kubecost_data[0]['node']}\n\n"

    report += f"## Abandoned Workloads\n"
    report += f"Pods that have not sent or received a meaningful rate of traffic over a given duration may represent abandoned workloads. After ensuring that a pod is abandoned, potential remedies include scaling down replicas, deleting, resizing, or notifying their owner.\n\n"
    for index, node in enumerate(kubecost_data):
       report += f"### Pod {index}\n" 
       report += f"- **Pod ID**: {node["pod"]}\n"
       report += f"- **Ingress**: {node["ingressBytesPerSecond"]} Bytes/Sec\n"
       report += f"- **Egress**: {node["egressBytesPerSecond"]} Bytes/Sec\n"
       report += f"- **Ram**: {node["egressBytesPerSecond"]} Bytes/Sec\n"

       report += "\n\n\n\n TODO Add the rest of the fields above\n\n\n"

       report += f"**TOTAL SAVINGS PER MONTH: ${node["monthlySavings"]}**\n\n"
       
    
    report += "\n---\n"
    with open(f"report_outputs/{application["app_name"]}_report.md", 'w') as report_file:
        report_file.write(report)

if __name__ == "__main__":
    app_data_file = 'client-data.json'
    kubecost_file = 'nodes.json'

    MATCH_BY = "clusterId"

    with open(app_data_file, 'r') as f:
        app_data = json.load(f)
    
    with open(kubecost_file, 'r') as f:
        kubecost_data = json.load(f)
    
    print(len(app_data))
    for application in app_data:
        matched_kubecost_data = [item for item in kubecost_data if item[MATCH_BY] == application[MATCH_BY]]
        generate_markdown_report(application, matched_kubecost_data) 

    print("Markdown report has been generated successfully.")
