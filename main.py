from net_automation import net_automation

# net_automation.EdgeOS.deploy_yaml_now("configs/erx-zahid-lan.yml")
net_automation.EdgeOS.deploy_yaml_now("configs/erx-usman-lan.yml")
net_automation.Cisco_IOS.deploy_yaml_now("configs/2960-usman-lan.yml")
# net_automation.Vyos.deploy_yaml_now("configs/edge-dn42-lan.yml")
# net_automation.Vyos.deploy_yaml("edge-ca-dn42-lan.yml")
