select "Country" , "Year" , max("AvgTemperature"), min("AvgTemperature") 
	from bootcamp_test_alfi 
	where ("Country" = 'Canada' or "Country" = 'Malaysia' or "Country"='Turkey') and "Year" = 2018 group by "Country", "Year" 