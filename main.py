#!/usr/bin/env python
"""
Main program
"""

import asyncio
import json
import websockets

from recognizer import Recognizer

# Settings
width = 15
total = 50
repeats = 20
# End

ready_message = json.dumps({'data': {'message': "Ready"}})
bye_message = json.dumps({'data': {'message': 'Bye'}})
task = 'second'
session = 'valeria'
settings = {
    'width': width,
    'loss': 'L1',
    'totalSteps': total,
    'repeats': repeats
}


async def main():
    url = 'wss://sprs.herokuapp.com/{}/{}'.format(task, session)
    async with websockets.connect(url) as ws:
        await ws.send(json.dumps({'data': settings}))
        req = json.loads(await ws.recv())
        print(req)


asyncio.get_event_loop().run_until_complete(main())
