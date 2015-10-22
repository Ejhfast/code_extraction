# Need to replace some token in a file with the name of the file
(Get-Content -Path contact.aspx) -replace '(Hallo\s?&lt;%=\s?)(.+?)(\s?%&gt;)', '$1Resource.contact_aspx.Title$3' | Set-Content -Path contact.aspx
