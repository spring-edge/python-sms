Python SMS-Lib
================================

This repository contains Python-lib to send sms using Spring Edge (https://www.springedge.com) APIs

Requirements
------------

- [Sign up](https://www.springedge.com/) for a free Trail Messaging account
- Create a new `apikey` from developers section of sms account
- Setup sender name for sms account.
- A working envounment to run Python.


Installation
------------

Place `smsapi.py` in same directory.
Get API key and Sender name.

Usage
-----

Send Text message:

```
from smsapi import SmsApi

apikey = "675031xxxxxxxxxxxx"
sender = "SEDEMO"

sms = SmsApi(apikey, sender)

sms = sms.send_sms(
    recipient="902000xxxx",
    message="test message"
)

```

Success Response:

```
{
 "groupID":xxxxxx,
 "MessageIDs":"xxxxxxx-xx",
 "status":"AWAITED-DLR"
}
```


Or in case of an error:

```
{
  "error":"Invalid Mobile Numbers"
}
```


Support
-------------

For any support or query please visit:
[https://www.springedge.com](https://www.springedge.com)
