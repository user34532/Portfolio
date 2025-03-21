-- SQL query for analyzing Supermetrics marketing data
SELECT campaign, SUM(clicks) AS total_clicks, SUM(impressions) AS total_impressions
FROM marketing_data
GROUP BY campaign
ORDER BY total_clicks DESC;
