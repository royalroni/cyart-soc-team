# Task 02 – SOAR Playbook Development

## Overview

This task focuses on creating a simple SOAR (Security Orchestration, Automation, and Response) playbook to automate the response to phishing-related incidents.

---

## Objective

The main objective was to reduce manual effort in handling alerts by automating detection, validation, and response steps.

---

## Tools Used

* Wazuh (Alert Detection)
* TheHive (Case Management)
* CrowdSec (IP Blocking – simulated)
* Google Docs (Documentation)

---

## Playbook Workflow

The playbook was designed with the following steps:

1. Detect phishing alert from Wazuh
2. Check IP reputation
3. Block malicious IP (simulated using CrowdSec)
4. Create incident case in TheHive

---

## Playbook Execution Results

| Playbook Step | Status  | Notes                       |
| ------------- | ------- | --------------------------- |
| Check IP      | Success | IP identified as suspicious |
| Block IP      | Success | IP blocking simulated       |
| Create Case   | Success | Case created in TheHive     |

---

## Screenshots Included

* Alert Detection (Wazuh)
* IP Blocking (Simulation)
* Case Creation (TheHive)

---

## Summary

The SOAR playbook successfully demonstrated how phishing incidents can be handled automatically. It helped in reducing response time and ensured proper incident tracking using TheHive.

---

## Note

Some actions like IP blocking were simulated due to lab limitations, but the workflow represents real-world SOC operations.
