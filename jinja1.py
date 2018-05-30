from jinja2 import Environment, FileSystemLoader

ENV = Environment(lstrip_blocks=True, trim_blocks=True,keep_trailing_newline=False, loader=FileSystemLoader('.'))
template = ENV.get_template("template1.j2")

class NetworkInterface(object):

    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10)

print(template.render(interface=interface_obj))