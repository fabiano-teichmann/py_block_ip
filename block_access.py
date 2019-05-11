import iptc


class ControlIptables(object):
    def __init__(self):
        self.rule = iptc.Rule()
        self.rule.in_interface = "eth0"
        self.chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")

    def lock_ip(self, ip):
        self.rule.src = ip
        target = self.rule.create_target("DROP")
        self.rule.target = target
        self.chain.insert_rule(self.rule)

    def unlock_ip(self, ip):
        self.rule.src = ip
        target = self.rule.create_target("ACCEPT")
        self.rule.target = target
        self.chain.insert_rule(self.rule)
