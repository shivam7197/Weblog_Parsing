

def _parse_weblog_file_forips(filename):                #Function to Parse the weblog.txt file and return different Ip_Addresses 
    
    with open(filename,"r") as f:
        
        lines = f.readlines()  
        
        all_data = []
        for line in lines:
            tokens = line.split(' ')
            data = (tokens[0],tokens[6],tokens[8],tokens[9])
            all_data.append(data)
    return all_data    


def get_unique_ips(filename):                        #Function To Return Unique IP addresses in weblog.txt
    
    ips = _parse_weblog_file_forips(filename)
    unique_ips = []
    
    all_ips = [idx[0] for idx in ips]
    unique_ips = set(all_ips)
    return unique_ips      
     
    
def get_ips_with_count(filename):                   #Function to return the dictionary of Occurences of IP_Addresses in the text file

    ips = _parse_weblog_file_forips(filename)
    ips_dict = {}
    all_ips = [idx[0] for idx in ips]
    for key in all_ips:
        ips_dict[key] = ips_dict.setdefault(key,0) + 1
            
    return ips_dict


def get_min_occuring_ips(filename):                    #Function that returns list of  IP_Addresses that are accessed MIN times
    
    ips = _parse_weblog_file_forips(filename)
    ips_min_ocurring = []
    ips_dict = get_ips_with_count(filename)
    ipValues = list(ips_dict.values())
    min_value = min(ipValues)
    
    for key,value in ips_dict.items():
        if ips_dict[key] == min_value:
            ips_min_ocurring.append(key)

    return ips_min_ocurring


def get_max_occuring_ips(filename):                    #Function that returns list of  IP_Addresses that are accessed MAX times 
    
    ips = _parse_weblog_file_forips(filename)
    ips_max_occuring = []
    ips_dict = get_ips_with_count(filename)
    ipValues = list(ips_dict.values())
    max_value = max(ipValues)
    
    for key,value in ips_dict.items():
        if ips_dict[key] == max_value:
            ips_max_occuring.append(key)
            
    return ips_max_occuring

    
if __name__ == "__main__":

     filename = "weblog.txt"
     
     
     data = _parse_weblog_file_forips(filename)
     #print data
     
     unique_ips = get_unique_ips(filename)                #function call to get unique Ip_Addresses 
     print "\nUnique Ip Addresses In The Log File Are :: \n ",unique_ips   
     
     ips_dict = get_ips_with_count(filename)                #function call to get Ip_Addresses with number of times they occured
     print "\n\nEach Ip_Address With Its Number Of Occurence in Log File :: \n",ips_dict 
     
     ips_max_occuring = get_max_occuring_ips(filename)            #function call to get Ip Addresses that occured max number of times 
     print "\nIp Addresses That Occurs Maximum Number of Times :: \n",ips_max_occuring
     
     ips_min_occuring = get_min_occuring_ips(filename)            #function call to get Ip Addresses that occured min number of times
     print "\nIp Addresses That Occurs Minimum Number of Times :: \n",ips_min_occuring
      
      
      
      
