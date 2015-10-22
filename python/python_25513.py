# GAE Python GCS filename accesses old file
with gcs.open(new_zf.gcs_filename, 'w', content_type=b'multipart/x-zip',
                  options={b'x-goog-acl': b'public-read', b'cache-control': b'private, max-age=0, no-cache'}) as nzf:
