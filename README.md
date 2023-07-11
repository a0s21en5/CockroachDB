# Setting up CockroachDB on Windows

## Prerequisites
- Windows operating system

## Steps

# Create a new folder, for example: 
`C:\CockroachDB`.

# Open PowerShell with Admin rights and execute the following command:
`
   $ErrorActionPreference = "Stop"; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;$ProgressPreference = 'SilentlyContinue'; $null = New-Item -Type Directory -Force $env:appdata/cockroach; Invoke-WebRequest -Uri https://binaries.cockroachdb.com/cockroach-v23.1.5.windows-6.2-amd64.zip -OutFile cockroach.zip; Expand-Archive -Force -Path cockroach.zip; Copy-Item -Force "cockroach/cockroach-v23.1.5.windows-6.2-amd64/cockroach.exe" -Destination $env:appdata/cockroach; $Env:PATH += ";$env:appdata/cockroach"
`

# After the successful execution of the above command, the following folder will be created:
`
C:\CockroachDB\cockroach\cockroach-v23.1.5.windows-6.2-amd64
`
# pen the environment variables settings from the Start menu:

* Click on "Environment Variables."
* Under the "System variables" section, locate and select  
* the "Path" variable, then click on the "Edit" button.
Click on the "New" button and paste the following path:
`
C:\CockroachDB\cockroach\cockroach-v21.2.0-rc.3.windows-6.2-amd64
`
* Click on the "OK" button.

# Open a new instance of PowerShell and execute the following command:
`
cockroach version
`

# In the same PowerShell window, execute the following command:
`
cockroach start-single-node --insecure --listen-addr=localhost:26257 --http-addr=localhost:8080
`

# Note: Close the PowerShell window only when you are not using or operating the database. To connect using an IP address, use the following command:
`
cockroach start-single-node --insecure --listen-addr=172.16.1.123:26257 --http-addr=172.16.1.123:8080
`

# To access the CockroachDB web interface, open the following link in your browser:
`http://localhost:8080/`

# Open the command prompt and execute the following command to access the CockroachDB SQL shell:
`
cockroach sql --insecure --host=localhost:26257
`

# To connect using an IP address, use the following command:
`
cockroach sql --insecure --host=172.16.1.123:26257
`

# If you prefer a graphical SQL editor, you can download SQL Editor (SQL Wizard) from the following link:
`
https://dbeaver.io/download/
`
