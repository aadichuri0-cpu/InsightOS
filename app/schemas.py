from pydantic import BaseModel,Field

class UserRequest(BaseModel):

    user_id: int = Field(gt=0)

class UserResponse(BaseModel):

    success: bool
    data: dict | None
    error: str | None
    error_type: str | None