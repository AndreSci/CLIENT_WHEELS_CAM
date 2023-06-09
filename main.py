""" For start, you need enter in terminal:
uvicorn main:app --port 8090 --reload
"""

from fastapi import FastAPI, status, HTTPException

import uvicorn

from routes.events import event_router

app = FastAPI()


# Register routes
app.include_router(event_router, prefix="/event")


if __name__ == "__main__":
    # Напоминание для запуска через терминал
    # uvicorn main:app --port 8080 --reload
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
