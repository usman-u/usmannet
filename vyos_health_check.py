from net_automation import net_automation

vyos = net_automation.Vyos(
    "edge.dn42.lan",
    "test",
    "test",
    False,
    "",
    "",
)
vyos.init_ssh()
print ("----------------------")
print (vyos.get_version())
print ("----------------------")
print ("INTERFACES")
print ("----------------------")
print (vyos.get_interfaces())
print ("----------------------")
print ("BGP")
print ("----------------------")
print (vyos.get_bgp_neighbors())