from msfrpc import MsfRpcClient

# Connect to the Metasploit RPC service
client = MsfRpcClient('your_metasploit_host', port=55552, username='msf', password='msf')

# List available modules
modules = client.modules.exploits
print("Available exploits:")
for module in modules:
    print(module['name'])

# Launch an exploit
exploit = client.modules.use('exploit', 'exploit/path')
exploit['RHOST'] = 'target_ip'
exploit['RPORT'] = 'target_port'

# Execute the exploit
exploit.execute()

# Check for sessions
sessions = client.sessions.list
print("Active sessions:")
for session in sessions:
    print("Session ID: {}, Type: {}, Platform: {}".format(session['sid'], session['type'], session['platform']))
