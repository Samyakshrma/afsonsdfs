from fastapi import FastAPI, Response, status, HTTPException, Depends
from . import models, schemas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/mail")
def Send_Mail(post: schemas.EmailRequest):
    Data = schemas.EmailRequest(**post.dict())
    models.send_email(Data.Head, Data.Body, Data.email)
    return "Email Sent"
