# Born2BeRoot

*This project has been created as part of the 42 curriculum by skhachat.*

---

## Description

Born2BeRoot is a system administration project from the 42 school curriculum. The goal is to create and configure a virtual machine following strict rules, setting up a secure Linux server from scratch.

### Operating System: Debian

**Debian** was chosen over Rocky Linux for the following reasons:

| | Debian | Rocky Linux |
|---|---|---|
| **Target audience** | General purpose, widely used | Enterprise (RHEL clone) |
| **Package manager** | APT (easy, well-documented) | DNF/YUM |
| **Community & docs** | Huge, beginner-friendly | Smaller, enterprise-focused |
| **Stability** | Extremely stable | Stable (follows RHEL) |
| **Learning curve** | Lower | Higher |
| **Recommended for 42** | ✅ Yes | Possible but harder |

**Debian advantages:** massive documentation, easier package management with APT, more beginner-friendly, widely used in the industry.

**Debian disadvantages:** older package versions compared to rolling distros, less SELinux integration out of the box.

**Rocky Linux advantages:** closer to enterprise environment (RHEL-compatible), SELinux by default, good for learning enterprise sysadmin.

**Rocky Linux disadvantages:** steeper learning curve, less beginner documentation, overkill for this project.

---

### Main Design Choices

**Partitioning:**
Encrypted LVM partitioning was used with separate logical volumes for `/`, `/home`, `/var`, `/srv`, `/tmp`, `/var/log`, and swap. This follows security best practices by isolating system areas and allowing flexible resizing.

**Security policies:**
- Strong password policy enforced via `libpam-pwquality` (minimum length, complexity, expiration)
- `sudo` configured with restricted TTY, log of all commands, and limited authentication attempts
- AppArmor enabled for mandatory access control

**User management:**
- A non-root user created and added to `sudo` and `user42` groups
- Root login disabled via SSH

**Services installed:**
- **SSH** on port 4242 (root login disabled)
- **UFW** firewall (only ports 4242, 80 allowed)
- **Lighttpd** — lightweight web server
- **MariaDB** — database for WordPress
- **PHP** — backend for WordPress
- **WordPress** — functional CMS
- **Redis** — in-memory cache server (chosen as the additional service)

---

### Comparisons

#### AppArmor vs SELinux

| | AppArmor | SELinux |
|---|---|---|
| **Used in** | Debian, Ubuntu | Rocky, Fedora, RHEL |
| **Configuration** | Profile-based (per application) | Label-based (per file/process) |
| **Complexity** | Easier to configure | More complex but more powerful |
| **Default on Debian** | ✅ Yes | ❌ No |

AppArmor was used in this project as it is the default MAC system on Debian and easier to manage for a first server setup.

#### UFW vs firewalld

| | UFW | firewalld |
|---|---|---|
| **Used in** | Debian, Ubuntu | Rocky, Fedora, RHEL |
| **Interface** | Simple CLI | Dynamic, zone-based |
| **Complexity** | Very simple | More complex |
| **Default on Debian** | ✅ Yes (after install) | ❌ No |

UFW (Uncomplicated Firewall) was used as it provides a simple interface to `iptables` and integrates naturally with Debian.

#### VirtualBox vs UTM

| | VirtualBox | UTM |
|---|---|---|
| **Platform** | Windows, Mac, Linux | Mac only (ARM & x86) |
| **Performance on Apple Silicon** | Poor (x86 emulation) | Excellent (native ARM) |
| **Open source** | ✅ Yes | ✅ Yes (free version) |
| **Ease of use** | Good | Good |
| **42 recommendation** | Primary | Alternative for Mac M1/M2 |

VirtualBox is the standard tool used at 42. UTM is the recommended alternative for Apple Silicon Macs.

---

## Instructions

### Requirements
- VirtualBox (or UTM on Apple Silicon)
- Debian ISO (version 12 recommended)

### Setup
1. Create a new VM in VirtualBox (4096MB RAM, 30GB storage)
2. Attach the Debian ISO and install with encrypted LVM partitioning
3. Follow the configuration steps: sudo, SSH, UFW, password policy, AppArmor
4. Set up bonus services: Lighttpd, MariaDB, PHP, WordPress, Redis

### Accessing the server
Connect via SSH from the host machine:
```bash
ssh skhachat@localhost -p 4242
```

### Accessing WordPress
Open in browser on the host machine:
```
http://localhost:8081
```
*(Port Forwarding: Host 8081 → Guest 80)*

### Monitoring script
The monitoring script runs every 10 minutes via cron and broadcasts system info to all terminals:
```bash
sudo crontab -u root -e
```

---

## Resources

- [Debian Official Documentation](https://www.debian.org/doc/)
- [Born2BeRoot Guide (GitBook)](https://noreply.gitbook.io/born2beroot)
- [UFW Documentation](https://help.ubuntu.com/community/UFW)
- [AppArmor Wiki](https://wiki.debian.org/AppArmor)
- [LVM Guide](https://wiki.debian.org/LVM)
- [Redis Documentation](https://redis.io/documentation)
- [WordPress Documentation](https://wordpress.org/documentation/)
- [Lighttpd Documentation](https://wiki.lighttpd.net)

### AI Usage
Claude (Anthropic) was used during this project for:
- Troubleshooting connection issues between VirtualBox Port Forwarding and the host machine
- Guidance on installing and enabling Redis as the additional service
- Writing this README
