-- COUNT와 SUM을 where로 만들려다가 도저히 안되서 막판에 case문으로 만드는 경우를 찾아냄, 나이스!
SELECT EXTRACT(YEAR FROM created_at), EXTRACT(MONTH FROM created_at),
    COUNT(CASE WHEN category = 1 THEN 1 ELSE NULL END), -SUM(CASE WHEN category = 1 THEN amount ELSE 0 END)
FROM card_usages
GROUP BY EXTRACT(YEAR FROM created_at), EXTRACT(MONTH FROM created_at)
ORDER BY EXTRACT(YEAR FROM created_at) DESC, EXTRACT(MONTH FROM created_at) DESC