-- SQL query to analyze memory recall patterns
SELECT participant_id, AVG(recall_score) AS avg_score
FROM memory_data
GROUP BY participant_id
ORDER BY avg_score DESC;
