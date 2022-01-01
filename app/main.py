from typing import IO, Optional

from fastapi import FastAPI
from fastapi.datastructures import UploadFile
from fastapi.params import File
from starlette.responses import StreamingResponse

from similarity import generate_similarity_xlsx

app = FastAPI()

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
