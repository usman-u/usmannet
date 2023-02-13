from net_automation import net_automation

net_automation.Vyos.deploy_yaml("configs/fr-lil1-usman-dn42.yml", True)
net_automation.Vyos.deploy_yaml("configs/us-ca1-usman-dn42.yml", True)