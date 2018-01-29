# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:00:14 2018

@author: jonatha.costa
"""

from NYTimesArticleAPI import articleAPI
api = articleAPI("Key")


articles = api.search(q="Obama", 
                          fq={"headline": "Obama", 
                              "source": ["Reuters", 
                                         "AP", 
                                         "The New York Times"]}, 
                          begin_date="20161001", # this can also be an int
                          facet_field=["source", "day_of_week"], 
                          facet_filter=True)



fq = {"headline": "Obama", "source": ["Reuters", "AP", "The New York Times"]}
articles = api.search(q="Obama", fq=fq)


articles = api.search(q="Obama")
articles = api.search(q="Obama", begin_date="20161001", end_date="20161020", page=2)
headers = api.req.headers