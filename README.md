# Web-Scraping-using-API
A basic web scraping program to retrieve all the products enlisted in Big Basket under different levels of categories. Information regarding the price, quantity, brand name, product ID, similar products, etc for each product are retrieved. This project aims at extracting data from the API calls that are being received from the main web server of the website. Upon inspecting the different API calls and its REST method from the client system, and API call under GET method was identified to carry the essential details from the web server. 

A single API call is chosen and it is iteratively run under a try-except loop for a range of pages. The required details are stored as lists. The entire set of lists is stored as a data frame that can be converted to a CSV or JSON file. 

