from random_user_agent.params import SoftwareName, HardwareType
from random_user_agent.user_agent import UserAgent
import requests as rq
import urllib3, json
from fp.fp import FreeProxy 

#TELEGRAM BOT CHECKER EA SNKRS COUNTRY IT
#By Dimitrino#0126

#proxy_obj = FreeProxy(rand=True) // leave comment for enable proxy

software_names = [SoftwareName.CHROME.value]
hardware_type = [HardwareType.MOBILE__PHONE]
user_agent_rotator = UserAgent(software_names=software_names, hardware_type=hardware_type)
urllib3.disable_warnings()

headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en;q=0.9',
        'appid': 'com.nike.commerce.snkrs.web',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'nike-api-caller-id': 'nike:snkrs:web:1.0',
        'origin': 'https://www.nike.com',
        'referer': 'https://www.nike.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': user_agent_rotator.get_random_user_agent()
    }
#proxy = {'http': proxy_obj.get()} // leave comment for enable proxy

def ea_us():
    url  = "https://api.nike.com/product_feed/threads/v2/?anchor=1&count=100&filter=marketplace%28US%29&filter=language%28en%29&filter=inStock%28false%29&filter=productInfo.merchPrice.discounted%28false%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29&fields=active&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.nodes&fields=publishedContent.properties.coverCard&fields=publishedContent.properties.productCard&fields=publishedContent.properties.products&fields=publishedContent.properties.publish.collections&fields=publishedContent.properties.relatedThreads&fields=publishedContent.properties.seo&fields=publishedContent.properties.threadType&fields=publishedContent.properties.custom"
    items = []
    first = 0
    sizes = ''
    html = rq.get(url=url, timeout=20, verify=False, headers=headers) # add proxies=proxy for enable proxy
    output = json.loads(html.text)
    status = html.status_code
    for item in output['objects']:
        items.append(item)
    PRIMO = "FALSE"
    for item in items:
        for j in item['productInfo']:
            if j['merchProduct']['exclusiveAccess'] == True and PRIMO != "TRUE":
                code = j['merchProduct']['styleColor']
                title=j['productContent']['fullTitle']
                url='https://www.nike.com/' + 'it' + '/launch/t/' + j['productContent']['slug']
                img = j['imageUrls']['productImageUrl']
                status =j['merchProduct']["status"]
                PRIMO = "TRUE" 
                for k in j['availableSkus']:
                    item = [j['productContent']['fullTitle'], j['productContent']['colorDescription'], k['id']]  
                    for s in j['skus']:
                        if first == 0:
                            if s['id'] == k['id']:
                                sizes = str(s['nikeSize']) + ': ' + str(k['level'])
                                first = 1
                        else:
                            if s['id'] == k['id']:
                                sizes += '\n' + str(s['nikeSize']) + ': ' + str(k['level'])
                dataus = f"⚠ ULTIMO EA CARICATO : {title}\n{url}\n{img}\nStatus : {status}\nSTOCK:\n{sizes}"
    return dataus

def ea1():
    url  = "https://api.nike.com/product_feed/threads/v2/?anchor=1&count=100&filter=marketplace%28IT%29&filter=language%28it%29&filter=inStock%28false%29&filter=productInfo.merchPrice.discounted%28false%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29&fields=active&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.nodes&fields=publishedContent.properties.coverCard&fields=publishedContent.properties.productCard&fields=publishedContent.properties.products&fields=publishedContent.properties.publish.collections&fields=publishedContent.properties.relatedThreads&fields=publishedContent.properties.seo&fields=publishedContent.properties.threadType&fields=publishedContent.properties.custom"
    items = []
    first = 0
    sizes = ''
    html = rq.get(url=url, timeout=20, verify=False, headers=headers) # add proxies=proxy for enable proxy
    output = json.loads(html.text)
    status = html.status_code
    for item in output['objects']:
        items.append(item)
    PRIMO = "FALSE"
    for item in items:
        for j in item['productInfo']:
            if j['merchProduct']['exclusiveAccess'] == True and PRIMO != "TRUE":
                code = j['merchProduct']['styleColor']
                title=j['productContent']['fullTitle']
                url='https://www.nike.com/' + 'it' + '/launch/t/' + j['productContent']['slug']
                img = j['imageUrls']['productImageUrl']
                status =j['merchProduct']["status"]
                PRIMO = "TRUE" 
                for k in j['availableSkus']:
                    item = [j['productContent']['fullTitle'], j['productContent']['colorDescription'], k['id']]  
                    for s in j['skus']:
                        if first == 0:
                            if s['id'] == k['id']:
                                sizes = str(s['nikeSize']) + ': ' + str(k['level'])
                                first = 1
                        else:
                            if s['id'] == k['id']:
                                sizes += '\n' + str(s['nikeSize']) + ': ' + str(k['level'])
                data = f"⚠ ULTIMO EA CARICATO : {title}\n{url}\n{img}\nStatus : {status}\nSTOCK:\n{sizes}"
    return data

