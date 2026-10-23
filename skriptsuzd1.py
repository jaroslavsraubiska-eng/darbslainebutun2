$os = Get-CimInstance Win32_OperatingSystem
$procesi = (Get-Process).Count

Write-Output "Datora nosaukums: $env:COMPUTERNAME"
Write-Output "Operētājsistēmas nosaukums: $($os.Caption)"
Write-Output "Būvējuma numurs: $($os.BuildNumber)"
Write-Output "PowerShell versija: $($PSVersionTable.PSVersion)"
Write-Output "Datums un laiks: $(Get-Date)"
Write-Output "Darbojošos procesu skaits: $procesi"
