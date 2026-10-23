$t1 = Measure-Command { $a = Get-Service -Name Spooler }
$t2 = Measure-Command { $b = Get-CimInstance Win32_Service -Filter "Name = 'Spooler'" }

Write-Output "Get-Service: $($a.Name), $($a.Status)"
Write-Output "Get-CimInstance: $($b.Name), $($b.State)"
Write-Output "Get-Service laiks: $([math]::Round($t1.TotalMilliseconds, 2)) ms"
Write-Output "Get-CimInstance laiks: $([math]::Round($t2.TotalMilliseconds, 2)) ms"