def ea2():
    url  = "https://api.nike.com/product_feed/threads/v2/?anchor=1&count=100&filter=marketplace%28IT%29&filter=language%28it%29&filter=inStock%28false%29&filter=productInfo.merchPrice.discounted%28false%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29&fields=active&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.nodes&fields=publishedContent.properties.coverCard&fields=publishedContent.properties.productCard&fields=publishedContent.properties.products&fields=publishedContent.properties.publish.collections&fields=publishedContent.properties.relatedThreads&fields=publishedContent.properties.seo&fields=publishedContent.properties.threadType&fields=publishedContent.properties.custom"
    items = []
    first = 0
    sizes = ''
    html = rq.get(url=url, timeout=20, verify=False, headers=headers) # add proxies=proxy for enable proxy
    output = json.loads(html.text)
    status = html.status_code
    for item in output['objects']:
        items.append(item)
    PRIMO = 0
    for item in items:
        for j in item['productInfo']:
            if j['merchProduct']['exclusiveAccess'] == True and PRIMO != 2:
                code = j['merchProduct']['styleColor']
                title=j['productContent']['fullTitle']
                url='https://www.nike.com/' + 'it' + '/launch/t/' + j['productContent']['slug']
                img = j['imageUrls']['productImageUrl']
                status =j['merchProduct']["status"]
                PRIMO = PRIMO + 1 
                if PRIMO ==2:
                    for k in j['availableSkus']:
                        item = [j['productContent']['fullTitle'], j['productContent']['colorDescription'], k['id']]  
                        for s in j['skus']:
                            if first == 0:
                                if s['id'] == k['id']:
                                    sizes = str(s['nikeSize']) + ': ' + str(k['level'])
                                    first = 1
                            else:
                                if s['id'] == k['id']:
                                    sizes += '\n' + str(s['nikeSize']) + ': ' + str(k['level'])
                data = f"⚠ ULTIMO EA CARICATO : {title}\n{url}\n{img}\nStatus : {status}\nSTOCK:\n{sizes}"
    return data

def ea3():
    url  = "https://api.nike.com/product_feed/threads/v2/?anchor=1&count=100&filter=marketplace%28IT%29&filter=language%28it%29&filter=inStock%28false%29&filter=productInfo.merchPrice.discounted%28false%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29&fields=active&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.nodes&fields=publishedContent.properties.coverCard&fields=publishedContent.properties.productCard&fields=publishedContent.properties.products&fields=publishedContent.properties.publish.collections&fields=publishedContent.properties.relatedThreads&fields=publishedContent.properties.seo&fields=publishedContent.properties.threadType&fields=publishedContent.properties.custom"
    items = []
    first = 0
    sizes = ''
    html = rq.get(url=url, timeout=20, verify=False, headers=headers) # add proxies=proxy for enable proxy
    output = json.loads(html.text)
    status = html.status_code
    for item in output['objects']:
        items.append(item)
    PRIMO = 0
    for item in items:
        for j in item['productInfo']:
            if j['merchProduct']['exclusiveAccess'] == True and PRIMO != 4:
                code = j['merchProduct']['styleColor']
                title=j['productContent']['fullTitle']
                url='https://www.nike.com/' + 'it' + '/launch/t/' + j['productContent']['slug']
                img = j['imageUrls']['productImageUrl']
                status =j['merchProduct']["status"]
                PRIMO = PRIMO + 1
                if PRIMO == 4: 
                    for k in j['availableSkus']:
                        item = [j['productContent']['fullTitle'], j['productContent']['colorDescription'], k['id']]  
                        for s in j['skus']:
                            if first == 0:
                                if s['id'] == k['id']:
                                    sizes = str(s['nikeSize']) + ': ' + str(k['level'])
                                    first = 1
                            else:
                                if s['id'] == k['id']:
                                    sizes += '\n' + str(s['nikeSize']) + ': ' + str(k['level'])
                data = f"⚠ ULTIMO EA CARICATO : {title}\n{url}\n{img}\nStatus : {status}\nSTOCK:\n{sizes}"
    return data

