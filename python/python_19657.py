# Passing .csv values to a script in Powershell
Get-Content C:\PathToInputFile.txt | ForEach-Object { .\MyPermissionsScript.ps1 $_ } | Export-Csv C:\Scripts\ScanResults.csv -NoTypeInformation
