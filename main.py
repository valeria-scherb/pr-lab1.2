#!/usr/bin/env python
"""
Main program
"""

import asyncio
import json
import websockets

from strategy import Strategy
from test_strategy import TestStrategy

# Settings
width = 15
total = 20
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
        ts = TestStrategy()
        cl = 0
        print("Start processing", total, "tasks")
        for step in range(0, total):
            await ws.send(ready_message)
            problem = json.loads(await ws.recv())
            cs = problem['data']['step']
            heatmap = problem['data']['heatmap']
            guesses = st.guess_bars(heatmap, repeats)
            await ws.send(json.dumps({'data': {'step': cs, 'guesses': guesses}}))
            result = json.loads(await ws.recv())
            sl = ts.measure_loss(result['data']['solutions'], guesses)
            print("Loss in", cs, "is", sl)
            cl += sl
        await ws.send(bye_message)
        print("Finished!")
        summary = json.loads(await ws.recv())
        print("Server loss", summary['data']['loss'])
        print("Client loss", cl)


asyncio.get_event_loop().run_until_complete(main())
