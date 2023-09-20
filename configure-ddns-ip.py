
from support import *;
import support;
import requests;
import re;
import sys;

public_address = support.from_json(path="config.json")["public_address"];
ddns = support.from_json(path="config.json")["ddns"];

def retrieve_public_address():
    response = requests.get("https://api.myip.com/");
    if response.status_code == 200:
        if re.search("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", response.json()["ip"]):
            public_address["ipv4"] = response.json()["ip"];
        else:
            public_address["ipv6"] = response.json()["ip"];
        logger.info(f"Public address is successfully retrieved through the API. IPv4: \"{public_address['ipv4']}\", IPv6: \"{public_address['ipv6']}\"");
        modify_ddns_ip();
    else:
        logger.critical("Unable to retrieve the public IP.");
        sys.exit(1);

def modify_ddns_ip():
    response = requests.get(f"https://dynupdate.no-ip.com/nic/update?hostname={ddns['hostname']}&myip={public_address['ipv4']},{public_address['ipv6']}", auth=(ddns["username"], ddns["password"]));
    if response.status_code == 200:
        logger.info(f"Public address have been successfully modified for the FQDN \"{ddns['hostname']}\".");
        logger.info(f"DDNS response: {response.text}");
    else:
        logger.critical("Unable to modify the public IP.");
        sys.exit(1);

retrieve_public_address();
