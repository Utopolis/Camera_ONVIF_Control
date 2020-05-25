import onvifconfig
import time


if __name__ == '__main__':

    ip_camera='xx.xx.xx.xx'
    port = 80
    user = 'admin'
    password = 'password'
    
    #Do all setup initializations
    ptz = onvifconfig.ptzcam(ip_camera, port, user, password)

#*****************************************************************************
# IP camera motion tests
#*****************************************************************************
    print ('Starting tests...')
    
    #Save the current localisation
    x, y, Zoom, PanTilt = ptz.current_loc()
    ptz.get_preset()
    #Go back to preset
    #ptz.goto_preset('special_preset')
    #To let the camera have the time to move
    time.sleep(5)
    
    #Go back to previous position
    ptz.position_initial(x, y, Zoom, PanTilt)
    # ptz.set_preset('hello', 3)

    exit()