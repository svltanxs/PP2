import json

with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("{:50} {:20}  {:6}  {:6}".format("DN", "Description", "Speed", "MTU"))
print("{:50} {:20}  {:6}  {:6}".format("-" * 50, "-" * 20, "-" * 6, "-" * 6))

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    print("{:50} {:20}  {:6}  {:6}".format(
        attrs["dn"], attrs["descr"], attrs["speed"], attrs["mtu"]
    ))