## Third-Party Vendor Agreements
Our Industrial AI solution relies on multiple external vendors for hardware (NVIDIA Jetson AGX) and ICS security software (Nozomi, Vectra). This document captures key contractual terms, licensing, and synergy points.

---

### 1. HPC Device Vendor (NVIDIA)
- **Hardware**: Jetson AGX boards for on-prem HPC inference.
- **Licensing**: 
  - NVIDIA JetPack SDK usage license. 
  - TensorRT optimization requires acceptance of NVIDIA EULA.
- **Support SLA**:
  - Standard business hours support from NVIDIA for hardware issues.
  - Extended warranty recommended if HPC must run 24/7 in harsh smelter environments.
- **Data Usage**:
  - Telemetry from Jetson boards (temperature, GPU usage) can be shared with NVIDIA for troubleshooting. 
  - Must ensure no PII or ICS confidential data is inadvertently included.

### 2. ICS Security Vendor (Nozomi or Vectra)
- **Software**: ICS anomaly detection, threat intel feeds.
- **Licensing**:
  - Typically annual subscription with node-based or sensor-based licensing.
  - Additional cost for advanced threat intelligence or managed SOC integration.
- **Integration**:
  - Our solution taps into Nozomi/Vectra logs for correlation with YOLO defect spikes.
  - Must confirm we have an API or CSV export license for real-time ingestion.
- **Support SLA**:
  - 24/7 ICS security incident hotline recommended if critical production lines might be targeted by advanced threats.
- **Data Usage**:
  - ICS logs are typically anonymized or aggregated before leaving the premises.
  - Vendor must comply with local data sovereignty laws if logs are shared to their cloud.

### 3. Synergy & Co-Marketing Opportunities
- Potential to co-market the “Industrial AI + ICS Security” synergy at manufacturing expos or whitepapers.
- Joint press releases: e.g., “EGA and Nozomi Team Up for Next-Gen ICS + AI Detection.”

### 4. Renewal & Contract Terms
- HPC device warranties typically 2–3 years, extended service recommended for on-site spares.
- ICS security software annual renewal with an optional multi-year discount.
- Non-disclosure agreements to protect ICS environment specifics.

---

### Risk & Mitigation
- **Vendor Lock-In**: Evaluate alternative HPC boards or ICS tools to avoid single-vendor dependency.
- **License Expiry**: Track license renewal timelines in a central compliance calendar.
- **Cost Overruns**: Regularly check usage-based licensing if ICS sensor expansions occur.
