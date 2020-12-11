select "Region", count("Country") as "TotalCountry" from 
	(select "Region" , "Country" from bootcamp_test_alfi group by "Region","Country") as tb2
	group by "Region"