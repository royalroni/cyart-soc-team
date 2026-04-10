#  Task 4: Alert Triage & Investigation

##  Objective
The objective of this task is to simulate a security alert, perform threat investigation, validate indicators using threat intelligence platforms, and manage the incident lifecycle using TheHive and Cortex.

---

##  Tools & Technologies Used

- **Wazuh** – Security monitoring and alert generation  
- **VirusTotal** – Threat intelligence and IP reputation analysis  
- **TheHive** – Incident response and case management  
- **Cortex** – Automated analysis and enrichment engine  
- **Windows PowerShell** – Activity simulation  

---

##  Step 1: Alert Simulation

A suspicious activity was simulated by creating a new user account on the Windows system:

```powershell
net user testuser123 Password@123 /add

 Purpose:
Simulates unauthorized account creation
Represents a potential privilege escalation or persistence technique

📸 Screenshot:
screenshots/task4_user_creation.png



 Step 2: Threat Intelligence Analysis

The identified IP address was analyzed using VirusTotal:

IP Address: 192.168.56.1
Detection Result: 0 / 94 (Clean)
 Key Observation:
The IP belongs to a private network range (RFC1918)
Private IPs are not publicly routable, hence no external malicious reputation

📸 Screenshot:
screenshots/task4_virustotal.png



 Step 3: Case Creation in TheHive

A new incident case was created to document and manage the alert:

Case Details:
Title: Suspicious Activity
Severity: Medium
TLP: Amber
PAP: Amber
Tags: suspicious-login
 Description:

Suspicious login/user activity detected from Wazuh alert. Source IP identified and validated using VirusTotal.

📸 Screenshots:

screenshots/task4_case_creation.png
screenshots/task4_case_details.png


 Step 4: Observable Enrichment

The following observable was added to the case:

Type	Value	Tag
IP	192.168.56.1	suspicious-ip

 Purpose:

Enables threat intelligence enrichment
Supports automated analysis via Cortex

📸 Screenshot:
screenshots/task4_observable.png


 Step 5: Cortex Analyzer Integration

Cortex was configured with multiple analyzers for automated investigation:

Enabled Analyzers:
YARA Analyzer
AbuseIPDB
IPInfo
VirusTotal (if configured)
Functionality:
Enrich observables with threat intelligence
Automate investigation workflows
Reduce manual analysis time

📸 Screenshots:

screenshots/task4_cortex_setup1.png
screenshots/task4_cortex_setup2.png


 Findings & Analysis
A new user account was successfully created on the system
This activity can indicate:
Unauthorized access attempt
Persistence mechanism
The investigated IP was found to be:
A private IP address
Not associated with any known malicious activity
No external threat indicators were identified


 MITRE ATT&CK Mapping
Technique ID	Technique Name	Description
T1078	Valid Accounts	Use of legitimate credentials
T1136	Create Account	Creation of new user accounts
T1046	Network Service Discovery	Scanning internal services


 Recommendations
Enable alerts for user account creation events
Implement Multi-Factor Authentication (MFA)
Monitor privileged account activity
Integrate SOAR automation for faster response
Perform regular security audits


 SOC Workflow Summary
Alert generated (Wazuh)
Suspicious activity identified
Indicator extracted (IP Address)
Threat intelligence validation (VirusTotal)
Case created (TheHive)
Observable added
Analyzer configured (Cortex)
Investigation completed


 Conclusion

The alert triage process was successfully performed using industry-standard SOC tools. The suspicious activity was investigated, validated, and documented through proper incident response procedures. Although the activity was identified as internally generated, the workflow demonstrated effective detection, analysis, and response capabilities within a Security Operations Center (SOC) environment.