SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, COALESCE(FREEZER_YN, "N") AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE LEFT(ADDRESS, 3) = "경기도"
ORDER BY WAREHOUSE_ID