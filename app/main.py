from typing import IO, Optional

from fastapi import FastAPI
from fastapi.datastructures import UploadFile
from fastapi.params import File
from starlette.responses import HTMLResponse, StreamingResponse

from similarity import generate_similarity_xlsx

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <body>
        <h1>This page is inspired by nordic design. Simple and clean.</h1>
        <label for="file">Please upload the csv </label>
        <br/>
        <br/>
        <form action="check_similarity" method="post" enctype="multipart/form-data">
            <input type="file" id="file" name="file" accept="text/csv" />
            <br/>
            <br/>
            <br/>
            <input type="submit" value="Generate" />
        </form>
    </body>
    """


@app.post("/check_similarity/")
async def create_upload_file(file: UploadFile = File(...)) -> StreamingResponse:
    stream = generate_similarity_xlsx(file)
    response = StreamingResponse(
        iter([stream.getvalue()]),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response.headers["Content-Disposition"] = "attachment; filename=similarity.xlsx"
    stream.close()
    return response
