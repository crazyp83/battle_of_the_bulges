import dropbox
import os

# Initialize Dropbox client with access token
access_token = os.getenv('DROPBOX_ACCESS_TOKEN')
dbx = dropbox.Dropbox(access_token)

# File paths
local_file_path = os.getenv('IPA_PATH')
dropbox_file_path = '/BattleoftheBulges.ipa'

# Chunk size for large file uploads (4 MB)
chunk_size = 4 * 1024 * 1024

# Open and upload the file
with open(local_file_path, 'rb') as f:
    file_size = os.path.getsize(local_file_path)
    if file_size <= chunk_size:
        # For small files, upload directly
        dbx.files_upload(f.read(), dropbox_file_path, mode=dropbox.files.WriteMode.overwrite)
    else:
        # For large files, use upload sessions
        upload_session_start_result = dbx.files_upload_session_start(f.read(chunk_size))
        cursor = dropbox.files.UploadSessionCursor(
            session_id=upload_session_start_result.session_id,
            offset=f.tell()
        )
        while f.tell() < file_size:
            if (file_size - f.tell()) <= chunk_size:
                dbx.files_upload_session_finish(
                    f.read(chunk_size),
                    cursor,
                    dropbox.files.CommitInfo(dropbox_file_path)
                )
            else:
                dbx.files_upload_session_append_v2(f.read(chunk_size), cursor)
                cursor.offset = f.tell()

# Create and output a shareable link
link_response = dbx.sharing_create_shared_link_with_settings(dropbox_file_path)
print(link_response.url)