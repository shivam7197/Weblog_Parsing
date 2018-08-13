

def _parse_weblog_file(filename):                #Function to Parse the weblog.txt file and return different Ip_Addresses 
    
    with open(filename,"r") as f:
        
        lines = f.readlines()  
        
        all_data = []
        for line in lines:
            tokens = line.split(' ')
            data = (tokens[0],tokens[6],tokens[8],tokens[9])
            all_data.append(data)
    return all_data    

def get_unique_ips(filename):                        #Function To Return Unique IP addresses in weblog.txt
    
    ips = _parse_weblog_file(filename)
    unique_ips = []
    
    all_ips = [idx[0] for idx in ips]
    unique_ips = set(all_ips)
    
    
    return unique_ips      
     
def get_urls(filename):

    all_data = _parse_weblog_file(filename)
    urls = []
    urls = [idx[1] for idx in all_data]
    
    return urls      

def get_HTTPcodes(filename):
    
    all_data = _parse_weblog_file(filename)
    http_codes = []
    http_codes = [idx[2] for idx in all_data]
    return http_codes

def get_ips_with_count(filename):                   #Function to return the dictionary of Occurences of IP_Addresses in the text file

    ips = _parse_weblog_file(filename)
    ips_dict = {}
    all_ips = [idx[0] for idx in ips]
    for key in all_ips:
        ips_dict[key] = ips_dict.setdefault(key,0) + 1
            
    return ips_dict

def get_urls_with_count(filename):                   #Function to return the dictionary of Occurences of IP_Addresses in the text file

    urls = _parse_weblog_file(filename)
    urls_dict = {}
    all_urls = [idx[1] for idx in urls]
    for key in all_urls:
        urls_dict[key] = urls_dict.setdefault(key,0) + 1
            
    return urls_dict

def get_distribution_of_HTTPcodes(filename):
    
    http_codes = _parse_weblog_file(filename)
    codes_dict = {}
    all_codes = [idx[2] for idx in http_codes]
    for key in all_codes:
        codes_dict[key] = codes_dict.setdefault(key,0) + 1
            
    return codes_dict    
    
def get_freq_accessed_urls(filename):
    
    urls = _parse_weblog_file(filename)
    urls_accessed_frequently = []
    urls_dict = get_urls_with_count(filename)
    urlValues = list(urls_dict.values())
    max_value = max(urlValues)
    
    
    for key,value in urls_dict.items():
        if urls_dict[key] == max_value:
            urls_accessed_frequently.append(key)

    return urls_accessed_frequently
    
def get_min_occuring_ips(filename):                    #Function that returns list of  IP_Addresses that are accessed MIN times
    
    ips = _parse_weblog_file(filename)
    ips_min_ocurring = []
    ips_dict = get_ips_with_count(filename)
    ipValues = list(ips_dict.values())
    min_value = min(ipValues)
    
    for key,value in ips_dict.items():
        if ips_dict[key] == min_value:
            ips_min_ocurring.append(key)

    return ips_min_ocurring


def get_max_occuring_ips(filename):                    #Function that returns list of  IP_Addresses that are accessed MAX times 
    
    ips = _parse_weblog_file(filename)
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
     
     
     
     unique_ips = get_unique_ips(filename)                #function call to get unique Ip_Addresses 
     print "\nUnique Ip Addresses In The Log File Are :: \n ",unique_ips   
                     
     ips_dict = get_ips_with_count(filename)                #function call to get Ip_Addresses with number of times they occured
     print "\nEach Ip_Address With Its Number Of Occurence in Log File :: \n",ips_dict 
     
     ips_max_occuring = get_max_occuring_ips(filename)            #function call to get Ip Addresses that occured max number of times 
     print "\nIp Addresses That Occurs Maximum Number of Times :: \n",ips_max_occuring
     
     ips_min_occuring = get_min_occuring_ips(filename)            #function call to get Ip Addresses that occured min number of times
     print "\nIp Addresses That Occurs Minimum Number of Times :: \n",ips_min_occuring
      
     urls_accessed_frequently = get_freq_accessed_urls(filename) 
     print "\nURLs Accessed Frequently are ::  \n",urls_accessed_frequently 
     
     codes_dict = get_distribution_of_HTTPcodes(filename)
     print "\nHTTP Response Code Distribution :: \n",codes_dict
