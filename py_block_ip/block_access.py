import iptc


class ControlIptables(object):
    def __init__(self, interface=False, ):

        self.rule = iptc.Rule()
        if interface:
            self.rule.in_interface = interface

    def lock_ip(self, ip, subnet=False):
        """

        Args:
            ip (str):
            subnet (str): Use for blocked range ip

        Returns:
            (bool)
        """
        try:
            chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
            if subnet:
                ip = self.ip_and_subnet(ip, subnet)
            self.rule.src = ip
            target = self.rule.create_target("DROP")
            self.rule.target = target
            chain.insert_rule(self.rule)
            return True

        except Exception as e:
            raise e

    def unlock_ip(self, ip):
        self.rule.src = ip
        target = self.rule.create_target("ACCEPT")
        self.rule.target = target
        self.chain.insert_rule(self.rule)

    def ip_and_subnet(self, ip, subnet):
        """
        Recive ip and apply subnet in ip for block ip and subnets
        Args:
            ip (str): ip
            subnet (str): format example 0/24

        Returns:
            str

        """
        subnet_split = subnet.split('/')
        ip_split = ip.split('.')
        ip = ip_split[:-len(subnet_split[0])]
        ip = ".".join(ip)
        return f"{ip}.{subnet}"
