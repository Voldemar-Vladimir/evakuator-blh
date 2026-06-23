from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from mako.lookup import TemplateLookup
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = TemplateLookup(directories=["templates"])

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    template = templates.get_template("index.html")
    return HTMLResponse(template.render())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)