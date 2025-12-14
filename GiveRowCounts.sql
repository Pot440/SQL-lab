SELECT 
	'HighLowEntries' AS TabName,
	COUNT(*) AS RowCount
FROM `high_low table`
UNION ALL
SELECT 
	'OpenCloseEntries' AS TabName,
	COUNT(*) AS RowCount
FROM `open_close table`
UNION ALL
SELECT 
	'VolumeEntries' AS TabName,
	COUNT(*) AS RowCount
FROM `volume table`;