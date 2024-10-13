from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.Organization.OrgRouter import router as OrgRouter
from app.User.UserRouter import router as UserRouter

app = FastAPI()

# origins = [
#     "http://localhost:3000"  # Add other origins if needed
# ]

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
    expose_headers=["*"],  # Exposes all headers
)


@app.get("/")
def index():
    return {"message": "Welcome to Organization Management Project"}






app.include_router(OrgRouter, prefix="/org", tags=["Organization"])
app.include_router(UserRouter, prefix="/admin", tags=["User"])


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=3754)