# this part will accept .txt
# Simple!!! GET data return RESPONSE

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from services.storage import create_essay_record
from constants import _ESSAY_MIN_LENGTH
from services.storage import load_user_profile, get_essay

# In main.py it will be connected by prefix   /essays...
router = APIRouter()


@router.post("/upload/file")
async def upload_essay_file(
    user_id: str = Form(...),  # get user ID out of form
    file: UploadFile = File(...),  # get file out of form
):
    """
    Endpoint to upload essay by  file.txt
    Get user ID and file.txt, read it,
    decode to str and send to be saved as JSON.
    """

    # check if user is registered in the system
    user = load_user_profile(user_id)
    if not user:  # check if user is registered in the system
        raise HTTPException(
            status_code=404,
            detail=f"user with ID: {user_id} not found. Please pass registration first!",
        )

    # Validation: check that file is  .txt format
    if not file.filename or not file.filename.endswith(".txt"):
        raise HTTPException(
            status_code=400, detail="Format is not correct. Allowed .txt format only"
        )

    try:
        # Async reading, get bytes
        file_bytes = await file.read()

        # Decoding: transform bytes into regular Python str
        # 'utf-8' very important for reading another languages
        essay_text = file_bytes.decode("utf-8").replace("\r\n", "\n")

        # Check for empty file
        if not essay_text.strip():
            raise HTTPException(
                status_code=400,
                detail="File is empty. Please, upload file with content/essay",
            )

        # Saving: function call, to create JSON file
        essay_id = create_essay_record(user_id=user_id, text=essay_text)

        # Client answer: return status SUCCESS and essay ID
        return {
            "success": True,
            "message": f"File '{file.filename}' successfully uploaded and saved",
            "essay_id": essay_id,
            "status": "pending",
        }

    except UnicodeDecodeError:
        # If file is saved in wrong encoding (not UTF-8), raise exception
        raise HTTPException(
            status_code=400,
            detail="Encoding of file is wrong. Make shore, that file is saved as UTF-8.",
        )
    except Exception as e:
        # Another exception
        raise HTTPException(
            status_code=500, detail=f"Server error is occurred: {str(e)}"
        )


@router.post("/upload/text")
async def upload_essay_text(
    user_id: str = Form(...),  # get user ID
    text: str = Form(...),  # get text out of form
):
    """
    Endpoint for uploading essay by text field on client side by typing
    Accept user ID and text, then save it
    """

    # check if user is registered in the system
    user = load_user_profile(user_id)
    if user is None:  # check if user is registered in the system
        raise HTTPException(
            status_code=404,
            detail=f"user with ID: {user_id} not found. Please pass registration first!",
        )

    # Validation: empty form send check
    clean_text = text.strip()

    if not clean_text:
        raise HTTPException(
            status_code=400,
            detail="Text content not found. Please, enter text",
        )

    # Minimum length check
    if len(clean_text) < _ESSAY_MIN_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Text too short. Essay must be at least {_ESSAY_MIN_LENGTH} symbols",
        )

    try:
        # Saving
        essay_id = create_essay_record(user_id=user_id, text=clean_text)

        # Response to client
        return {
            "success": True,
            "message": "Essay is successfully uploaded",
            "essay_id": essay_id,
            "status": "pending",
        }

    except Exception as e:
        # Catch another server errors
        raise HTTPException(
            status_code=500, detail=f"Internal server error occurred: {str(e)}"
        )


@router.get("/{essay_id}")
def get_essay_(essay_id: str):
    essay_record = get_essay(essay_id)
    if not essay_record:
        raise HTTPException(
            status_code=404, detail=f"Essay with ID {essay_id} not found."
        )
    return essay_record
