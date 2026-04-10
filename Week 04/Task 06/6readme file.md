# ⚔️ Task 6: Adversary Emulation using CALDERA

##  Objective
The objective of this task is to simulate real-world cyber attack techniques using MITRE CALDERA and analyze detection capabilities using a SOC environment.

---

##  Tools & Technologies Used

- **MITRE CALDERA** – Adversary emulation platform  
- **Wazuh** – Security monitoring and detection  
- **Windows VM** – Target machine  
- **MITRE ATT&CK Framework** – Attack technique mapping  

---

##  Step 1: Agent Deployment

A CALDERA agent was deployed on the Windows target system.

###  Observations:
- Agent status: **Alive & Trusted**
- Platform: Windows
- Privilege: Elevated

📸 Screenshot:  
`screenshots/task6_agent.png`

---

##  Step 2: Adversary Operation Execution

An adversary profile was executed to simulate attack techniques.

###  Activities Performed:

| Time | Ability | Status | Description |
|------|--------|--------|------------|
| 4:19 PM | PowerShell Command Execution | Failed | Attempted PowerShell execution |
| 4:20 PM | System Discovery (whoami) | Failed | User enumeration |
| 4:21 PM | CMD Execution | Success | Command execution via cmd |
| 4:21 PM | Get System Time | Success | System information gathering |

📸 Screenshots:
- `screenshots/task6_operation.png`

---

##  Step 3: MITRE ATT&CK Mapping

| Technique ID | Technique Name | Description |
|-------------|--------------|-------------|
| T1059 | Command and Scripting Interpreter | PowerShell and CMD execution |
| T1082 | System Information Discovery | System time and environment info |
| T1033 | System Owner/User Discovery | whoami command |

---

##  Step 4: Detection Analysis

| Timestamp | TTP | Detection Status | Notes |
|----------|-----|----------------|------|
| 17:10:12 | T1566 | Detected | PowerShell execution detected |
| 17:11:03 | T1566 | Detected | CMD execution detected |
| 17:12:10 | T1566 | Not Detected | No C2 traffic detected |

###  Key Findings:
- Some attack techniques were successfully detected
- Some activities were not detected, indicating **visibility gaps**
- Failed executions show realistic adversary behavior

---

##  Security Insights

- Detection systems successfully identified execution-based attacks
- Lack of C2 detection highlights monitoring limitations
- Failed attempts indicate potential misconfigurations or blocked execution

---

##  SOC Workflow

1. Deploy CALDERA agent  
2. Execute adversary profile  
3. Simulate attack techniques  
4. Monitor logs in Wazuh  
5. Analyze detection results  
6. Map techniques to MITRE ATT&CK  

---

##  Conclusion

The adversary emulation exercise successfully demonstrated how real-world attack techniques can be simulated and analyzed within a SOC environment. The results highlight both detection strengths and gaps, providing valuable insights for improving security monitoring and response capabilities.

---

## 📎 Project Structure
