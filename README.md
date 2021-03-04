# AXIBO OPENSOURCE API
#### Version: 1.0.0

In this doc we are sharing AXIBO's opensource API. Once you get an AXIBO you can follow the instracutions below:
1. Power AXIBO on
2. Wait 3-5 mins for AXIBO to get booted
3. Check the wifi networks aviablibe around you, you shoud see wifi name: `AXIBO-{Model#}`
4. Connect to that network, it will ask you for a password, and the password is the `{Model#}` everything after the `-` in the wifi name

5. you can navigate from your browser to AXIBO UI by going into the following route: http://10.42.0.1:3000
6. You should see the data coming out of AXIBO, Raw Camera stream, and Pose Images, as well as the json output of POSE detection and the status of the motors.

7. You can control AXIBO using the joystick in the UI, it is located on the top right `+`. Once you click there you can move AXIBO pan and tilt modules.

8. To control AXIBO using the API you can check the postman json or the swagger yaml file in this repo. You can use the documentation below as well as refernece for the API

9. Regarding websockets, you can refer to the python code within this repo. 
there are:
Communication: "ws://"+ipAddress+":2100/ws" 
RAW Cam: "ws://"+ipAddress+":2101/ws"
Pose Cam: "ws://"+ipAddress+":2102/ws"
Pose Data: "ws://"ipAddress":2103/ws"

----
### ROUTES:
#### /system/status

##### GET
###### Summary

Retreive the entire status of AXIBO

###### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | JSON object with the following response | [systemMsg](#systemmsg) |
| 405 | Invalid input |  |

#### /system/wifiInfo

##### GET
###### Summary

Retreive AXIBO current wifi connection

###### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | JSON object with the following response | [Wifi](#wifi) |
| 405 | Invalid input |  |

#### /system/wifi

##### GET
###### Summary

List all the available and saved WIFIs connections

###### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | JSON object with the following response | [WifiList](#wifilist) |
| 405 | Invalid input |  |

##### PUT
###### Summary

Connect to WIFI network

###### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| wifiConfig | body | BSSID, SSID, and Password | No | [ConnectWifi](#connectwifi) |

###### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | JSON object with the following response | [ApiResponse](#apiresponse) |
| 405 | Invalid input |  |

##### DELETE
###### Summary

Delete WIFI network from the saved list

###### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| wifiName | body | Status object that needs to be added to the database | No | object |

###### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | JSON object with the following response | [ApiResponse](#apiresponse) |
| 405 | Invalid input |  |

#### /imaging/cam

##### GET
###### Summary

Retrives a raw image with a timestamp

###### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | JSON object with the following response | [imageRes](#imageres) |
| 405 | Invalid input |  |

#### /imaging/pose

##### GET
###### Summary

Retrives an pose overlay image with a timestamp

###### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | JSON object with the following response | [imageRes](#imageres) |
| 405 | Invalid input |  |

#### /direct-control/config

##### PUT
###### Summary

Move AXIBO to relative position

###### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| wifiConfig | body | Specify the position and the speed to move AXIBO | No | [motorConfig](#motorconfig) |

###### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | JSON object with the following response | [ApiResponse](#apiresponse) |
| 405 | Invalid input |  |

#### /direct-control/home

##### PUT
###### Summary

Home AXIBO to set defualt limits

###### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| wifiConfig | body | Home AXIBO motors | No | [motorHome](#motorhome) |

###### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | JSON object with the following response | [ApiResponse](#apiresponse) |
| 405 | Invalid input |  |

#### /direct-control/move-absolute

##### PUT
###### Summary

Move AXIBO to absolute position

###### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| wifiConfig | body | Specify the position and the speed to move AXIBO | No | [controlCMD](#controlcmd) |

###### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | JSON object with the following response | [ApiResponse](#apiresponse) |
| 405 | Invalid input |  |

#### /direct-control/move-relative

##### PUT
###### Summary

Move AXIBO to relative position

###### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| wifiConfig | body | Specify the position and the speed to move AXIBO | No | [controlCMD](#controlcmd) |

###### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | JSON object with the following response | [ApiResponse](#apiresponse) |
| 405 | Invalid input |  |

#### /direct-control/motion-status

##### GET
###### Summary

Move AXIBO to relative position

###### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | JSON object with the following response | object |
| 405 | Invalid input |  |

#### Models

##### motorConfig

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| panAccel | number |  | No |
| panDeaccel | number |  | No |
| tiltAccel | number |  | No |
| tiltDeaccel | number |  | No |
| panMin | number |  | No |
| panMax | number |  | No |
| tiltMin | number |  | No |
| tiltMax | number |  | No |

##### motorHome

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| pan | boolean |  | No |
| tilt | boolean |  | No |

##### controlCMD

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| position | object |  | No |
| velocity | object |  | No |

##### imageRes

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| timestamp | integer |  | No |
| image | string |  | No |

##### ConnectWifi

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| bssid | string |  | No |
| ssid | string |  | No |
| password | string |  | No |

##### WifiList

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| savedWifiList | [ string ] |  | No |
| availableWifis | [ string ] |  | No |

##### Wifi

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| accessPoint | boolean |  | No |
| networkName | string |  | No |

##### Errors

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| error | string |  | No |

#### systemMsg

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| operation | string | Controller condition <br>_Enum:_ `"in moition"`, `"tracking"`, `"detecting"`, `"idle"` | No |
| progress | integer | _Example:_ `66` | No |
| motionStatus | object |  | No |
| wifi | [Wifi](#wifi) |  | No |
| timeStamp | integer | _Example:_ `123131231231231` | Yes |
| batteryStatus | integer | _Example:_ `59` | Yes |
| backendErrors | [Errors](#errors) |  | Yes |

##### ApiResponse

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| status | integer |  | No |
| message | string |  | No |
