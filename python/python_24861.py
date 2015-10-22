# Execute system commands using wmi python on remote computer
conn.Win32_Process.Create(CommandLine='cmd.exe /c mkdir temp')
