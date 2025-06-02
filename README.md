# FirstBank-OPay-Customer-Review-Sentiment
This project was inspired by recurring conversations on Twitter and in the tech community around the question: **"Which is better — traditional banks or fintech apps?"** As a Data Analyst, I decided to explore this debate using data. I gathered user reviews from the Google Play Store using Python (pandas, matplotlib, seaborn) and visualized the results with Power BI.

## Overview  
This project analyzes customer reviews of two popular Nigerian mobile banking apps—FirstBank (traditional bank) and OPay (fintech)—to understand user sentiment and app performance. The analysis was inspired by ongoing discussions on Twitter about which type of bank offers a better digital experience.

## Data Collection  
Using Python, I scraped real user reviews from the Google Play Store, focusing on feedback about app speed, reliability, and usability.

## Analysis  
I performed sentiment analysis and created interactive dashboards with Power BI to visualize trends in positive, neutral, and negative reviews, identifying key strengths and areas for improvement.

## Insights and Recommendations

### 🔹 FirstBank Dashboard Insights

- **Neutral Sentiment Dominates**  
  Most reviews fell under neutral sentiment, indicating users were either not emotionally invested or left short, standard comments.
  
- **Significant Negative Feedback**  
  Common complaints include app crashes, login failures, slow response times, and poor error handling.

- **Average Review Rating Is Moderate**  
  FirstBank's ratings hovered around the middle — not terrible, but far from excellent.

- **Low Engagement**  
  Reviews were generally short, often reflecting dissatisfaction or minimal user interest.

---

### ✅ FirstBank Recommendations

- **Improve App Reliability and Performance**  
  Fix recurring bugs and responsiveness issues to boost user trust.

- **Encourage Positive Reviews**  
  Prompt satisfied users with gentle in-app reminders to leave reviews and boost app reputation.

- **Enhance UI/UX**  
  A modern, seamless experience could increase engagement and reduce frustration.

---

### 🔹 OPay Dashboard Insights

- **Positive Sentiment Is Most Frequent (~49.11%)**  
  Users often praised the app for being *fast*, *reliable*, and *easy to use*.

- **Minimal Negative Sentiment**  
  A few reviews mentioned issues like delayed reversals or OTP verification problems, but these were relatively rare.

- **High Average Rating (~4.57)**  
  The ratings consistently reflected strong user satisfaction.

- **Higher User Engagement**  
  Reviews were slightly longer and more expressive, reflecting trust and emotional investment.

---

### ✅ OPay Recommendations

- **Maintain Quality and Reliability**  
  Continue improving performance and addressing minor issues early to retain user loyalty.

- **Monitor Isolated Complaints Proactively**  
  Even small issues like reversal delays can snowball if ignored.

- **Capitalize on Positive Feedback**  
  Highlight keywords like *fast* and *reliable* in ads and app store content.

---

### 🗂️ Final Notes

- This dashboard project uses a 2-day snapshot of app reviews. A longer data window could offer deeper trends.
- For side-by-side comparisons in Power BI, consider merging datasets and adding a “Bank Name” column for easy filtering.

---

## Technologies Used  
- Python (for web scraping)
- Excel (For data Cleaning)
- Power BI (for data visualization)

## Project Structure  
/data
└── firstbank_reviews.csv
└── opay_reviews.csv
/scripts
└── scraper.py
└── sentiment_analysis.py
/PowerBI
└── dashboard.pbix
/README.md

## How to Run

1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/FirstBank-vs-OPay-Review-Analysis.git
2. Navigate into the project folder:
   cd FirstBank-vs-OPay-Review-Analysis
3. Run the Python scraper (make sure dependencies are installed):
   python scripts/scraper.py
4. Open the Power BI dashboard (dashboard.pbix) with Power BI Desktop to explore the visualizations.
   
## Dependencies

- Python 3.x
- pandas
- matplotlib
- seaborn
- Power BI Desktop

## Screenshots
![Opay Sentiment Analysis Dashboard](https://github.com/user-attachments/assets/657750ba-1d9f-442a-a02f-9859539c327a)
![FirstBank Sentiment Analysis Dashboard](https://github.com/user-attachments/assets/8b31fb1c-1fcc-4996-88c9-8e538de1a407)

## Author
[Gbemisola Abolade] — Data Analyst
GitHub: https://github.com/Gbemisola-lab




