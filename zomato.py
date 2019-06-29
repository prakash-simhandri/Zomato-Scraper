from bs4 import BeautifulSoup
from pprint import pprint

# ye code dynamic web page ko open karneme madat karata hai..

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zomato.com/nagpur')
response = browser.execute_script('return document.documentElement.outerHTML')
browser.quit()

# ye code web page ko scrapeing karne me madat kar ta hai.

soup =BeautifulSoup(response,'html.parser')
Towns = soup.find('div',class_='ui segment row')
All_Towns_ditalls = Towns.findAll('a',class_='col-l-1by3 col-s-8 pbot0')
Towns_links=[]
num=0
for one_by_one_titals in All_Towns_ditalls:
	num+=1
	titals=(one_by_one_titals.text.split())
	print(num," ".join(titals)+'\n')
	Towns_links.append(one_by_one_titals.get('href'))

def link_open(zomato):
	user_choes = int(input('Enter the your choes >>'))

	# ye code next link ko open karne me madat kar ta hai.

	Restaurants_link = webdriver.Chrome()
	Restaurants_link.get(zomato[user_choes-1])
	second_response = Restaurants_link.execute_script('return document.documentElement.outerHTML')
	Restaurants_link.quit()

	# ye code next link ko scrapeing karne me madat kar ta hai.

	second_soup =BeautifulSoup(second_response,'html.parser')
	food_tital = second_soup.findAll('div',class_='left floated')
	num_2=1
	for B_L_d in food_tital:
		only_tital = B_L_d.find('div',class_='fontsize1 semi-bold mt2')
		print(num_2,only_tital.text.strip())
		num_2+=1

	All_foods_ditals =second_soup.findAll('div',class_='pb5 bt ptop0 ta-right')
	food_tital_link=[]
	for see_more in All_foods_ditals:
		food_tital_link.append(see_more.find('a').get('href'))
	return(food_tital_link)
Restaurants_food=link_open(Towns_links)


def food_menu(zomato):
	user_choes_second=int(input('Enter the your choes >>'))
	if user_choes_second == 2:
		Delivery_foods =webdriver.Chrome()
		Delivery_foods.get(zomato[user_choes_second-1])
		fourth_response =Delivery_foods.execute_script('return document.documentElement.outerHTML')
		Delivery_foods.quit()

		fourth_soup =BeautifulSoup(fourth_response,'html.parser')
		Delivery_ditals =fourth_soup.findAll('div',class_='js-search-result-li even near status 1')
		Delivery_list=[]
		for Delivery in Delivery_ditals:
			tital_div =Delivery.find('div',class_='search_left_featured clearfix').find('a').get('href')
			word=''
			for slysing in tital_div[30:]:
				if slysing != '/':
					word+=slysing
				else:
					break
			tital=(word)

			rateing_div =Delivery.find('div',class_='ta-right floating search_result_rating col-s-4 clearfix')
			rateing =rateing_div.find('div').get_text().strip()

			RS =Delivery.find('span',class_='col-s-11 col-m-12 pl0').get_text()

			Delivery_list.append({'name':tital,'Rating':rateing,'COST FOR TWO':RS})
		pprint(Delivery_list)
	else:
		zomato_foods =webdriver.Chrome()
		zomato_foods.get(zomato[user_choes_second-1])
		therd_response = zomato_foods.execute_script('return document.documentElement.outerHTML')
		zomato_foods.quit()

		# ye code next link ko scrapeing karne me madat kar ta hai.

		therd_soup =BeautifulSoup(therd_response,'html.parser')
		food_ditals =therd_soup.findAll('div',class_='js-search-result-li even status 1')
		Delivery_list=[]
		for food_name in food_ditals:
			col = food_name.find('div',class_='search_left_featured clearfix').find('a').get('href')
			# name_type =col.find('a',class_='data-result-type')
			word=''
			for slysing in col[30:]:
				if slysing != '/':
					word+=slysing
				else:
					break
			yame=(word)
			rateing=food_name.find('div',class_='ta-right floating search_result_rating col-s-4 clearfix')
			only_ratieng =rateing.find('div').get_text().strip()

			RS=food_name.find('span',class_='col-s-11 col-m-12 pl0').get_text()

			Delivery_list.append({'name':yame,'Rating':only_ratieng,'COST FOR TWO':RS})
		pprint(Delivery_list)
zomato_food_ditals=food_menu(Restaurants_food)
