stocks=["reliance","infosys","tcs"]
prices=[2757,3754,890]

new_dict={stocks:prices for stocks,
                                prices in zip(stocks,prices)}
print(new_dict)