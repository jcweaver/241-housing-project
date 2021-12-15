import pandas as pd
import numpy as np
import requests
import yaml
import csv
import re
import pandas as pd
import numpy as np
from functools import reduce
from itertools import chain, repeat
import operator

# Requests
create_session = lambda : requests.Session()

# Reading files

# This lambda is passed around to config the requests for Census data
# Following instructions from: https://api.census.gov/data/2019/acs/acs5/examples.html & https://api.census.gov/data/2019/acs/acs5/profile/examples.html
config = lambda x, y, z, a, b: {
    'base': 'https://api.census.gov/data',
    'date': y,
    'endpoint': x,
    'codes': z,
    'county': b,
    'state': a,
    'key': '46d54a1a571c5269457ff16466c244dd5b7cab24'
}



#Need to update to follow - https://api.census.gov/data/2019/acs/acs5/examples.html
#https://api.census.gov/data/2019/acs/acs5?get=NAME,B01001_001E&for=block%20group:*&in=state:01&in=county:001&in=tract:*&key=YOUR_KEY_GOES_HERE
def format_request(base, endpoint, date, codes, state, county, key):
    codes = f"get=NAME,{','.join(map(str,codes))}"
    #bg = f'for=block%20group:*'
    state = f'in=state:{state}'
    county = f'in=county:{county}'
    tract = f'for=tract:*'
    key = f'key={key}'
    args = '&'.join(map(str, [codes, tract, state, county, key]))
    url = f'{base}/{date}/{endpoint}?{args}'
    return url

def make_request(url, session):
    """A wrapper/bracket for making HTTP requests"""
    try:
        req = session.get(url)
        #print("req=",req)
        return req
    except Exception as e:
        return e
    
def small_batch_request(session, partition, func, arg, date, exceptions, state, county, debug=False):
    """ make small batch requests to the Census API. The limit is 50. This function makes requests of 40."""
    tmp = partition[arg][:]
    if exceptions.get(arg, False):
        for exception in exceptions[arg]:
            if date <= int(exception['start']):
                for y in exception['codes']:
                    if y in tmp:
                        tmp.remove(y)
                        
    if len(tmp) == 0:
        return None
        
    date = str(date)
    if debug:
        print(format_request(**func(arg, date, tmp[:40], state, county)))
    try:
        res = result_to_dataframe(make_request(format_request(**func(arg, date, tmp[:40], state, county)), session).json())
    except:
        return None 
    
    while (len(tmp) >= 40):
        tmp = tmp[40: ]
        idx = len(tmp)
        if debug:
            print(format_request(**func(arg, date, tmp[:idx], state, county)))
        df = result_to_dataframe(make_request(format_request(**func(arg, date, tmp[:idx], state, county)), session).json())
        res = pd.concat([res,df], axis=1)
    return res

def small_batch_all(session, partition, func, endpoints, date, state, county, exceptions={}, debug=False):
    """small batch requests are done for each endpoint and then concatenated into a final dataframe."""
    #small_batch_all(session, codes, config, part, year, exceptions, pad_with_zero(state), pad_place_with_zero(county), debug)
    res = small_batch_request(session, partition, func, endpoints[0], date, exceptions, state, county, debug)
    for arg in endpoints[1:]:
        if type(res) != pd.DataFrame:
            res = small_batch_request(session, partition, func, arg, date, exceptions, state, county, debug)
        else:
            tmp = small_batch_request(session, partition, func, arg, date, exceptions, state, county, debug)
            if type(tmp) == pd.DataFrame:                
                #res = pd.concat([res, tmp], axis=1)
                res = res.merge(tmp, how = "inner", on=["NAME","state","tract","county"])
        
    if type(res) != pd.DataFrame:
        #print("res =",res)
        return res
    else:
        pass
        #res['year'] = int(date)
        #res['FIPSST'] = state
        #res['COUNTY'] = county
        #res = res.loc[:,~res.columns.duplicated()]
    return res
    
def result_to_dataframe(res):
    x = pd.DataFrame(res[1:], columns=res[0])
    return x

        
def gather_results(session, acs_endpoints, config, state_county, codes, dfs=[], start=0, debug=False):
    """ Main entry point into the execution of a call to the census API. Requires:
    (1) session: requests.Session
    (2) part:  a list of acs_endpoints
    (3) config:   the configuration lambda at the top of this file
    (4) codes: a dictionary of strings of an ACS source (i.e. acs5 or acs5/profile) mapping to a list of string variable names
    (5) state_county: list of valid states and counties
    """
    failure_point = -1
    for i in range(start, len(state_county)):
        state = state_county[i][0]
        county = state_county[i][1]
        print(state, county)
        try:
            # Reach this is the state-county is valid.
            # we make a bunch of requests and append the results to a list
            year=2019
            tmp = [small_batch_all(session, codes, config, acs_endpoints, year, pad_with_zero(state), pad_place_with_zero(county), debug=False)]
            #print(tmp)
            list(map(lambda x: tmp.remove(x) if type(x) != pd.DataFrame else x, tmp[:]))
            if len(tmp) != 0:
                dfs.append(tmp)
            print(f"Status: {((i+1)/len(state_county))*100:.2f}%")
        except:
            # if there is a failure record this index as the failure point and break. Print out the point where the task failed for debugging.
            failure_point = i
            break
    if failure_point == -1:
        df = pd.concat(list(chain(*dfs)), ignore_index=True)
        df = df.fillna(-1)
        return df
    else:
        print(f"The task failed at this point: {failure_point}")
        return 0


zeros = lambda x: "".join(map(str, repeat("0", x)))

pad_with_zeros = lambda x, y: str(x) if y - len(str(x)) == 0 else zeros(y - len(str(x)))+str(x)

pad_with_zero =  lambda x : str(x) if len(str(x)) > 1 else "0"+str(x)

pad_place_with_zero =  lambda x : str(x) if len(str(x)) >= 3 else "00"+str(x) if len(str(x))==1 else "0"+str(x)

def pad_tract_with_zero(x):
    val = str(x)
    while len(val) < 6:
        val = "0"+val
    return val

        

          