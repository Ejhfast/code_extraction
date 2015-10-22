# Stream rdiff - delta differencing?
rdiff signature oldfile oldfile.sig
rdiff delta oldfile.sig newfile | gzip -c | gpg -e -r ... &gt; compressed_encrypted_delta
