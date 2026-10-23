$procesi = (Get-Process).Count
$darbojas = @(Get-Service | Where-Object { $_.Status -eq "Running" }).Count
$aptureti = @(Get-Service | Where-Object { $_.Status -eq "Stopped" }).Count
$sakums = (Get-Date).AddHours(-48)
$kludas = @(Get-WinEvent -FilterHashtable @{LogName = "System"; Level = 2; StartTime = $sakums} -ErrorAction SilentlyContinue).Count

Write-Output "Procesu skaits: $procesi"
Write-Output "Darbojošies servisi: $darbojas"
Write-Output "Apturētie servisi: $aptureti"
Write-Output "Kļūdu skaits 48 h: $kludas"

foreach ($d in Get-CimInstance Win32_LogicalDisk -Filter "DriveType = 3") {
    Write-Output "Brīvā vieta diskā $($d.DeviceID): $([math]::Round($d.FreeSpace / 1GB, 1)) GB"
}
