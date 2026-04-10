#  Task 5: Evidence Analysis

##  Objective
To analyze collected forensic evidence using Velociraptor and maintain chain-of-custody integrity.

---

##  Tools Used
- Velociraptor (Endpoint Forensics)
- Windows PowerShell (Hash Verification)
- FTK Imager (conceptual)

---

##  Evidence Collection Process

### 1. Client Identification
- Connected client: **Roni (Windows System)**
- Verified system details (OS, IP, Agent version)

📸 Screenshot:
`screenshots/task5_client_overview.png`

---

### 2. Artifact Selection (Network Analysis)
Artifact used:
- `Windows.Network.Netstat`

- Used to collect open network connections
- Helps identify suspicious communication

📸 Screenshot:
`screenshots/task5_artifact_selection.png`

---

### 3. Artifact Collection
- Executed artifact collection
- Data successfully collected from endpoint

📸 Screenshot:
`screenshots/task5_collect_artifact.png`

---

### 4. Evidence Collection Status
- Collection completed successfully
- Total rows collected: **106**
- No errors during execution

📸 Screenshot:
`screenshots/task5_collection_completed.png`

---

### 5. Evidence Analysis (Network Connections)

- Observed active processes:
  - `svchost.exe`
  - `System`
  - `velociraptor.exe`

- Ports detected:
  - 135, 139 (Windows services)
  - 8000 (Velociraptor communication)

- Localhost connections identified (127.0.0.1)

📸 Screenshots:
- `screenshots/task5_netstat_result1.png`
- `screenshots/task5_netstat_result2.png`

---

### 6. Hash Verification (Chain-of-Custody)

Command used:
```powershell
netstat -ano > netstat_log.txt
certutil -hashfile netstat_log.txt SHA256