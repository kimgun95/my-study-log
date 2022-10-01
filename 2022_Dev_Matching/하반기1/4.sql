SELECT id, name, count(id) FROM places pl
LEFT JOIN schedules sc
ON pl.id = sc.place_id
WHERE price IS NOT null
GROUP BY pl.id, pl.name
ORDER BY pl.id