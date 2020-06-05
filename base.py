from speedtest import Speedtest

# debugmode
debugmode = 0

st = Speedtest()

# debug
if debugmode:
    print(f'Download: {st.download()}')
    print(f'Upload: {st.upload()}')
    st.get_best_server([])
    print(f'Ping: {st.results.ping}')

# functons
def get_upload_speed():
    print('UPLOAD SPEED: Wait a few seconds...')
    return int(st.upload())

def get_download_speed():
    print('DOWNLOAD SPEED: Wait a few seconds...')
    return int(st.download())

def get_ping():
    print('Wait a few seconds...')
    st.get_best_server([])
    return int(st.results.ping)