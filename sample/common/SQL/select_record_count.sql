SELECT 'employee' AS table_name, COUNT(1) AS record_count FROM employee UNION ALL
SELECT 'customer' AS table_name, COUNT(1) AS record_count FROM customer UNION ALL
SELECT 'play_list' AS table_name, COUNT(1) AS record_count FROM play_list UNION ALL
SELECT 'media_type' AS table_name, COUNT(1) AS record_count FROM media_type UNION ALL
SELECT 'invoice' AS table_name, COUNT(1) AS record_count FROM invoice UNION ALL
SELECT 'genre' AS table_name, COUNT(1) AS record_count FROM genre UNION ALL
SELECT 'artist' AS table_name, COUNT(1) AS record_count FROM artist UNION ALL
SELECT 'album' AS table_name, COUNT(1) AS record_count FROM album UNION ALL
SELECT 'track' AS table_name, COUNT(1) AS record_count FROM track UNION ALL
SELECT 'playlist_track' AS table_name, COUNT(1) AS record_count FROM playlist_track UNION all
SELECT 'invoice_line' AS table_name, COUNT(1) AS record_count FROM invoice_line;