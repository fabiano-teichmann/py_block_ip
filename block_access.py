import iptc


def block(ip):
    rule = iptc.Rule()
    rule.in_interface = "eth0"
    rule.src = "192.168.1.0/255.255.255.0"


# chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
# >>> chain.insert_rule(rule)
# >>> arget = rule.create_target("DROP")
# >>> rule.src = "192.168.25.235"
# >>> target = iptc.Target(rule, "DROP")
# >>> rule.target = target
# >>> chain.insert_rule(rule)
# >>> target = rule.create_target("DROP")
# >>> target
# <iptc.ip4tc.

"""
check path = lambda x, y: True if x in y else False
list(map(check path , paths, path))

"""