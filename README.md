# 🖥️ **Detailed Guide to Network Automation Using Python**

## **Chapter 1: Setting Up Your Python Environment**

### **1.1 Python Installation**
- Install Python from the official [Python website](https://www.python.org/downloads/).
- Install a virtual environment tool: 
  ```bash
  pip install virtualenv
  ```
  This helps you isolate your project’s dependencies.
- Create and activate a virtual environment:
  ```bash
  virtualenv venv
  source venv/bin/activate   # Linux/Mac
  venv\Scripts\activate      # Windows
  ```

---

## **Chapter 2: Key Python Libraries for Network Automation**

In this chapter, we’ll go through Python libraries commonly used in network automation, their descriptions, use cases, and examples of code.

---

### **2.1 Netmiko**

Netmiko simplifies the process of connecting to network devices using SSH and executing commands. It is particularly useful for automating tasks like retrieving device configuration, making configuration changes, and managing network devices.

#### **2.1.1 Installation:**
```bash
pip install netmiko
```

#### **2.1.2 Key Functions:**
- **`ConnectHandler`**: Establishes an SSH connection to a network device.
- **`send_command()`**: Executes a single command on the device and returns the output.
- **`send_config_set()`**: Sends a series of configuration commands to the device.

#### **2.1.3 Example Script:**
Connecting to a Cisco router and retrieving its running configuration:
```python
from netmiko import ConnectHandler

# Define the device parameters
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password123',
    'secret': 'enablepassword',  # For privileged mode
}

# Establish an SSH connection
connection = ConnectHandler(**device)
connection.enable()  # Enter privileged exec mode

# Send command to retrieve running configuration
output = connection.send_command('show running-config')
print(output)

# Close the connection
connection.disconnect()
```

---

### **2.2 Paramiko**

Paramiko is a lower-level SSH library in Python, providing more control over SSH sessions. While not as high-level as Netmiko, it's useful for advanced automation and when finer control over the SSH process is required.

#### **2.2.1 Installation:**
```bash
pip install paramiko
```

#### **2.2.2 Key Functions:**
- **`SSHClient()`**: Establishes an SSH connection.
- **`exec_command()`**: Executes a command on a remote server.
- **`get_transport()`**: Provides access to the SSH transport layer, useful for tunneling.

#### **2.2.3 Example Script:**
Using Paramiko to connect to a device and execute a command:
```python
import paramiko

# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the device
ssh.connect('192.168.1.1', username='admin', password='password123')

# Execute a command
stdin, stdout, stderr = ssh.exec_command('show ip interface brief')
output = stdout.read().decode()

# Print the command output
print(output)

# Close the connection
ssh.close()
```

---

### **2.3 Napalm**

Napalm (Network Automation and Programmability Abstraction Layer with Multivendor support) abstracts the differences between vendors, providing a single API to manage network devices regardless of their type (e.g., Cisco, Juniper, Arista).

#### **2.3.1 Installation:**
```bash
pip install napalm
```

#### **2.3.2 Key Functions:**
- **`get_facts()`**: Retrieves basic information about the device (uptime, OS version, etc.).
- **`load_merge_candidate()`**: Loads a configuration candidate (intended changes).
- **`commit_config()`**: Commits the configuration changes to the device.

#### **2.3.3 Example Script:**
Using Napalm to retrieve device facts and update configuration:
```python
from napalm import get_network_driver

# Initialize the driver for the device type
driver = get_network_driver('ios')

# Connect to the device
device = driver('192.168.1.1', 'admin', 'password123')
device.open()

# Retrieve and print facts
facts = device.get_facts()
print(facts)

# Load configuration changes
device.load_merge_candidate(config='hostname Router1')
diff = device.compare_config()

# Check if there are changes
if diff:
    print(f"Config changes: {diff}")
    device.commit_config()
else:
    print("No changes needed.")
    
# Close the connection
device.close()
```

---

## **Chapter 3: Advanced Libraries for Specific Use Cases**

### **3.1 PySNMP**

PySNMP is a library for working with SNMP (Simple Network Management Protocol), commonly used for monitoring network devices.

#### **3.1.1 Installation:**
```bash
pip install pysnmp
```

#### **3.1.2 Example Script:**
Retrieve SNMP data from a device:
```python
from pysnmp.hlapi import *

# SNMP GET command to retrieve sysDescr (System Description)
iterator = getCmd(SnmpEngine(),
                  CommunityData('public', mpModel=0),
                  UdpTransportTarget(('192.168.1.1', 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')))

# Process response
for errorIndication, errorStatus, errorIndex, varBinds in iterator:
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print(f'Error: {errorStatus}')
    else:
        for varBind in varBinds:
            print(f'{varBind}')
```

---

### **3.2 Netconf & ncclient**

Netconf is a protocol to manage network devices. **ncclient** is a Python library to interact with devices over Netconf.

#### **3.2.1 Installation:**
```bash
pip install ncclient
```

#### **3.2.2 Key Functions:**
- **`manager.connect()`**: Establishes a connection to the device using Netconf.
- **`get_config()`**: Retrieves configuration from the device.
- **`edit_config()`**: Edits and commits configuration changes.

#### **3.2.3 Example Script:**
```python
from ncclient import manager

# Connect to a Netconf-enabled device
with manager.connect(host='192.168.1.1', port=830, username='admin', password='password123', hostkey_verify=False) as m:
    
    # Retrieve running configuration
    config = m.get_config('running')
    print(config)
    
    # Load and send configuration changes
    config_data = """
    <config>
        <system>
            <hostname>Router1</hostname>
        </system>
    </config>
    """
    m.edit_config(target='running', config=config_data)
```

---

## **Chapter 4: Utility Libraries for Networking Automation**

### **4.1 PyYAML**

An essential library for handling YAML files, which are commonly used in network automation for configuration templates or storing network inventory.

#### **4.1.1 Installation:**
```bash
pip install pyyaml
```

#### **4.1.2 Example Script:**
Loading and parsing a YAML file:
```python
import yaml

# Load YAML data
with open('network_config.yaml') as f:
    data = yaml.safe_load(f)

# Access data
print(data['hostname'])
```

---

### **4.2 Jinja2**

Jinja2 is a templating engine, used to generate configuration files dynamically by feeding data into predefined templates.

#### **4.2.1 Installation:**
```bash
pip install jinja2
```

#### **4.2.2 Example Script:**
Generate configuration from a template:
```python
from jinja2 import Template

# Jinja2 template
template = Template("""
interface {{ interface }}
 ip address {{ ip_address }} {{ subnet_mask }}
""")

# Data to be rendered in the template
data = {
    'interface': 'GigabitEthernet0/1',
    'ip_address': '192.168.1.10',
    'subnet_mask': '255.255.255.0'
}

# Render the template with data
config = template.render(data)
print(config)
```

---

## **Chapter 5: Building a Complete Network Automation Script**

Combining everything from libraries, templating, and configuration management, here's a final, more complex example:

### **5.1 Full Automation Script:**
```python
from netmiko import ConnectHandler
from jinja2 import Template

# Template for interface configuration
template = Template("""
interface {{ interface }}
 ip address {{ ip_address }} {{ subnet_mask }}
 no shutdown
""")

# Define network devices
devices = [
    {'device_type': 'cisco_ios', 'host': '192.168.1.1', 'username': 'admin', 'password': 'pass'},
    {'device_type': 'cisco_ios', 'host': '192.168.1.2', 'username': 'admin', 'password': 'pass