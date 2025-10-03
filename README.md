# Industrial Edge Gateway

This project demonstrates an **Edge Gateway for Industrial IoT**:
- Simulated PLC → OPC UA server → MQTT broker → InfluxDB
- Grafana dashboards for visualization
- Jenkins pipeline for automated builds

## 📂 Project Structure
- `gateway/` : MQTT → InfluxDB bridge
- `simulator/` : Fake PLC data generator
- `jenkins/` : Jenkins CI/CD pipeline
- `docker-compose.yml` : Starts InfluxDB, Grafana, MQTT
