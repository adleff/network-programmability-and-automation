from jinja2 import Environment, FileSystemLoader

ENV = Environment(lstrip_blocks=True, trim_blocks=True, loader=FileSystemLoader('.'))
template = ENV.get_template("template1.j2")

interface_obj = {'name': 'GigabitEthernet0/1', 'vlan': 10, 'description': 'SERVER', 'uplink': False}

print(template.render(interface=interface_obj))