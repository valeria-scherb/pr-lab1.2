#!/usr/bin/env python
"""
Main program
"""

import asyncio
import json
import websockets

from strategy import Strategy

# Settings
width = 15
total = 1
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
        json.loads(await ws.recv())
        st = Strategy()
        await ws.send(ready_message)
        problem = json.loads(await ws.recv())
        step = problem['data']['step']
        heatmap = problem['data']['heatmap']
        guesses = st.guess_bars(heatmap, repeats)
        await ws.send(json.dumps({'data': {'step': step, 'guesses': guesses}}))
        result = json.loads(await ws.recv())
        print(result)
        await ws.send(bye_message)
        print("Finished!")
        summary = json.loads(await ws.recv())
        print("Loss", summary['data']['loss'])


asyncio.get_event_loop().run_until_complete(main())
