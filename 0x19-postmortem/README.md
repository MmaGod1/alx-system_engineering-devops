# Postmortem: Nginx Service Outage on Ubuntu Container

# Issue Summary
**• Duration:** September 4, 2024, 10:00 AM to 11:30 AM WAT
**• Impact:** Nginx was not responding on port 80, leading to 100% service downtime for web traffic. Users attempting to access the hosted website encountered a "Connection Refused" error.
**• Root Cause:** Misconfiguration in Nginx settings prevented the server from listening on port 80.

# Timeline
**• 10:00 AM WAT:** Issue detected by a monitoring alert indicating that the web service was unreachable.
**• 10:05 AM WAT:** Engineer verified the alert by attempting to access the web service directly via `curl`, confirming the "Connection Refused" error.
**• 10:10 AM WAT:** Initial investigation focused on network-related issues (firewall rules, IP binding).
**• 10:20 AM WAT:** Misleading path explored; suspected Docker container IP misconfiguration.
**• 10:35 AM WAT:** Issue escalated to the DevOps team for further investigation.
**• 10:45 AM WAT:** Nginx configuration file was reviewed, revealing that Nginx was not correctly bound to port 80.
**• 11:00 AM WAT:** Configuration was corrected, and Nginx service was restarted.
**• 11:05 AM WAT:** Web service functionality was restored, confirmed by a successful `curl` request.
**• 11:30 AM WAT:** Full service restored; incident closed.

# Root Cause and Resolution
**• Root Cause:** The root cause of the issue was a misconfiguration in the Nginx server configuration file. The Nginx service was set to listen on a non-existent IP address instead of listening on all active IPv4 IPs on port 80. 
                  This misconfiguration caused Nginx to fail to bind to port 80, leading to the "Connection Refused" error when attempting to access the web service.
  
**• Resolution:** The issue was resolved by updating the Nginx configuration file to ensure that the server was listening on port 80 for all active IPv4 addresses. The configuration change involved updating the `listen` directive in the Nginx configuration file to `listen 80;`.
                  After the configuration change, the Nginx service was restarted to apply the new settings, which successfully restored the web service.

# Corrective and Preventative Measures
**• Improvements:**
 **• Configuration Validation:** Implement a validation step during Nginx configuration deployment to check that the service is correctly set to listen on the required ports.
 **• Enhanced Monitoring:** Add monitoring for specific ports (like port 80) to alert earlier if the service is not responding.
 **• Documentation Update:** Update the deployment and configuration documentation to include common pitfalls and their resolutions.

**• Tasks:**
  1. **Patch Nginx Configuration:**
       Ensure the default Nginx configuration file includes `listen 80;` by default.
  2. **Implement Configuration Validation:**
       Develop a pre-deployment script to validate that Nginx is configured to listen on the correct ports.
  3. **Enhance Monitoring:**
       Add specific checks for Nginx listening on port 80 in the monitoring system.
  4. **Documentation:**
       Update internal documentation to reflect this incident and provide guidelines on avoiding similar issues in the future.
  5. **Training:**
       Conduct a training session for the engineering team on common Nginx misconfigurations and their resolution.

This postmortem highlights the importance of thorough configuration management and the need for robust monitoring systems to detect and resolve issues promptly.
