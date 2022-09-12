from net_automation import net_automation

# net_automation.EdgeOS.deploy_yaml("configs/erx-zahid-lan.yml")
# net_automation.Cisco_IOS.deploy_yaml("configs/2960-usman-lan.yml")
# net_automation.EdgeOS.deploy_yaml("configs/erx-usman-lan.yml")
net_automation.Vyos.deploy_yaml("configs/edge-dn42-lan.yml")
# net_automation.Vyos.deploy_yaml("edge-ca-dn42-lan.yml")

print ("Diagnostics:")
edge = net_automation.Vyos(
    "edge.dn42.lan",
    "usman",
    "",
    True,
    r"c:\Users\Usman\.ssh\id_rsa",
)

edge = net_automation.Vyos()

print (edge.init_ssh())
print (edge.get_bgp_neighbors())
print (edge.get_interfaces())