# -*- coding: utf-8 -*-

"""Buying a car;

https://www.codewars.com/kata/554a44516729e4d80b000012/train/python

Let us begin with an example:

A man has a rather old car being worth $2000. He saw a secondhand car being worth $8000. He wants to keep his old car
until he can buy the secondhand one

He thinks he can save $1000 each month but the prices of his old car and of the new one decrease of 1.5 percent per
month. Furthermore this percent of loss increases of 0.5 percent at the end of every two months. Our man finds it
difficult to make all these calculations

Can you help him?

How many months will it take him to save up enough money to buy the car he wants, and how much money will he have
left over?

"""


def nb_months(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    if start_price_old >= start_price_new:
        return [0, round(start_price_old - start_price_new)]
    
    month, savings = 0, 0
    price_old, price_new = start_price_old, start_price_new
    current_loss = percent_loss_by_month
    
    while (savings + price_old) < price_new:
        month += 1
        
        if month % 2 == 0:
            current_loss += 0.5
        
        price_old *= (100 - current_loss) / 100
        price_new *= (100 - current_loss) / 100
        
        savings += saving_per_month
    
    return [month, round(savings + price_old - price_new)]
