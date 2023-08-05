CREATE VIEW `education` AS 
SELECT Education,
COUNT(Education) AS `People with Education Type` 
FROM `marketing_campaign_merged_data` 
GROUP BY Education;
