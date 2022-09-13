from net_automation import net_automation

# net_automation.EdgeOS.deploy_yaml("configs/erx-zahid-lan.yml")
# net_automation.Cisco_IOS.deploy_yaml("configs/2960-usman-lan.yml")
# net_automation.EdgeOS.deploy_yaml("configs/erx-usman-lan.yml")
net_automation.Vyos.deploy_yaml("configs/edge-dn42-lan.yml")
# net_automation.Vyos.deploy_yaml("edge-ca-dn42-lan.yml")

print ("Diagnostics:")
edge = net_automation.Vyos(
    "vyos",
    "edge.dn42.lan",
    "test",
    "test",
    False,
    "",
)

print (edge.init_ssh())
print ("----------------- Interfaces -----------------")
print (edge.get_interfaces())
print ("----------------- BGP Neighb -----------------")
print (edge.get_bgp_neighbors())