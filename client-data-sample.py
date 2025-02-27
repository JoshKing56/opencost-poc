from faker import Faker
import random
import json
 
fake = Faker()
 
def generate_fake_node(clusterid):
    return {
        "pod": fake.mac_address(),
        "namespace": fake.word(),
        "node": fake.mac_address(),
        "clusterId": clusterid,
        "clusterName": "",
        "owners": [{"name": fake.word(), "kind": "deployment"}],
        "ingressBytesPerSecond": round(random.uniform(0, 200), 6),
        "egressBytesPerSecond": round(random.uniform(0, 200), 6),
        "allocation": {
            "cpuCores": round(random.uniform(0.01, 1.0), 6),
            "ramBytes": random.randint(100000000, 1000000000)
        },
        "requests": {
            "cpuCores": round(random.uniform(0.01, 1.0), 6),
            "ramBytes": random.randint(100000000, 1000000000)
        },
        "usage": {
            "cpuCores": round(random.uniform(0.0001, 0.1), 6),
            "ramBytes": random.randint(10000000, 100000000)
        },
        "monthlySavings": round(random.uniform(0.01, 10.0), 6)
    }
def generate_fake_client_data(app_name, clusterid):
    return {
        "app_name": app_name,
        "app_id": random.randint(1, 1000),
        "business_criticality": f"{random.choice(['high', 'mid', 'low'])}",
        "business_owner": fake.name(),
        "technical_owner": fake.name(),
        "server_id": f"eusdev{random.randint(1, 40)}",
        "environments": ["dev", "qa", "prod"],
        "clusterId": clusterid
    }
  
# Generate fake data
client_data = []
nodes = []
app_suffixes = ["Flow", "Hub", "Connect", "Link", "Core", "Plus", "Works", "Store", "Tools", "View"]

for _ in range(20):
    app_name = fake.word().capitalize() + random.choice(app_suffixes)
    clusterid = f"kc-{app_name}"
    client_data.append(generate_fake_client_data(app_name, clusterid))
    for _ in range(random.randint(1, 5)):
        nodes.append(generate_fake_node(clusterid))

with open("client-data.json", 'w') as f:
    json.dump(client_data,  f)

with open("nodes.json", 'w') as f:
    json.dump(nodes,  f)