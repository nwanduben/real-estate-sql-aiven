##  Project Summary: Real Estate Market Analytics (2001–2022)

### Overview
This project analyzes over 1 million property sales across Connecticut (2001–2022) using PostgreSQL and Python.  
The goal is to uncover pricing trends, regional patterns, and correlations between assessed and actual market values.

### Key Insights
- **Top Luxury Markets:** Greenwich, New Canaan, and Darien lead with average property prices above \$1.6M.  
-  **Market Trends:** Sales volume declined sharply post-2008, indicating the housing bubble impact.  
-  **Value Correlation:** A moderate correlation (0.52) between assessed and sale values reveals price variability across regions.  
-  **Property Types:** Residential and condominium properties dominate sales activity.  
-  **Yearly Dynamics:** 2006–2007 marked a peak in average sale prices before the dip.

### Tools Used
- **PostgreSQL (Aiven)** — SQL-based EDA & aggregation queries  
- **Python (Pandas, Psycopg2)** — automation and data loading  

##  Data Sources
All datasets used in this project are publicly viewable via Google Drive.

| Dataset | Description | Download Link |
|----------|--------------|----------------|
| Real_Estate_Sales_2001-2022_GL.csv | Full Connecticut real estate sales data (2001-2022) | [View on Drive](https://drive.google.com/drive/u/0/folders/1tv9D93a0vPIV03RirIVUAOidPZ_xbVYd) |
| sample_real_estate.csv | Lightweight 1 000-row sample for quick testing | [View on Drive](https://drive.google.com/drive/u/0/folders/1tv9D93a0vPIV03RirIVUAOidPZ_xbVYd) |
| yearly_sales.csv | Yearly total sales summary | [View on Drive](https://drive.google.com/drive/u/0/folders/1c7s_yb0IPsSM4eXjkAXrIf8d9UlY_g9e) |
| top_towns.csv | Top 10 towns by average sale price | [View on Drive](https://drive.google.com/drive/u/0/folders/1c7s_yb0IPsSM4eXjkAXrIf8d9UlY_g9e) |
| avg_sale_trend.csv | Average sale trend by year | [View on Drive](https://drive.google.com/drive/u/0/folders/1c7s_yb0IPsSM4eXjkAXrIf8d9UlY_g9e) |
| corr_assessed_sale.csv | Correlation between assessed value and sale price | [View on Drive](https://drive.google.com/drive/u/0/folders/1c7s_yb0IPsSM4eXjkAXrIf8d9UlY_g9e) |
| median_property_type.csv | Median sale price by property type | [View on Drive](https://drive.google.com/drive/u/0/folders/1c7s_yb0IPsSM4eXjkAXrIf8d9UlY_g9e) |
| top_residential_types.csv | Top residential types by average price | [View on Drive](https://drive.google.com/drive/u/0/folders/1c7s_yb0IPsSM4eXjkAXrIf8d9UlY_g9e) |





