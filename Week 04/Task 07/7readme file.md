#  Task 7: Security Metrics and Executive Reporting

##  Objective
To calculate SOC performance metrics, create a dashboard in Elastic Security, and generate an executive report.

---

##  Tools Used
- Elastic Security (Dashboard & Metrics)
- Google Sheets / Excel (Dwell Time Calculation)
- Google Docs (Executive Reporting)

---

##  Metrics Dashboard (Elastic Security)

Created a dashboard in Elastic showing key SOC metrics:

- MTTD (Mean Time to Detect)
- MTTR (Mean Time to Respond)
- False Positive Rate

📸 Screenshots:
- `screenshots/task7_dashboard_creation.png`
- `screenshots/task7_dashboard_list.png`
- `screenshots/task7_metrics_visualization.png`
- `screenshots/task7_final_dashboard.png`

---

##  Metrics Values

| Metric | Value |
|--------|------|
| MTTD   | 3 hours |
| MTTR   | 3 hours |
| False Positive Rate | Low (approx. 3 events) |

---

##  Dwell Time Calculation

Dwell time = Time attacker remains undetected in the system.

From Excel:

| Start Time | End Time | Dwell Time |
|------------|----------|------------|
| 00:00      | 05:00    | 05:00      |

📸 Screenshot:
`screenshots/task7_dwell_time.png`

 Calculation Explanation:
- Formula used:  
```excel
=B3-A3