$sakums = (Get-Date).AddHours(-48)

$kludas = Get-WinEvent -FilterHashtable @{LogName = "System"; Level = 2; StartTime = $sakums} -ErrorAction SilentlyContinue

if ($null -eq $kludas) {
    Write-Output "Kļūdu ierakstu skaits pēdējo 48 stundu laikā: 0"
}
else {
    $skaits = @($kludas).Count
    $top = $kludas | Group-Object ProviderName | Sort-Object Count -Descending | Select-Object -First 1
    Write-Output "Kļūdu ierakstu skaits pēdējo 48 stundu laikā: $skaits"
    Write-Output "Visbiežākais avots: $($top.Name), reizes: $($top.Count)"
}
