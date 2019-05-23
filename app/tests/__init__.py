
# # url: https://www.apartments.com/1-bedrooms-1-bathrooms-under-1900/washer-dryer-dishwasher/?sk=52bf689fa8847bfa84178de70fa77f6b&bb=o484mpu_xJl4uyvJ
# # around north side, washer dryer dishwasher, 1 bed < 1900
#
# # url: https://www.apartments.com/chicago-il/1-bedrooms-1-bathrooms-under-1900/washer-dryer-dishwasher/'
# # all of chicago, washer dryer dishwasher, 1 bed < 1900
#
# # url: https://www.apartments.com/avondale-chicago-il/1-bedrooms-1-bathrooms-under-1900/washer-dryer-dishwasher/
# # avondale neighborhood, washer dryer dishwasher, 1 bed < 1900
#
# trulia_url = 'https://www.apartments.com/1-bedrooms-1-bathrooms-under-1900/washer-dryer-dishwasher/?sk=52bf689fa8847bfa84178de70fa77f6b&bb=o484mpu_xJl4uyvJ'
#
# response = get(trulia_url, headers=headers)
# html_soup = BeautifulSoup(response.text, 'html.parser')
#
#
# placards = html_soup.find_all('article', class_="placard")
# location = apartment.find(class_="placardTitle").get('title')
#
# url = apartment.get('data-url')
# if not location[:1].isdigit():
#     location = apartment.find('div', class_="location").text
#
# rent = apartment.find('span', class_="altRentDisplay").text
#
# main_info = html_soup.find('tr', class_="rentalGridRow")
# beds = main_info.find('td', class_="beds").find('span', class_="longText").text.strip()
# baths = main_info.find('td', class_="baths").find('span', class_="longText").text.strip()
# sqft = main_info.find('td', class_="sqft").text.strip()
# leaseLength = main_info.find('td', class_="leaseLength").text.strip()
# dateAvailable = main_info.find('td', class_="available").text.strip()
# description = html_soup.find('section', class_="descriptionSection").find('p').text.strip()

# apartment = Apartment('https://www.apartments.com/lakeview-3200-chicago-il/3qc6kde/',
#                           '3200 N Clark St, Chicago, IL 60657', '$1,844 - 2,100')