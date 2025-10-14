-- 1. Overview: total transactions per year
SELECT list_year, COUNT(*) AS num_sales
FROM real_estate_sales
GROUP BY list_year
ORDER BY list_year;

-- 2. Average sale price per town
SELECT town, ROUND(AVG(sale_amount), 2) AS avg_price
FROM real_estate_sales
WHERE sale_amount > 0
GROUP BY town
ORDER BY avg_price DESC
LIMIT 15;

-- 3. Year-over-year average sale price trend
SELECT list_year, ROUND(AVG(sale_amount), 2) AS avg_sale
FROM real_estate_sales
WHERE sale_amount > 0
GROUP BY list_year
ORDER BY list_year;

-- 4. Correlation between assessed and sale values
SELECT ROUND(CAST(CORR(assessed_value, sale_amount) AS numeric), 3) AS corr_ratio
FROM real_estate_sales
WHERE assessed_value > 0 AND sale_amount > 0;

-- 5. Median sale price by property type
SELECT property_type,
       ROUND(CAST(PERCENTILE_CONT(0.5) 
                  WITHIN GROUP (ORDER BY sale_amount) AS numeric), 2) AS median_sale
FROM real_estate_sales
WHERE sale_amount > 0
GROUP BY property_type
ORDER BY median_sale DESC;


-- 6. Top 10 residential types by volume
SELECT residential_type, COUNT(*) AS total_sales
FROM real_estate_sales
GROUP BY residential_type
ORDER BY total_sales DESC
LIMIT 10;
