import re
from collections import Counter

from constants import _ESSAY_MIN_LENGTH, _REPEATED_WORDS_THRESHOLD


# פונקציה שסופרת את כמות המילים במאמר
def words_count(essay: str) -> int:
    if not essay or not essay.strip():
        return 0
    return len(essay.split())


# פונקציה שבודקת האם המאמר עומד באורך המינימלי הנדרש
def min_words_check(essay: str, min_words: int = _ESSAY_MIN_LENGTH) -> bool:
    return words_count(essay) >= min_words


# פונקציה שסופרת פסקאות אמיתיות (מתעלמת משורות ריקות)
def paragraphs_count(essay: str) -> int:
    if not essay or not essay.strip():
        return 0
    # נרמול ירידות השורה של חלונות ל-\n לצורך הפיצול, בלי לשנות את הטקסט המקורי בחוץ
    paragraphs = essay.replace("\r\n", "\n").split("\n\n")
    # סינון פסקאות ריקות וספירה
    return len([p for p in paragraphs if p.strip()])


# פונקציה שמחזירה מילון עם תדירות הופעה של כל מילה (נקייה מסימני פיסוק)
def get_word_segmentation(essay: str) -> dict:
    if not essay or not essay.strip():
        return {}
    # ניקוי סימני פיסוק והפיכה לאותיות קטנות ישירות בתוך הפונקציה
    cleaned = re.sub(r"[,\.\?\!\;\:\"\(\)]", " ", essay)
    words = cleaned.lower().split()
    return dict(Counter(words))


# פונקציה שמזהה מילים שחוזרות על עצמן יותר מדי פעמים
def find_repeated_words(essay: str, threshold: int = _REPEATED_WORDS_THRESHOLD) -> dict:
    all_words = get_word_segmentation(essay)
    repeated = {}
    for word, count in all_words.items():
        if count >= threshold:
            repeated[word] = count
    return repeated


# פונקציה שבודקת רווחים כפולים או מרובים בטקסט
def check_double_spaces(essay: str) -> int:
    if not essay:
        return 0
    return len(re.findall(r" {2,}", essay))


# פונקציה שבודקת פסיק, נקודה, סימן שאלה או סימן קריאה שאין אחריהם רווח
def check_missing_space_after_punctuation(essay: str) -> int:
    if not essay:
        return 0
    return len(re.findall(r"[,\.\?\!][^\s\d\.\, \?\!]", essay))


# פונקציה שבודקת רווח מיותר לפני סימן פיסוק
def check_space_before_punctuation(essay: str) -> int:
    if not essay:
        return 0
    return len(re.findall(r" +[\,\.\?\!]", essay))


# פונקציה שבודקת שורות ריקות מיותרות (3 ירידות שורה ומעלה)
def check_empty_lines(essay: str) -> int:
    if not essay:
        return 0
    return len(re.findall(r"\n{3,}", essay))


# פונקציה שבודקת שפסקאות מסתיימות בסימן פיסוק תקני (. או ? או !)
def check_missing_paragraph_punctuation(essay: str) -> int:
    if not essay or not essay.strip():
        return 0
    count = 0
    # חלוקה לפסקאות לפי ירידת שורה כפולה (\n\n)
    paragraphs = [p.strip() for p in essay.split("\n\n") if p.strip()]
    for paragraph in paragraphs:
        if not paragraph.endswith((".", "?", "!")):
            count += 1
    return count


def create_report_dic(text: str) -> dict:
    return {
        "general_metrics": {
            "total_words": words_count(text),
            "total_paragraphs": paragraphs_count(text),
            "meets_minimum_length": min_words_check(text),
        },
        "structural_issues_counters": {
            "double_spaces": check_double_spaces(text),
            "missing_space_after_punctuation": check_missing_space_after_punctuation(
                text
            ),
            "space_before_punctuation": check_space_before_punctuation(text),
            "empty_lines": check_empty_lines(text),
            "missing_paragraph_punctuation": check_missing_paragraph_punctuation(text),
        },
        "repeated_words_analysis": find_repeated_words(text),
    }
