import ambient
import time

try:        
    AMBIENT_CHANNEL_ID = int(os.environ['AMBIENT_CHANNEL_ID'])
    AMBIENT_WRITE_KEY = os.environ['AMBIENT_WRITE_KEY']
except KeyError as e:
    sys.exit('Couldn\'t find env: {}'.format(e))

am = ambient.Ambient(AMBIENT_CHANNEL_ID, AMBIENT_WRITE_KEY)

def get_temp():
    return int(open('/sys/class/thermal/thermal_zone0/temp').read())/1000.0

def request():
    am.send({
        'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'd1': get_temp(),
    })

if __name__ == '__main__':
    while True:
        request()
        time.sleep(60)
    