def ea4():
    url  = "https://api.nike.com/product_feed/threads/v2/?anchor=1&count=100&filter=marketplace%28IT%29&filter=language%28it%29&filter=inStock%28false%29&filter=productInfo.merchPrice.discounted%28false%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29&fields=active&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.nodes&fields=publishedContent.properties.coverCard&fields=publishedContent.properties.productCard&fields=publishedContent.properties.products&fields=publishedContent.properties.publish.collections&fields=publishedContent.properties.relatedThreads&fields=publishedContent.properties.seo&fields=publishedContent.properties.threadType&fields=publishedContent.properties.custom"
    items = []
    first = 0
    sizes = ''
    html = rq.get(url=url, timeout=20, verify=False, headers=headers) # add proxies=proxy for enable proxy
    output = json.loads(html.text)
    status = html.status_code
    for item in output['objects']:
        items.append(item)
    PRIMO = 0
    for item in items:
        for j in item['productInfo']:
            if j['merchProduct']['exclusiveAccess'] == True and PRIMO != 5:
                code = j['merchProduct']['styleColor']
                title=j['productContent']['fullTitle']
                url='https://www.nike.com/' + 'it' + '/launch/t/' + j['productContent']['slug']
                img = j['imageUrls']['productImageUrl']
                status =j['merchProduct']["status"]
                PRIMO = PRIMO + 1
                if PRIMO == 5: 
                    for k in j['availableSkus']:
                        item = [j['productContent']['fullTitle'], j['productContent']['colorDescription'], k['id']]  
                        for s in j['skus']:
                            if first == 0:
                                if s['id'] == k['id']:
                                    sizes = str(s['nikeSize']) + ': ' + str(k['level'])
                                    first = 1
                            else:
                                if s['id'] == k['id']:
                                    sizes += '\n' + str(s['nikeSize']) + ': ' + str(k['level'])
                data = f"⚠ ULTIMO EA CARICATO : {title}\n{url}\n{img}\nStatus : {status}\nSTOCK:\n{sizes}"
    return data

def ea5():
    url  = "https://api.nike.com/product_feed/threads/v2/?anchor=1&count=100&filter=marketplace%28IT%29&filter=language%28it%29&filter=inStock%28false%29&filter=productInfo.merchPrice.discounted%28false%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29&fields=active&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.nodes&fields=publishedContent.properties.coverCard&fields=publishedContent.properties.productCard&fields=publishedContent.properties.products&fields=publishedContent.properties.publish.collections&fields=publishedContent.properties.relatedThreads&fields=publishedContent.properties.seo&fields=publishedContent.properties.threadType&fields=publishedContent.properties.custom"
    items = []
    first = 0
    sizes = ''
    html = rq.get(url=url, timeout=20, verify=False, headers=headers) # add proxies=proxy for enable proxy
    output = json.loads(html.text)
    status = html.status_code
    for item in output['objects']:
        items.append(item)
    PRIMO = 0
    for item in items:
        for j in item['productInfo']:
            if j['merchProduct']['exclusiveAccess'] == True and PRIMO != 6:
                code = j['merchProduct']['styleColor']
                title=j['productContent']['fullTitle']
                url='https://www.nike.com/' + 'it' + '/launch/t/' + j['productContent']['slug']
                img = j['imageUrls']['productImageUrl']
                status =j['merchProduct']["status"]
                PRIMO = PRIMO + 1
                if PRIMO == 6: 
                    for k in j['availableSkus']:
                        item = [j['productContent']['fullTitle'], j['productContent']['colorDescription'], k['id']]  
                        for s in j['skus']:
                            if first == 0:
                                if s['id'] == k['id']:
                                    sizes = str(s['nikeSize']) + ': ' + str(k['level'])
                                    first = 1
                            else:
                                if s['id'] == k['id']:
                                    sizes += '\n' + str(s['nikeSize']) + ': ' + str(k['level'])
                data = f"⚠ ULTIMO EA CARICATO : {title}\n{url}\n{img}\nStatus : {status}\nSTOCK:\n{sizes}"
    return data