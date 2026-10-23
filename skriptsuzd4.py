param([switch]$WhatIf)

$servisi = Get-Service | Where-Object { $_.StartType -eq "Automatic" -and $_.Status -eq "Stopped" }

if (@($servisi).Count -eq 0) {
    Write-Output "Tādu servisu nav, skaits: 0"
}
else {
    Write-Output "Atrasti servisi: $(@($servisi).Count)"
    foreach ($s in $servisi) {
        if ($WhatIf) {
            Write-Output "WhatIf: tiktu palaists serviss $($s.Name)"
        }
        else {
            Start-Service -Name $s.Name -ErrorAction SilentlyContinue
            Write-Output "Mēģināju palaist: $($s.Name), statuss tagad: $((Get-Service $s.Name).Status)"
        }
    }
}
