$robeza = 20   # GB, zem šīs vērtības rādu brīdinājumu

$diski = Get-CimInstance Win32_LogicalDisk -Filter "DriveType = 3"

foreach ($d in $diski) {
    $kopa = [math]::Round($d.Size / 1GB, 1)
    $brivs = [math]::Round($d.FreeSpace / 1GB, 1)
    Write-Output "Disks $($d.DeviceID) - kopā: $kopa GB, brīvs: $brivs GB"
    if ($brivs -lt $robeza) {
        Write-Output "BRĪDINĀJUMS: diskā $($d.DeviceID) ir mazāk nekā $robeza GB brīvas vietas!"
    }
}
