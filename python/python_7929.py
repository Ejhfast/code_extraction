# (Get-Content -Path default.aspx) -replace '(Whats\s?up\s?&lt;%=\s?)(.+?)(\s?%&gt;)', '$1Resource.default_aspx.Title$3' | Set-Content -Path default.aspx
