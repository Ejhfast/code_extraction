# Send email to exchange with attachment in russian file name
mail_coding = 'utf-8'
att_header = Header(os.path.basename(attachment_file_path), mail_coding);
part.add_header('Content-Disposition', 'attachment; filename="%s"' % att_header)
