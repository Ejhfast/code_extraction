# Programatically DOC/DOCX to PDF
exec("/opt/libreoffice4.0/program/soffice.bin  --headless --convert-to pdf --outdir ".$path."  ".$filename.".".$extension, $output, $return_var);
