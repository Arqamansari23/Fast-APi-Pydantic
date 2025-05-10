# This file is responsible for validating the input data passed to model to predict the iris species 

from pydantic import BaseModel, Field

class IrisInputValidator(BaseModel):
    sepal_length: float = Field(..., gt=0, description="Length of the sepal in cm")
    sepal_width: float = Field(..., gt=0, description="Width of the sepal in cm")
    petal_length: float = Field(..., gt=0, description="Length of the petal in cm")
    petal_width: float = Field(..., gt=0, description="Width of the petal in cm")

