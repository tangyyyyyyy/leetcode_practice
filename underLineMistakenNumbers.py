# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:55:43 2024

You're holding a silent auction with 650 bidders, assigning each bidder a numbered sign between 1-650. A person raises their sign when they want to make an offer.

Sometimes, bidders accidentally hold the sign upside-down, and then mistakes their number for a different number. For example, bidder #6 could be mistaken for bidder #9 if they held it incorrectly.

Write a function to help you find all the numbers that need to be underlined because they can be misinterpreted for another number in the range 1-650.

@author: Kashyap
"""

def underLineMistakenNumbers(MAX_BID=650):
    
    flipped_digit_dict = {
        '0':'0',
        '1':'1',
        '2':'',
        '3':'',
        '4':'',
        '5':'',
        '6':'9',
        '7':'',
        '8':'8',
        '9':'6'
        }
    
    bidders = range(1, MAX_BID+1)
    underlined_bidders = []
    
    for bidder in bidders:
        
        bidder_str = str(bidder) #unflipped digits as a string
        if bidder_str.endswith('0'): #ends in 0, safe
            continue
        
        flipped_bidder_str = bidder_str.translate(bidder_str.maketrans(flipped_digit_dict)) #replace digits based on dict
        if len(flipped_bidder_str) != len(bidder_str): #if contains safe char, safe
            continue
        
        flipped_bidder_str = flipped_bidder_str[::-1] #flip string
        if flipped_bidder_str == bidder_str: #they are the same, safe
            continue
        
        if int(flipped_bidder_str) > MAX_BID: #if greater than maxbid, safe
            continue
        
        else:
            underlined_bidders.append(bidder)
        
    return underlined_bidders
    
         
test = underLineMistakenNumbers()
print('\n', test)
print(len(test))
