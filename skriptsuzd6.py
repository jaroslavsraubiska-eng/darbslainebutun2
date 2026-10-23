$draiveri = Get-CimInstance Win32_PnPSignedDriver |
    Where-Object { $_.DriverProviderName -and $_.DriverProviderName -notlike "Microsoft*" } |
    Select-Object DeviceName, DriverProviderName, DriverVersion, DriverDate

$draiveri | Export-Csv -Path ".\draiveri.csv" -NoTypeInformation -Encoding UTF8

$rindas = (Get-Content ".\draiveri.csv").Count
Write-Output "Rindu skaits CSV failā: $rindas"
$draiveri | Format-Table
