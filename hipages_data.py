#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json
import pandas as pd
import csv
import os.path
from random import randint
import time
import re
import requests
import json
import pandas as pd
from pandas import json_normalize
import ast


# In[ ]:


def get_data_hipages():
    
    l = []
    
    pagination = ""
    
    for x in range(5):
        pagination += 1
    
        url = "https://hipages.com.au/api/directory/sites?suburb=perth&state=wa&category=8&page={}&perpage=10&code=111d887415230e233b23fdaae8e160d62715d99d7c417a33c1ca27c0b47b3a6ce810db7af2cec77fe5a629d12ad9cc68".format(pagination)

        payload = {}
        headers= {}

        response = requests.request("GET", url, headers=headers, data = payload)

        json_data = json.loads(response.text)
        
       
        
        for x in json_data:
            print(type(x))
            del x['link']
            del x['requestAQuoteLink']
            del x['makeAnEnquiryLink']
            del x['thumbLink']
            del x['recommendationTrackLink']
            l.append(x)
    print(l)
    df = pd.DataFrame(l)
    df.to_csv('nombre8.csv', index=False, header=False, mode='a')

#get_data()


# In[ ]:


def get_category_truelocal():
    
    l_description = []
    
    l_jsonD = []
    
    l_category = {}
    
    category = ""
    
    url = "https://api.truelocal.com.au/rest/business-type/?passToken=V0MxbDBlV2VNUw==&"

    payload = {}
    headers = {
      'authority': 'api.truelocal.com.au',
      'accept': 'application/truelocal-1.0+json',
      'sec-fetch-dest': 'empty',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
      'dnt': '1',
      'origin': 'https://www.truelocal.com.au',
      'sec-fetch-site': 'same-site',
      'sec-fetch-mode': 'cors',
      'referer': 'https://www.truelocal.com.au/business-type',
      'accept-language': 'es-ES,es;q=0.9,en;q=0.8,nl;q=0.7',
      'cookie': '_vwo_uuid_v2=DA9765AC719145E7200BD9527793E2DC0|ee0fe2ee207b868ddedf9863e57478fd; _fbp=fb.2.1583255339750.87913506; tl_trackingid=34F566780A27DBB9D67D7830E496AD04; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; AMCVS_8412403D53AC3D7E0A490D4C%40AdobeOrg=1; AMCV_8412403D53AC3D7E0A490D4C%40AdobeOrg=1585540135%7CMCIDTS%7C18325%7CMCMID%7C18659484353519361890470684408141064779%7CMCAAMLH-1583867901%7C4%7CMCAAMB-1583867901%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1583270301s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; tl_trackingid_expires=1583276765968; ak_bmsc=6012CD2D40BDECD1AFC295243D145B0B17C91614BB4800003DCA5E5E8C663C2D~plhN8TQ5wPaAVeN/BuZHOKBxuKSYfO5JH5WlI+xnMU2NcfX+DXe7OR11Z3jJD3PYVnAbgFwQJi25gOpaFhyu6lLlvkXVLUu7gXq4Mz0GNYxBQtsbkiUKffrnJq4SC0ecH7sozJs4e/0gOfXxInL67WKWhP2aNfPN8h2J72Xq6hnJzJ1OjIh66T4Dr8X2mD6/zoyQp3UcYU3YZ/pXiBHxVhieYZV2sEKrK2cDzhfbRCLmQkRnXJGXRCAphqSTKZuYup; bm_mi=5751BEA1A2C66C076099AA1F99B4C0BA~LuWo5JI3UJvtwU18rxDQNokncj8Nl0ME2bl8WqAA+RufWTyf9Ys4zsFRrMJje0VivYOFFCSiMfUFWS++atoLUragx22oyjU263M00LXL6oJ/Oox/qWMEaJbF01EST0SuQaqsvJlKp5BAqtrDC/WXew9wSBAfV5h7N7bbDIt7BVE7HWDdwWmIbwkyBv997GSVTzlgc3tSbK0QC08h4CgkWcAhCJRw8qLV4iODYtkZTMcpAfTZtEIXUZIOQFUgJJCg; bm_sv=CEAE1537194ECD8BEE3E75BD3F66E4CD~nx0xmUVUpMrzTh5KyMm9G5YdYbkUyS59H0lb6Qsn/D/kLVp0tiZEw43YQqIhmUUXIqno/KWG3ECHonJRr0wBd4Fxjo5X6joTkXAU4zNAQr4tCfin9NyStTsywN24C+8AzrXrjPqC1mXi3l5xnf62Wzb4hbLep+SAG+SjLwuyfn4='
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    #print(response.text.encode('utf8'))
    
    json_data = json.loads(response.text)
    
    #print(type(json_data))
         
    for k,v in json_data.items():
        if k == "data":
            for x,a in v.items():
                if x == "parentCategory":
                    for z in a:
                        for f,g in z.items():
                            if f == "description":
                                category = g
                            if f == "subCategories":
                                for n,m in g.items():
                                    if n == "subCategory":
                                        for e in m:
                                            for i,j in e.items():
                                                if i == "description":
                                                    l_description.append(j)
                                                    
#                         jsonD = {
#                             category : l_description
#                         }
#                         l_description = []
#                         l_jsonD.append(jsonD)
                        l_category.setdefault(category,l_description)
                        l_description = []
    #print(l_description)
    #print(l_category)
    return l_category

#get_category_truelocal()


# In[ ]:


def get_companies_truelocal():

    url = "https://api.truelocal.com.au/rest/listings?inventory=true&keyword=software&limit=1000&offset=300&showCopyPoints=true&type=keyword&&passToken=V0MxbDBlV2VNUw=="

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    response_ = json.loads(response.text)

    df = pd.DataFrame(response_["data"]["listing"])

    df[["dateCreated", "name"]].to_csv('truelocal_list_businesses_1000_1.csv')
    
#get_companies_truelocal()


# In[ ]:


def get_companies_truelocal_():

    url = "https://api.truelocal.com.au/rest/listings?inventory=true&keyword=software&limit=1&offset=300&showCopyPoints=true&type=keyword&&passToken=V0MxbDBlV2VNUw=="

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    response_ = json.loads(response.text)

    df = pd.DataFrame(response_["data"]["listing"])
    
    dc = pd.DataFrame(df["contacts"])
    
    for k,v in dc.to_dict().items():
        for a,d in v.items():
            for x,c in d.items():
                if x == "contact":
                    da = pd.DataFrame(c)
                    da.to_csv('truelocal_list_contact_1000_1.csv',index=False, header=False, mode='a')
    
#get_companies_truelocal_()


# In[ ]:


def function(x): 
    list_1 = x.get("contacts").get("contact")
    id = x.get("id")
    name = x.get("name")
    fecha = x.get("dateCreated")
    json = {}
    for x in list_1:
        json[x["type"]] = x["value"]
    json["name"] = name
    json["id"] = id
    json["fecha"] = fecha
    return json


# In[ ]:


def get_all_companies_for_category_truelocal(category):
    
    try:
    
        size = 0   
        offset = 0
        limit = 200    
        resultado = 0   
        count_name_csv = 0   
        pCategory = category.upper()
        while True:
            print(count_name_csv)

            count_name_csv = count_name_csv + 1
            url = "https://api.truelocal.com.au/rest/listings?inventory=true&keyword={}&limit={}&offset={}&showCopyPoints=true&type=keyword&&passToken=V0MxbDBlV2VNUw==".format(pCategory,limit,offset)

            payload = {}
            headers= {}

            response = requests.request("GET", url, headers=headers, data = payload)

            response_ = json.loads(response.text)

            df = pd.DataFrame(response_["data"]["listing"])

            if size == 0:
                for k,v in response_.items():
                    if k == "data":
                        for k2,v2 in v.items():
                            if k2 == "size":
                                size = v2

            csv_str = 'truelocal_list_category_{}_offset_{}_numbrerCSV_{}.csv'.format(pCategory,offset,count_name_csv)

            df_1 = df.apply(lambda x: function(x), axis=1, result_type="expand")
            #df_1.to_csv('truelocal_list_contact_1000_7.csv',index=False, header=True, mode='a')

            df_1.to_csv(csv_str ,index=False, header=True, mode='a')

            #if offset >= size:
            if count_name_csv == 10:
                break
            else:
                resultado = size - offset
                print("resultado1", resultado)
                print("size1", size)
                print("offset1", offset)
                if resultado > limit:
                    resultado = 0
                    offset = offset + limit
                    print("resultado2", resultado)
                    print("size2", size)
                    print("offset2", offset)
                    print("limit2", limit)
                else:
                    offset = offset + resultado
                    print("resultado3", resultado)
                    print("size3", size)
                    print("offset3", offset)
                    print("limit3", limit)

            time.sleep(randint(0,4))
        
        return "End complilation pCategory {}".format(pCategory)
    except Exception as error:
        print({"result":False, "message":"Something went wrong, error details: {}".format(error)})
        return {"result":False, "message":"Something went wrong, error details: {}".format(error)}

    
#get_all_companies_for_category_truelocal("software")


# In[ ]:


def get_all_companies_of_all_categories():
    
    try:
        
        categories = get_category_truelocal()
        #print(categories)
        for key, value in categories.items():
            print(key)
            get_all_companies_for_category_truelocal(key)
    
        return True
    
    except Exception as error:
        print({"result":False, "message":"Something went wrong, error details: {}".format(error)})
        return False
    
get_all_companies_of_all_categories()


# In[ ]:


from pandas import json_normalize
import ast

def get_contact_for_category_truelocal():

    url = "https://api.truelocal.com.au/rest/listings?inventory=true&keyword=software&limit=2&offset=0&showCopyPoints=true&type=keyword&&passToken=V0MxbDBlV2VNUw=="

    payload = {}
    headers= {}
    
    l_jdonD = []
    
    Diccionario_msg = {}

    response = requests.request("GET", url, headers=headers, data = payload)

    response_ = json.loads(response.text)

    df = pd.DataFrame(response_["data"]["listing"])
    
    dc = pd.DataFrame(df["contacts"].apply(ast.literal_eval).values.tolist())
    
    #print(dc.head())
    
    dz = json_normalize(dc)
    
    print(dz)
    
#     for k,v in dc.to_dict().items():
#         for a,d in v.items():
#             for x,c in d.items():
#                 if x == "contact":
#                     for d in c:
#                         for b,m in d.items():
#                             if b == "value":
#                                 value = m
#                             elif b == "type":
#                                 ptype = m
#                                 Diccionario_msg.setdefault(ptype,value)
#     print(Diccionario_msg)
# #     da = pd.DataFrame(Diccionario_msg)
# #     da.to_csv('truelocal_list_contact_1000_5.csv',index=False, header=True, mode='a')
    
#get_contact_for_category_truelocal()


# In[ ]:


# import requests
# import json
# import pandas as pd
# from pandas import json_normalize
# import ast

# url = "https://api.truelocal.com.au/rest/listings?inventory=true&keyword=software&limit=2&offset=0&showCopyPoints=true&type=keyword&&passToken=V0MxbDBlV2VNUw=="

# payload = {}
# headers= {}

# l_jdonD = []

# Diccionario_msg = {}

# response = requests.request("GET", url, headers=headers, data = payload)

# response_ = json.loads(response.text)

# df = pd.DataFrame(response_["data"]["listing"])

# #dc = pd.DataFrame(df["contacts"].apply(ast.literal_eval).values.tolist())

# #print(dc.head())

# #dz = json_normalize(dc)

# #print(dz)


# In[ ]:


#df["contacts_1"] = df.apply(lambda x: [x.get("contacts").get("contact")[0]["value"],x.get("contacts").get("contact")[1]["value"]], result_type='expand')


# In[ ]:


import time
def function(x): 
    list_1 = x.get("contacts").get("contact")
    id = x.get("id")
    name = x.get("name")
    fecha = x.get("dateCreated")
    json = {}
    epoch = fecha
    print(time.strftime("%a, %d %b %Y", time.localtime(epoch)))
    for x in list_1:
        json[x["type"]] = x["value"]
    json["name"] = name
    json["id"] = id
    json["fecha"] = fecha
    return json


# In[ ]:


#df_1 = df.apply(lambda x: function(x), axis=1, result_type="expand")
# #df_1.to_csv('truelocal_list_contact_1000_7.csv',index=False, header=True, mode='a')


# In[ ]:


#df_1


# In[ ]:


# fecha = 1255932839000
# epoch = fecha
# print(time.strftime("%a, %d %b %Y", time.localtime(epoch)))


# In[2]:


# import os
# import errno
# try:
#     os.mkdir('dir2')
#     os.cd('dir2')
# except OSError as e:
#     if e.errno != errno.EEXIST:
#         raise


# In[ ]:




