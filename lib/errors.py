# Custom library imports:
from .config import *



class KsInvalidTokenError(Exception):
    def __init__(self):
        super().__init__('Invalid API token. After creating an account, generate a new one at https://kleenscan.com/profile.')



class KsApiError(Exception):
    def __init__(self, message):
        super().__init__(message)



class KsFileTooLargeError(Exception):
    def __init__(self):
        super().__init__(f'The provided file is too large for the kleenscan API (Max: {MAX_FILE_MB} MB).')



class KsFileEmptyError(Exception):
    def __init__(self):
        super().__init__(f'The provided file is empty, provide a file with data.')



class KsRemoteFileTooLargeError(Exception):
    def __init__(self):
        super().__init__(f'The remote file is too large for the kleenscan API (Max: {MAX_FILE_MB} MB).')



class KsGetFileInfoFailedError(Exception):
    def __init__(self, message: str):
        super().__init__(f'Failed to get file info, HTTP statuc code: {message}')



class KsNoFileHostedError(Exception):
    def __init__(self):
        super().__init__(f'No file hosted on provided URL/server. Please provide a URL/server which hosts a file, e.g. https://malicious.com/file.exe')



class KsFileDownloadFailedError(Exception):
    def __init__(self, message: str):
        super().__init__(f'Failed to download file, HTTP status code: {message}')



class KsDeadLinkError(Exception):
    def __init__(self, message: str):
        super().__init__(f'The URL/server hosting the file cannot be conneceted to: {message}')
