from ecommercetools import seo

results = seo.get_serps(query="co working in London", pages=3)
results.to_csv("co_working_london_3_pages.csv")
print(results)
