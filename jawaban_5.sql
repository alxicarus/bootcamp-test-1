select "Region" ,"Country" , "AvgTemperature" 
	from (
		select "Region", "Country", "AvgTemperature", "Day", "Month" , "Year" , Rank()
			over (partition by "Region" order by "AvgTemperature" desc) as rn 
			from bootcamp_test_alfi where "Day" = 1 and "Month" = 10 and "Year" = 2012
	) as t2 where rn <=5