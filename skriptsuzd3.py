$darbojas = 0
$aptureti = 0

foreach ($s in Get-Service) {
    if ($s.Status -eq "Running") {
        $darbojas++
    }
    if ($s.Status -eq "Stopped") {
        $aptureti++
    }
}

Write-Output "Darbojas: $darbojas"
Write-Output "Apturēti: $aptureti"
Write-Output "Summa: $($darbojas + $aptureti)"
