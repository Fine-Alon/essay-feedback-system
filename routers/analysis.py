from fastapi import APIRouter, HTTPException, status

# ייבוא הפונקציות הלגו שכתבת ב-services/text_checker.py
from services.text_checker import create_report_dic

# ייבוא של פונקציות השמירה והקריאה של אלון
from services.storage import update_essay_results, get_essay

router = APIRouter()


@router.get("/essay/{essay_id}")
def get_essay_analysis_report(essay_id: str):
    """
    Endpoint שמקבל מזהה מאמר, שולף אותו מהאחסון המקומי,
    ומשתמש בפונקציות הממוקדות כדי להרכיב דוח ניתוח מלא.
    """
    essay_record = get_essay(essay_id)

    # חסימה במקרה שהקובץ לא קיים או חזר ריק
    if not essay_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Essay with ID {essay_id} not found.",
        )

    if essay_record["analysis_results"]:
        return essay_record["analysis_results"]

    update_essay_results(essay_id, create_report_dic(essay_record["original_text"]))
    return get_essay(essay_id)["analysis_results"]
