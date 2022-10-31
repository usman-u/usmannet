from net_automation import net_automation
import time

net_automation.EdgeOS.deploy_yaml("configs/erx-zahid-lan.yml")
# net_automation.Cisco_IOS.deploy_yaml("configs/2960-usman-lan.yml")
net_automation.EdgeOS.deploy_yaml("configs/erx-usman-lan.yml")
# net_automation.Vyos.deploy_yaml("configs/edge-dn42-lan.yml")
# net_automation.Vyos.deploy_yaml("edge-ca-dn42-lan.yml")

def verify_cicso_switchports():
    ciscosw = net_automation.Cisco_IOS(
        device_type = "cisco_ios",
        host = "2960-usman-lan",
        username = "test",
        password = "test",
    )
    ciscosw.init_ssh()
    print (ciscosw.custom_command("sh vlan"))
    print (ciscosw.custom_command("sh ip int desc"))



def verify_dn42_peerings():
    print ("Diagnostics:")
    edge = net_automation.Vyos(
        device_type = "vyos",
        host = "edge.dn42.lan",
        username = "test",
        password = "test",
    )

    print (edge.init_ssh())
    print ("----------------- Interfaces -----------------")
    print (edge.get_interfaces())
    time.sleep(15)
    print ("----------------- BGP Neighb -----------------")


    print (edge.custom_command("sudo wg"))

    print (edge.run_ping("172.23.0.53", 5))


# verify_cicso_switchports()