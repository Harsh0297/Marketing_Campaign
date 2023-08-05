CREATE  VIEW `marital_status_of_customer` AS 
SELECT Marital_Status,
COUNT(Marital_Status) AS `People with Status` 
FROM marketing_campaign_merged_data 
GROUP BY Marital_Status;
