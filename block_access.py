import iptc


class ControlIptables(object):
    def __init__(self, interface=False):
        self.rule = iptc.Rule()
        if interface:
            self.rule.in_interface = interface
        self.chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")

    def lock_ip(self, ip, subnet=False):
        if subnet:
            ip = subnet
        self.rule.src = ip
        target = self.rule.create_target("DROP")
        self.rule.target = target
        self.chain.insert_rule(self.rule)

    def unlock_ip(self, ip):
        self.rule.src = ip
        target = self.rule.create_target("ACCEPT")
        self.rule.target = target
        self.chain.insert_rule(self.rule)

    def ip_and_subnet(self, ip, subnet):
        subnet_split = subnet.split('/')
        ip_split = ip.split('.')
        ip = ip_split[:-len(subnet_split[0])]
        ip = ".".join(ip)
        return f"{ip}.{subnet}"
