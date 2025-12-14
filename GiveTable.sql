SELECT
	HL.Date,
    HL.High,
    HL.Low,
    OC.Open,
	OC.Close,
    OC.`Adj Close`,
    VU.Volume
FROM
	`High_Low Table` AS HL
JOIN
	`Open_Close Table` AS OC ON HL.Date = OC.Date
JOIN
	`Volume Table` AS VU ON HL.Date = VU.Date