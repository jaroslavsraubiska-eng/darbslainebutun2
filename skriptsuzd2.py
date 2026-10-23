# Atskaites ID: RVT-4417
# Atmiņas lauku atradu ar Get-Process | Get-Member, tas ir WorkingSet64
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 |
    Sort-Object WorkingSet64 |
    Select-Object Name, Id, @{Name = "Atmiņa MB"; Expression = { "{0:F1}" -f ($_.WorkingSet64 / 1MB) }}
