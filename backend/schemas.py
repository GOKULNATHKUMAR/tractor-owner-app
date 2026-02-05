from pydantic import BaseModel

class OwnerCreate(BaseModel):
    name: str
    mobile: str
    village: str | None = None

class OwnerResponse(OwnerCreate):
    id: int

    class Config:
        from_attributes = True
