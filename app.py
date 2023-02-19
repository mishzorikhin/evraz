from typing import Union

import uvicorn
from fastapi import FastAPI

from main_page import get_first_date


from fastapi import FastAPI, WebSocket, websockets
from starlette.websockets import WebSocketDisconnect
import websockets




from second_page import get_exhauster_data

app = FastAPI()


@app.get("/second")
def read_root():
    return get_exhauster_data()




@app.get("/main_page")
def read_item():
    return get_first_date()


users = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    users.append(websocket)
    
    try:
        
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    
    except WebSocketDisconnect as e:
        users.remove(websocket)
        
    
         
    
        
        
        
        



@app.get("/new")
async def read_root():

    for i in users:
        print(i)
        await i.send_json(
            get_first_date()
        )

    

    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4242)
