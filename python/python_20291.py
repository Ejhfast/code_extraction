# Determine if Powershell script started in main scope?
Try {if (get-variable args -scope 1){$true}}
Catch {$false}
