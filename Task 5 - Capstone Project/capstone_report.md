# Capstone Project: Full Alert-to-Response Cycle

## 1. Attack Simulation
A brute-force SSH login attempt was simulated by generating multiple failed login attempts on the system.

## 2. Detection
The attack activity was successfully detected using Wazuh SIEM. Alerts were generated based on suspicious authentication activity.

(Screenshot: wazuh_detection.png)

## 3. Alert Triage
The alerts were analyzed using Wazuh Events. Multiple SSH failed login alerts were observed.

(Screenshot: wazuh_alert_details.png)

| Alert ID | Description                    | Source        | Priority | Status        |
|----------|--------------------------------|--------------|----------|--------------|
| 001      | SSH Failed Login Attempts      | soc-server   | Medium   | True Positive|

MITRE Technique: T1110 (Brute Force)

## 4. Response Actions
- Monitored repeated failed login attempts
- Checked system logs for suspicious activity
- Verified no successful unauthorized access
- Strengthened authentication mechanisms

## 5. Evidence Collection
Velociraptor was used to collect forensic evidence such as running processes and system activity.

(Screenshot: velociraptor_evidence.png)

## 6. Conclusion
The simulated attack was successfully detected and analyzed. No system compromise was observed.

## 7. Recommendations
- Implement account lockout policies
- Improve alert monitoring rules
- Conduct regular security assessments