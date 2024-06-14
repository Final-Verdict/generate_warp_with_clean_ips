import subprocess
import json
import os
import random
from write_config_to_json import write_json_config , append_diff_to_json
from config_to_dict import config_to_dict
from scanner import ip_scanner
from get_ips import get_and_remove_first_ip_port
from github import Github
# Example usage
v2ray_url = None
first_ip_port = None
def upload_to_github():
                g = Github('your github token')
                user = g.get_user()
                repo = g.get_repo(f"{user.login}/sharefile")
                fileContents = repo.get_contents("")
                # Upload to github
                with open("config.json", 'r' , encoding="utf8") as file:
                    data = file.read()
                repo.update_file(fileContents[0].path, "committing files", data, fileContents[0].sha, branch='main')
                print(f'{fileContents[0].download_url}' + ' UPDATED')


i = 1
for i in range(1 ,10):
            
            with open('hiddifyguard2.json', 'r') as file:
                    singbox_config_orginal = json.load(file)

            #ip_scanner()
            while not first_ip_port :
            
                first_ip_port = get_and_remove_first_ip_port('result.csv')

                if first_ip_port:
                    v2ray_url = first_ip_port
                else:
                    ip_scanner()

            
            #with open('config.txt', 'r',encoding='utf-8') as file:
                #for line in file:
                    #if line.startswith("vless"):

            #v2ray_url = line.strip()  # Assuming the link is the entire line
            singbox_config_orginal = config_to_dict(v2ray_url,i,singbox_config_orginal)
            first_ip_port = None
            #singbox_config = singbox_config_orginal
            if singbox_config_orginal:
            # Adapt extracted_info to Singbox format (if possible)
                

                '''# Write to JSON file
                
                outbounds_with_tag = [item for item in singbox_config["outbounds"] if item.get("tag") == extracted_info[0]["outbounds"][0]["tag"]]
                if not outbounds_with_tag:
                    singbox_config["outbounds"].append(extracted_info[0]["outbounds"][0])  # Add extracted_info[0] to singbox_config["outbounds"]
                else :
                    extracted_info[0]["outbounds"][0]['tag'] = extracted_info[0]["outbounds"][0]['tag'] + str(f'_{i}')
                    singbox_config["outbounds"].append(extracted_info[0]["outbounds"][0])  # Add extracted_info[0] to singbox_config["outbounds"]'''

                if os.path.exists('config.json'):
                        with open('config.json', 'r') as file:
                            singbox_config_last = json.load(file)

                        singbox_config_last["outbounds"].extend(singbox_config_orginal["outbounds"][len(singbox_config_orginal["outbounds"])-2:])
                        
                        write_json_config(singbox_config_last, "config.json")

                else :
                    write_json_config(singbox_config_orginal, "config.json")
                
            else:
                print("Failed to extract information.")
upload_to_github()