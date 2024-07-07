# 0x0B. SSH

## Tasks

### 0. Use a private key
Write a Bash script that uses SSH to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

#### File:
- `0-use_a_private_key`

### 1. Create an SSH key pair
Write a Bash script that creates an RSA key pair with 4096 bits, named `school`, and protected by the passphrase `betty`.

#### File:
- `1-create_ssh_key_pair`

### 2. Client configuration file
Configure your SSH client to use the private key `~/.ssh/school` and refuse password authentication.

#### File:
- `2-ssh_config`

### 3. Let me in!
Add the provided SSH public key to your server for the `ubuntu` user.

#### File:
- `3-add_public_key`

### 4. Client configuration file (w/ Puppet)
Use Puppet to configure your SSH client to use the private key `~/.ssh/school` and refuse password authentication.

#### File:
- `100-puppet_ssh_config.pp`

## Repository
- **GitHub repository:** `alx-system_engineering-devops`
- **Directory:** `0x0B-ssh` 
