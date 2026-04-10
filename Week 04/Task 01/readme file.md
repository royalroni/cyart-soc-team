#  Task 3: Post-Incident Analysis

##  Objective
To perform root cause analysis (RCA), document lessons learned, and calculate SOC performance metrics for a phishing incident.

---

##  Tools Used
- Google Sheets (RCA & Metrics)
- Draw.io (Fishbone Diagram)
- SOC Analysis Techniques

---

##  Incident Description
A phishing email led to credential theft due to lack of user awareness and weak email security controls.

---

##  Root Cause Analysis (5 Whys)

| Question                     | Answer                          |
|----------------------------|--------------------------------|
| Why was email opened?      | User clicked malicious link     |
| Why was link clicked?      | Lack of phishing awareness      |
| Why no awareness?          | No user training program        |
| Why no training?           | Weak security policy            |
| Why weak policy?           | Lack of security governance     |

---

##  Fishbone Diagram (Cause Analysis)

📸 Screenshot:
`screenshots/task3_fishbone_diagram.png`

### Key Causes Identified:

- **People**
  - Lack of phishing awareness
  - No training provided
  - User failed to detect suspicious email

- **Process**
  - No incident response procedure
  - No email verification workflow
  - No regular audits

- **Policy**
  - Weak access control policies
  - No mandatory training policy

- **Technology**
  - Weak email filtering
  - No advanced threat detection (ATP)
  - Outdated antivirus/email gateway

- **Environment**
  - Remote work exposure
  - High volume of emails
  - Increased external threats

---

##  SOC Metrics Calculation

| Metric | Value |
|--------|------|
| MTTD (Mean Time to Detect) | 2 hours |
| MTTR (Mean Time to Respond) | 4 hours |

---

##  Metrics Summary (50 Words)

The phishing incident was detected within 2 hours and resolved in 4 hours, indicating moderate SOC efficiency. However, delays in detection highlight gaps in monitoring and alerting mechanisms. Improving threat detection systems, user awareness training, and automated response capabilities can significantly reduce response time and enhance overall security posture.

---

##  Lessons Learned

- User awareness training is critical
- Strong email filtering must be implemented
- Incident response procedures should be defined
- Regular audits are necessary
- Advanced threat detection tools should be deployed

---