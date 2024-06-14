import urllib.parse
def config_to_dict(url,i,singbox_config_orginal):
  """Attempts to extract information from a V2Ray config URL.

  Args:
    url: The V2Ray config URL in string format.

  Returns:
    A dictionary containing extracted information, or None if parsing fails.
  """

  try:
    parsed_url = urllib.parse.urlparse(url)

    # Extract basic information from the path
    server_port = int(parsed_url.path)
    ip_address = parsed_url.scheme

    v2ray_config_dict = {
    "outbounds": 
    [
        {
        "type": "wireguard",
        "tag": "Warp-IR",
        "local_address": [
            "172.16.0.2/32",
            "2606:4700:110:87fd:d3bc:b060:fc17:171d/128"
        ],
        "private_key": "qEqCVqV+l47lp7aSA+9SZDbdWsmE/eyCil8tmEJokGg=",
        "server": ip_address,
        "server_port": server_port,
        "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
        "reserved": "AAAA",
        "mtu": 1280,
        "fake_packets": "5-10"
        },
        {
        "type": "wireguard",
        "tag": "Warp-Main",
        "detour": "Warp-IR",
        "local_address": [
            "172.16.0.2/32",
            "2606:4700:110:8d34:65ad:a0c4:a92:f790/128"
        ],
        "private_key": "sKFNoq7RKGOswUrXKX4b/oEbL31KUD93pGUF4bhgBHM=",
        "server": ip_address,
        "server_port": server_port,
        "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
        "reserved": "AAAA",
        "mtu": 1280,
        "fake_packets": "5-10"
        }
    ]
}
    # Write to JSON file
                
    outbounds_with_tag = [item for item in singbox_config_orginal["outbounds"] if item.get("tag") == v2ray_config_dict["outbounds"][0]["tag"]]
    if not outbounds_with_tag:
        singbox_config_orginal["outbounds"].append(v2ray_config_dict["outbounds"][0])  # Add extracted_info[0] to singbox_config["outbounds"]
        singbox_config_orginal["outbounds"].append(v2ray_config_dict["outbounds"][1])  # Add extracted_info[0] to singbox_config["outbounds"]
    else :
        v2ray_config_dict["outbounds"][0]['tag'] = v2ray_config_dict["outbounds"][0]['tag'] + str(f'_{i}')
        singbox_config_orginal["outbounds"].append(v2ray_config_dict["outbounds"][0])  # Add extracted_info[0] to singbox_config["outbounds"]
        v2ray_config_dict["outbounds"][1]['tag'] = v2ray_config_dict["outbounds"][1]['tag'] + str(f'_{i}')
        v2ray_config_dict["outbounds"][1]['detour'] = v2ray_config_dict["outbounds"][0]['tag']
        singbox_config_orginal["outbounds"].append(v2ray_config_dict["outbounds"][1])  # Add extracted_info[0] to singbox_config["outbounds"]
    return singbox_config_orginal
  except Exception as e:
    print(f"Error parsing URL: {e}")
    return None