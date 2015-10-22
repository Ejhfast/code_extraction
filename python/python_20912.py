# PyDrive: cannot write file to specific GDrive folder
gfile = drive.CreateFile({'title':'dummy.csv', 'mimeType':'text/csv',
        "parents": [{"kind": "drive#fileLink","id": tgt_folder_id}]})
