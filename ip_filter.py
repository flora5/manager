import yaml
import socket, time

PORT = 8800
TIMEOUT = 0.1

def remove(fliter, IP):
        for k in fliter.keys():
            if IP in fliter[k]:
                fliter[k].remove(IP)
        stream = file('Conf/fliter.yaml', 'w')
        yaml.dump(fliter, stream)
        stream.close()
def ipFliter():
    tmp_ip_trash = []
    stream = file('Conf/timeup_ips.yaml', 'r')
    cmdinfo = yaml.load(stream)
    fliter = cmdinfo
    ip_list = []
    for v in fliter.values():
        ip_list = ip_list + v[:-2]
    ip_list = list(set(ip_list))
    for HOST  in ip_list:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        try:
            s.connect((HOST, PORT))
        except:
            tmp_ip_trash.append(HOST)
            remove(fliter, HOST)
    stream = file('Conf/tmp_ip_trash.yaml', 'w')
    counter = yaml.dump(tmp_ip_trash, stream)
    stream.close()



# after 20 minute
def add_ip_back():
    stream = file('Conf/tmp_ip_trash.yaml', 'r')
    ip_trash = yaml.load(stream)
    stream.close()
    
    
    stream = file('Conf/timeup_ips.yaml', 'r')
    timeup_ips = yaml.load(stream)
    stream.close()
    
    
    stream = file('Conf/fliter.yaml', 'r')
    fliter = yaml.load(stream)
    stream.close()
    
    for ip in ip_trash:
        for k in timeup_ips.keys():
            if ip in timeup_ips[k]:
                fliter[k].insert(0, ip)
                
   
ipFliter()



    

