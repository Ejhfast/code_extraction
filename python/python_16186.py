# automatic VMware snaphots creation
vmrun -T vc -h 10.1.1.44 -u root -p vmware snapshot "[datacenter-2/datastore1] CENTER/CENTER.vmx" CleanSnapshot
vmrun -T vc -h 10.1.1.44 -u root -p vmware -gu Administrator -gp P@ssword runScriptInGuest "[datacenter-2/datastore1] CENTER/CENTER.vmx" "" "echo Test &gt; c:\test.txt"
vmrun -T vc -h 10.1.1.44 -u root -p vmware revertToSnapshot "[datacenter-2/datastore1] CENTER/CENTER.vmx" CleanSnapshot
