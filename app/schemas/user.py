import re

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.models.users import UserRole

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
PHONE_REGEX = re.compile(r"^\+?[1-9]\d{1, 14}$")

class UserCreate(BaseModel):
    email: str = Field(min_length=6, max_length=255)
    phone: str | None = Field(default=None, min_length=10, max_length=20)
    password: str = Field(min_length=8, max_length=255)

    @field_validator("phone")
    @classmethod
    def validate_and_normalize_phone(cls, value:str | None) -> str | None:
        if value is None:
            return None

        cleaned_phone = re.sub(r"\s\-\(\)", "", value)

        if cleaned_phone.startswith("8") and len(cleaned_phone) == 11:
            cleaned_phone = '+7' + cleaned_phone[1:]
        elif not cleaned_phone.startswith("+"):
            cleaned_phone = "+" + cleaned_phone

        if not PHONE_REGEX.match(cleaned_phone):
            raise ValueError("Неккоректный phone")

        return cleaned_phone

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        email = value.strip().lower()

        if not EMAIL_REGEX.match(email):
            raise ValueError("Некоректный email")

        return email

class UserLogin(BaseModel):
    email: str = Field(min_length=6, max_length=255)
    password: str = Field(min_length=8, max_length=255)

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        email = value.strip().lower()

        if "@" not in email:
            raise ValueError("Email must contain @")

        return email

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    is_active: bool
    role: UserRole


UserRead = UserResponse