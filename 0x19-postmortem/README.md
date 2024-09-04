# Postmortem: Nginx Service Outage on Ubuntu Container


#Issue Summary:
   **• Duration:** September 4, 2024, 10:00 AM to 11:30 AM WAT (A short but intense 90 minutes of “Where did my website go?”)
  **• Impact:** 100% of users faced the dreaded “Connection Refused” error. Think of it as everyone arriving at your party, only to find the door locked and the lights off.
  **• Root Cause:** Nginx was so shy that it refused to open the door on port 80.

# Timeline:
  **• 10:00 AM:** Monitoring alert goes off, like an angry alarm clock reminding us that something is terribly wrong.
  **• 10:05 AM:** Engineer tries to access the website and gets a “Connection Refused” message. Cue the dramatic sigh.
  **• 10:10 AM:** Initial checks focus on network issues, suspecting the firewall was playing bouncer and blocking entry. Spoiler alert: It wasn’t.
  **• 10:20 AM:** Wild goose chase begins, with engineers checking if Docker’s IPs decided to take a vacation.
  **• 10:35 AM:** DevOps team is summoned to save the day, capes optional.
  **• 10:45 AM:** Eureka moment! The problem was Nginx being set to listen on the wrong IP, like trying to catch a bus that never stops at your station.
  **• 11:00 AM:** Nginx configuration is fixed, and the service is restarted. The website is back online, party resumes!
  **• 11:30 AM:** All systems green, and the incident is officially closed. High-fives all around.

# Root Cause and Resolution

**Root Cause:**
• The root of all evil (well, this time at least) was a misconfiguration in the Nginx server settings. Instead of opening its doors wide on port 80 to welcome visitors, Nginx was trying to listen on an IP address that didn’t exist. It’s like Nginx was waiting for guests at the wrong address, wondering why no one showed up.

**Resolution:**
 • After a few rounds of "Where’s Waldo" with the server settings, the issue was finally found in the Nginx configuration file. The `listen` directive was corrected to `listen 80;`, meaning Nginx was finally told, "Stand right here, and greet everyone who comes through port 80." With a quick restart of the Nginx service, the problem was resolved, and the party could finally begin.

# Corrective and Preventative Measures

**Improvements:**
• We’ve learned that even servers need clear instructions—no more guessing where to stand. Here’s what we can do to avoid another mix-up:
  1. **Improve Configuration Validation:** Implement a system where Nginx configurations are automatically checked to ensure they are pointing to the correct IP and port before deployment. No more wandering servers!
  2. **Enhanced Monitoring:** Add specific monitoring for critical ports like 80. If Nginx starts listening at the wrong door again, we’ll catch it immediately.
  3. **Documentation Update:** Let’s write down these lessons so the next engineer doesn’t have to play hide and seek with the server settings.

**TODO:**
1. **Patch Nginx Configuration:**
   • Update the default configuration to ensure that Nginx listens on all active IPv4 addresses on port 80.
2. **Automate Configuration Checks:**
   • Develop a script or integrate a tool to automatically validate Nginx configurations before deployment.
3. **Enhance Monitoring:**
   • Add port-specific monitoring to our alert system so we know right away if Nginx is not listening where it should be.
4. **Update Documentation:**
   • Add a section to our internal wiki on common Nginx misconfigurations and how to fix them. Include a note on why Nginx shouldn’t be left to guess its own IP.

This postmortem highlights the importance of thorough configuration management and the need for robust monitoring systems to detect and resolve issues promptly.
