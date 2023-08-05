CREATE VIEW `family_details` AS 
SELECT ID ,
Education,Marital_Status,
Income,
Enrolled_Date,Age,
Kidhome + Teenhome + Marital_Status_PeoplE AS `Family_Size`,
MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds AS `Total_Spend`,
NumDealsPurchases + NumWebPurchases + NumCatalogPurchases + NumStorePurchases AS `Total_Deal_Purchases`,
NumWebVisitsMonth
FROM marketing_campaign_merged_data;
