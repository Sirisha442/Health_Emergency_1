
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from crud import create_profile
from schemas import Profile  # ✅ Make sure this is imported correctly
from database import SessionLocal, engine
from models import Base

app = FastAPI()

# ✅ Create tables (once at startup)
Base.metadata.create_all(bind=engine)



# ✅ DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ This is the key part
@app.post("/submit-profile")
def submit_profile(profile: Profile, db: Session = Depends(get_db)):
    saved_profile = create_profile(db, profile)
    return {"message": "Profile saved successfully", "profile_id": saved_profile.id}
    #return {"message": "Received profile", "name": profile.full_name}

@app.get("/")
def root():
    return {"message": "API is live"}
